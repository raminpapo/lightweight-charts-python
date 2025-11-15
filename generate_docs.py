#!/usr/bin/env python3
"""
Repository Book Generator - World's Best Repo Documentation Generator
Generates comprehensive documentation for the entire repository.
"""

import os
import json
import re
import hashlib
from pathlib import Path
from datetime import datetime
from collections import defaultdict

class RepoBookGenerator:
    def __init__(self, repo_root='.', docs_dir='./docs'):
        self.repo_root = Path(repo_root)
        self.docs_dir = Path(docs_dir)
        self.manifest_path = self.docs_dir / 'manifest.json'
        self.progress_log = []
        self.errors = []
        self.docs_created = 0
        self.bytes_written = 0
        self.global_keywords = defaultdict(list)

    def load_manifest(self):
        """Load the existing manifest"""
        with open(self.manifest_path, 'r') as f:
            return json.load(f)

    def save_manifest(self, manifest):
        """Save updated manifest"""
        with open(self.manifest_path, 'w') as f:
            json.dump(manifest, f, indent=2)

    def read_file_safe(self, filepath):
        """Safely read a file, handling encoding issues"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return f.read()
        except UnicodeDecodeError:
            try:
                with open(filepath, 'r', encoding='latin-1') as f:
                    return f.read()
            except Exception as e:
                return None
        except Exception as e:
            return None

    def extract_keywords(self, content, filepath):
        """Extract keywords from file content"""
        keywords = set()

        # Get file extension
        ext = Path(filepath).suffix

        # Extract based on language
        if ext in ['.py']:
            # Python: classes, functions, imports
            keywords.update(re.findall(r'class\s+(\w+)', content))
            keywords.update(re.findall(r'def\s+(\w+)', content))
            keywords.update(re.findall(r'import\s+(\w+)', content))
            keywords.update(re.findall(r'from\s+(\w+)', content))
        elif ext in ['.ts', '.js']:
            # TypeScript/JavaScript: classes, functions, interfaces
            keywords.update(re.findall(r'class\s+(\w+)', content))
            keywords.update(re.findall(r'function\s+(\w+)', content))
            keywords.update(re.findall(r'interface\s+(\w+)', content))
            keywords.update(re.findall(r'const\s+(\w+)', content))
            keywords.update(re.findall(r'export\s+\w+\s+(\w+)', content))
        elif ext in ['.md']:
            # Markdown: headers
            keywords.update(re.findall(r'#+\s+(.+)', content))

        # Common: UPPER_CASE constants
        keywords.update(re.findall(r'\b([A-Z_]{3,})\b', content))

        # Filter out common words
        stop_words = {'THE', 'AND', 'FOR', 'THIS', 'THAT', 'WITH', 'FROM', 'HAVE'}
        keywords = {k for k in keywords if k not in stop_words and len(k) > 2}

        return sorted(list(keywords))

    def generate_file_docs(self, filepath, content):
        """Generate comprehensive documentation for a single file"""
        filename = Path(filepath).name
        ext = Path(filepath).suffix

        # Count lines and estimate complexity
        lines = content.split('\n')
        line_count = len(lines)

        # Generate doc content
        doc = f"""# {filename} Documentation

## File Metadata
- **Path**: `{filepath}`
- **Extension**: `{ext}`
- **Lines of Code**: {line_count}
- **File Size**: {len(content)} bytes

## Original Source

```{ext[1:] if ext else 'text'}
{content}
```

## Overview

This file is located at `{filepath}` and contains {line_count} lines of code.

"""

        # Add language-specific analysis
        if ext == '.py':
            doc += self._analyze_python(content, filepath)
        elif ext in ['.ts', '.js']:
            doc += self._analyze_typescript(content, filepath)
        elif ext == '.md':
            doc += self._analyze_markdown(content, filepath)
        elif ext in ['.json', '.yaml', '.yml']:
            doc += self._analyze_config(content, filepath)
        elif ext in ['.css']:
            doc += self._analyze_css(content, filepath)
        else:
            doc += f"**File Type**: {ext or 'Unknown'}\n\n"
            doc += "This file contains source code or configuration data. See the original source above for details.\n\n"

        doc += f"""
## Related Files

This file is part of the repository structure. Related files may be found in the same directory or referenced in the code above.

## Tests

To test this file, refer to the repository's test suite in the `test/` directory.

## Performance & Security Notes

- Always review code for potential security vulnerabilities
- Ensure proper error handling is implemented
- Follow best practices for the language/framework being used
"""

        return doc

    def _analyze_python(self, content, filepath):
        """Analyze Python file"""
        analysis = "## Python Code Analysis\n\n"

        # Find classes
        classes = re.findall(r'class\s+(\w+).*?:', content)
        if classes:
            analysis += "### Classes\n\n"
            for cls in classes:
                analysis += f"- **{cls}**: Class defined in this file\n"
            analysis += "\n"

        # Find functions
        functions = re.findall(r'def\s+(\w+)\s*\(([^)]*)\)', content)
        if functions:
            analysis += "### Functions\n\n"
            for func, args in functions:
                analysis += f"- **{func}**({args}): Function implementation\n"
            analysis += "\n"

        # Find imports
        imports = re.findall(r'(?:from\s+[\w.]+\s+)?import\s+(.+)', content)
        if imports:
            analysis += "### Dependencies\n\n"
            for imp in imports[:10]:  # Limit to first 10
                analysis += f"- {imp.strip()}\n"
            analysis += "\n"

        return analysis

    def _analyze_typescript(self, content, filepath):
        """Analyze TypeScript/JavaScript file"""
        analysis = "## TypeScript/JavaScript Code Analysis\n\n"

        # Find interfaces
        interfaces = re.findall(r'interface\s+(\w+)', content)
        if interfaces:
            analysis += "### Interfaces\n\n"
            for iface in interfaces:
                analysis += f"- **{iface}**: Interface definition\n"
            analysis += "\n"

        # Find classes
        classes = re.findall(r'class\s+(\w+)', content)
        if classes:
            analysis += "### Classes\n\n"
            for cls in classes:
                analysis += f"- **{cls}**: Class implementation\n"
            analysis += "\n"

        # Find functions
        functions = re.findall(r'function\s+(\w+)', content)
        if functions:
            analysis += "### Functions\n\n"
            for func in functions:
                analysis += f"- **{func}**: Function implementation\n"
            analysis += "\n"

        # Find exports
        exports = re.findall(r'export\s+(?:default\s+)?(?:class|function|const|interface)\s+(\w+)', content)
        if exports:
            analysis += "### Exports\n\n"
            for exp in exports:
                analysis += f"- **{exp}**: Exported symbol\n"
            analysis += "\n"

        return analysis

    def _analyze_markdown(self, content, filepath):
        """Analyze Markdown file"""
        analysis = "## Markdown Document Analysis\n\n"

        # Find headers
        headers = re.findall(r'^(#+)\s+(.+)$', content, re.MULTILINE)
        if headers:
            analysis += "### Document Structure\n\n"
            for level, title in headers[:20]:
                indent = "  " * (len(level) - 1)
                analysis += f"{indent}- {title}\n"
            analysis += "\n"

        return analysis

    def _analyze_config(self, content, filepath):
        """Analyze configuration file"""
        analysis = "## Configuration File Analysis\n\n"
        analysis += "This file contains configuration data in structured format.\n\n"

        if filepath.endswith('.json'):
            try:
                data = json.loads(content)
                analysis += f"### Top-level keys ({len(data)} total)\n\n"
                for key in list(data.keys())[:20]:
                    analysis += f"- **{key}**\n"
            except:
                pass

        return analysis

    def _analyze_css(self, content, filepath):
        """Analyze CSS file"""
        analysis = "## CSS Stylesheet Analysis\n\n"

        # Find selectors
        selectors = re.findall(r'([.#]?[\w-]+)\s*{', content)
        if selectors:
            analysis += f"### Selectors ({len(selectors)} total)\n\n"
            for sel in selectors[:30]:
                analysis += f"- `{sel}`\n"
            analysis += "\n"

        return analysis

    def generate_file_keywords(self, filepath, content, keywords):
        """Generate keyword index for a single file"""
        filename = Path(filepath).name

        kw_doc = f"""# {filename} - Keywords Index

## Extracted Keywords

This file contains {len(keywords)} keywords extracted from the source code.

"""

        for kw in sorted(keywords):
            kw_doc += f"""### {kw}

**Keyword**: `{kw}`
**Source File**: [{filepath}]({filename}_docs.md)
**Description**: Identifier found in {filepath}

---

"""

        return kw_doc

    def process_file(self, file_info, manifest):
        """Process a single file and generate documentation"""
        filepath = file_info['path']
        file_type = file_info['type']
        is_binary = file_info['is_binary']

        # Skip binary files and some large files
        if is_binary:
            # Create a small doc for binary files
            doc_path = self.docs_dir / filepath / f"{Path(filepath).name}_docs.md"
            doc_path.parent.mkdir(parents=True, exist_ok=True)

            binary_doc = f"""# {Path(filepath).name} (Binary File)

## File Metadata
- **Path**: `{filepath}`
- **Type**: Binary
- **Size**: {file_info['size']} bytes

## Description

This is a binary file and cannot be displayed as text.

**Suggested Handling**: View using appropriate application for this file type.
"""
            with open(doc_path, 'w') as f:
                f.write(binary_doc)

            self.docs_created += 1
            self.bytes_written += len(binary_doc)
            return

        # Read file content
        full_path = self.repo_root / filepath
        content = self.read_file_safe(full_path)

        if content is None:
            self.errors.append(f"Could not read {filepath}")
            return

        # Extract keywords
        keywords = self.extract_keywords(content, filepath)

        # Store global keywords
        for kw in keywords:
            self.global_keywords[kw].append(filepath)

        # Generate docs
        doc_content = self.generate_file_docs(filepath, content)
        kw_content = self.generate_file_keywords(filepath, content, keywords)

        # Save docs
        doc_dir = self.docs_dir / Path(filepath).parent
        doc_dir.mkdir(parents=True, exist_ok=True)

        doc_path = doc_dir / f"{Path(filepath).name}_docs.md"
        kw_path = doc_dir / f"{Path(filepath).name}_kw.md"

        with open(doc_path, 'w') as f:
            f.write(doc_content)
        with open(kw_path, 'w') as f:
            f.write(kw_content)

        self.docs_created += 2
        self.bytes_written += len(doc_content) + len(kw_content)

        # Add to progress log
        self.progress_log.append({
            'file': filepath,
            'docs_created': 2,
            'bytes': len(doc_content) + len(kw_content)
        })

    def generate_folder_docs(self, folder, manifest):
        """Generate folder-level documentation"""
        folder_path = Path(folder) if folder else Path('.')

        # Get files and subfolders in this folder
        files_in_folder = [f for f in manifest['files']
                          if Path(f['path']).parent == folder_path]
        subfolders = [f for f in manifest['folders']
                     if Path(f).parent == folder_path]

        # Create index.md
        index_content = f"""# {folder or 'Root'} - Index

## Directory: `{folder or '.'}`

"""

        if files_in_folder:
            index_content += f"### Files ({len(files_in_folder)})\n\n"
            for file_info in files_in_folder:
                fname = Path(file_info['path']).name
                index_content += f"- [{fname}]({fname}_docs.md) ({file_info['size']} bytes)\n"
            index_content += "\n"

        if subfolders:
            index_content += f"### Subdirectories ({len(subfolders)})\n\n"
            for subfolder in sorted(subfolders):
                subfolder_name = Path(subfolder).name
                rel_path = os.path.relpath(subfolder, folder) if folder else subfolder
                index_content += f"- [{subfolder_name}]({rel_path}/index.md)\n"
            index_content += "\n"

        # Create doc.md
        doc_content = f"""# {folder or 'Root'} - Documentation

## Overview

This directory contains {len(files_in_folder)} files and {len(subfolders)} subdirectories.

## Purpose

"""

        # Add context based on folder name
        folder_name = Path(folder).name if folder else 'root'
        if folder_name in ['src', 'source']:
            doc_content += "This directory contains the main source code for the project.\n\n"
        elif folder_name in ['test', 'tests']:
            doc_content += "This directory contains test files and test utilities.\n\n"
        elif folder_name == 'docs':
            doc_content += "This directory contains documentation files.\n\n"
        elif folder_name == 'examples':
            doc_content += "This directory contains example code and demonstrations.\n\n"
        else:
            doc_content += f"This directory is part of the project structure.\n\n"

        doc_content += """## Files

See the index.md file for a complete list of files in this directory.

## Navigation

- [Index](index.md) - Complete file listing
- [Keywords](sub.md) - Keyword index for this directory
"""

        # Create sub.md (merged keywords)
        sub_content = f"""# {folder or 'Root'} - Keyword Index

## Keywords from All Files

"""

        # Collect keywords from files in this folder
        folder_keywords = defaultdict(list)
        for file_info in files_in_folder:
            fname = Path(file_info['path']).name
            kw_path = self.docs_dir / folder_path / f"{fname}_kw.md"
            if kw_path.exists():
                # Read keywords from _kw.md file
                kw_content = self.read_file_safe(kw_path)
                if kw_content:
                    # Extract keyword headers
                    keywords = re.findall(r'^### (.+)$', kw_content, re.MULTILINE)
                    for kw in keywords:
                        folder_keywords[kw].append(fname)

        # Write sorted keywords
        for kw in sorted(folder_keywords.keys()):
            sub_content += f"### {kw}\n\n"
            sub_content += f"Found in: {', '.join(folder_keywords[kw])}\n\n"

        # Save folder docs
        folder_doc_dir = self.docs_dir / folder_path
        folder_doc_dir.mkdir(parents=True, exist_ok=True)

        with open(folder_doc_dir / 'index.md', 'w') as f:
            f.write(index_content)
        with open(folder_doc_dir / 'doc.md', 'w') as f:
            f.write(doc_content)
        with open(folder_doc_dir / 'sub.md', 'w') as f:
            f.write(sub_content)

        self.docs_created += 3
        self.bytes_written += len(index_content) + len(doc_content) + len(sub_content)

    def run(self):
        """Main execution"""
        print("Loading manifest...")
        manifest = self.load_manifest()

        print(f"Processing {manifest['file_count']} files...")

        # Process each file
        for i, file_info in enumerate(manifest['files']):
            if i % 10 == 0:
                print(f"  Progress: {i}/{manifest['file_count']}")
            try:
                self.process_file(file_info, manifest)
            except Exception as e:
                error_msg = f"Error processing {file_info['path']}: {str(e)}"
                self.errors.append(error_msg)
                print(f"  ERROR: {error_msg}")

        print(f"\nProcessing {manifest['folder_count']} folders...")

        # Process root folder
        self.generate_folder_docs('', manifest)

        # Process each folder
        for folder in sorted(manifest['folders']):
            try:
                self.generate_folder_docs(folder, manifest)
            except Exception as e:
                error_msg = f"Error processing folder {folder}: {str(e)}"
                self.errors.append(error_msg)
                print(f"  ERROR: {error_msg}")

        # Update manifest
        manifest['docs_created'] = self.docs_created
        manifest['bytes_written'] = self.bytes_written
        manifest['processing_timestamp'] = datetime.now().isoformat()

        self.save_manifest(manifest)

        print(f"\nCompleted!")
        print(f"  Docs created: {self.docs_created}")
        print(f"  Bytes written: {self.bytes_written}")
        print(f"  Errors: {len(self.errors)}")

        return {
            'docs_created': self.docs_created,
            'bytes_written': self.bytes_written,
            'errors': self.errors,
            'global_keywords': dict(self.global_keywords)
        }


if __name__ == '__main__':
    generator = RepoBookGenerator()
    result = generator.run()

    print("\nResult:")
    print(json.dumps({
        'docs_created': result['docs_created'],
        'bytes_written': result['bytes_written'],
        'error_count': len(result['errors'])
    }, indent=2))
