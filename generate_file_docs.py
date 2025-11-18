#!/usr/bin/env python3
"""
Per-File Documentation Generator
Generates _docs.md and _kw.md for each text file
"""

import os
import json
import re
import hashlib
from pathlib import Path
from datetime import datetime
from collections import defaultdict

class FileDocGenerator:
    def __init__(self, repo_path, docs_path):
        self.repo_path = Path(repo_path)
        self.docs_path = Path(docs_path)
        self.progress = []
        self.keywords_global = defaultdict(list)
        self.docs_created = 0
        self.bytes_written = 0

    def safe_read_file(self, filepath):
        """Safely read file content"""
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                return f.read()
        except Exception as e:
            return f"[ERROR: Could not read file - {str(e)}]"

    def detect_language(self, filepath):
        """Detect programming language from file extension"""
        ext = Path(filepath).suffix.lower()
        lang_map = {
            '.py': 'python',
            '.js': 'javascript',
            '.ts': 'typescript',
            '.tsx': 'typescript',
            '.jsx': 'javascript',
            '.html': 'html',
            '.css': 'css',
            '.json': 'json',
            '.yaml': 'yaml',
            '.yml': 'yaml',
            '.md': 'markdown',
            '.sh': 'bash',
            '.toml': 'toml',
            '.cfg': 'ini',
            '.ini': 'ini',
        }
        return lang_map.get(ext, '')

    def extract_functions_classes(self, content, filepath):
        """Extract functions, classes, and other code elements"""
        ext = Path(filepath).suffix.lower()
        elements = {
            'classes': [],
            'functions': [],
            'variables': [],
            'imports': [],
            'exports': []
        }

        if ext == '.py':
            # Classes
            for match in re.finditer(r'^class\s+(\w+).*?:', content, re.MULTILINE):
                line_num = content[:match.start()].count('\n') + 1
                elements['classes'].append({'name': match.group(1), 'line': line_num})

            # Functions
            for match in re.finditer(r'^def\s+(\w+)\s*\((.*?)\)', content, re.MULTILINE):
                line_num = content[:match.start()].count('\n') + 1
                elements['functions'].append({
                    'name': match.group(1),
                    'params': match.group(2),
                    'line': line_num
                })

            # Imports
            for match in re.finditer(r'^(?:from\s+([\w.]+)\s+)?import\s+(.*?)$', content, re.MULTILINE):
                elements['imports'].append(match.group(0))

        elif ext in {'.js', '.ts', '.jsx', '.tsx'}:
            # Classes
            for match in re.finditer(r'\bclass\s+(\w+)', content):
                line_num = content[:match.start()].count('\n') + 1
                elements['classes'].append({'name': match.group(1), 'line': line_num})

            # Functions
            for match in re.finditer(r'\bfunction\s+(\w+)\s*\((.*?)\)', content):
                line_num = content[:match.start()].count('\n') + 1
                elements['functions'].append({
                    'name': match.group(1),
                    'params': match.group(2),
                    'line': line_num
                })

            # Arrow functions
            for match in re.finditer(r'\bconst\s+(\w+)\s*=\s*\([^)]*\)\s*=>', content):
                line_num = content[:match.start()].count('\n') + 1
                elements['functions'].append({'name': match.group(1), 'line': line_num})

            # Exports
            for match in re.finditer(r'^export\s+(?:default\s+)?(?:class|function|const|let|var)\s+(\w+)', content, re.MULTILINE):
                elements['exports'].append(match.group(1))

        return elements

    def extract_keywords(self, content, filepath):
        """Extract keywords from content"""
        keywords = set()
        ext = Path(filepath).suffix.lower()

        # Get code elements
        elements = self.extract_functions_classes(content, filepath)

        # Add all identifiers
        for cls in elements['classes']:
            keywords.add(cls['name'])
        for func in elements['functions']:
            keywords.add(func['name'])

        # Extract CamelCase identifiers
        for match in re.finditer(r'\b([A-Z][a-z]+(?:[A-Z][a-z]+)+)\b', content):
            keywords.add(match.group(1))

        # Extract snake_case identifiers (3+ chars)
        for match in re.finditer(r'\b([a-z]+_[a-z_]+)\b', content):
            if len(match.group(1)) > 3:
                keywords.add(match.group(1))

        # Extract CONSTANT_NAMES
        for match in re.finditer(r'\b([A-Z][A-Z_]{2,})\b', content):
            keywords.add(match.group(1))

        return sorted(keywords)

    def generate_docs_md(self, filepath, rel_path):
        """Generate comprehensive _docs.md file"""
        content = self.safe_read_file(filepath)
        lang = self.detect_language(filepath)
        elements = self.extract_functions_classes(content, filepath)
        ext = Path(filepath).suffix.lower()

        file_size = os.path.getsize(filepath)
        line_count = content.count('\n') + 1

        # Build documentation
        docs = []
        docs.append(f"# {Path(rel_path).name}\n")
        docs.append(f"**File Path:** `{rel_path}`\n")
        docs.append(f"**File Size:** {file_size:,} bytes")
        docs.append(f"**Lines of Code:** {line_count:,}")
        docs.append(f"**Language:** {lang or 'Unknown'}\n")
        docs.append("---\n")

        # Metadata section
        docs.append("## File Metadata\n")
        docs.append(f"- **Relative Path:** `{rel_path}`")
        docs.append(f"- **File Type:** {Path(rel_path).suffix or 'No extension'}")
        docs.append(f"- **Size:** {file_size:,} bytes")
        docs.append(f"- **Total Lines:** {line_count:,}")
        docs.append(f"- **Programming Language:** {lang or 'Unknown'}\n")

        # Quick summary
        docs.append("## Quick Summary\n")
        docs.append(f"This file is part of the lightweight-charts-python repository.")

        if elements['classes']:
            docs.append(f" It defines {len(elements['classes'])} class(es).")
        if elements['functions']:
            docs.append(f" It contains {len(elements['functions'])} function(s).")
        docs.append("\n")

        # Original source
        docs.append("## Original Source Code\n")
        docs.append(f"```{lang}\n")
        # Truncate if very large (>50k lines), but prefer full content
        if line_count > 50000:
            lines = content.split('\n')
            docs.append('\n'.join(lines[:1000]))
            docs.append(f"\n\n... [Truncated: {line_count - 1000} more lines] ...\n\n")
            docs.append('\n'.join(lines[-100:]))
        else:
            docs.append(content)
        docs.append("\n```\n")

        # High-level overview
        docs.append("## High-Level Overview\n")

        if elements['classes']:
            docs.append(f"### Classes ({len(elements['classes'])})\n")
            for cls in elements['classes']:
                docs.append(f"- **`{cls['name']}`** (line {cls['line']})")
            docs.append("")

        if elements['functions']:
            docs.append(f"### Functions ({len(elements['functions'])})\n")
            for func in elements['functions'][:50]:  # Limit to first 50
                params = func.get('params', '')
                docs.append(f"- **`{func['name']}({params})`** (line {func['line']})")
            if len(elements['functions']) > 50:
                docs.append(f"- ... and {len(elements['functions']) - 50} more functions")
            docs.append("")

        if elements['imports']:
            docs.append(f"### Imports ({len(elements['imports'])})\n")
            for imp in elements['imports'][:20]:  # First 20
                docs.append(f"- `{imp}`")
            if len(elements['imports']) > 20:
                docs.append(f"- ... and {len(elements['imports']) - 20} more imports")
            docs.append("")

        # Detailed walkthrough
        docs.append("## Detailed Walkthrough\n")
        docs.append("### Code Structure\n")
        docs.append(f"This file contains {line_count:,} lines of {lang or 'code'}.")

        if elements['classes']:
            docs.append("\n#### Classes\n")
            for cls in elements['classes']:
                docs.append(f"##### {cls['name']} (Line {cls['line']})\n")
                # Try to extract class docstring or first few lines
                class_pattern = rf"class\s+{cls['name']}.*?:\s*\n(.*?)(?:\n\s*\n|\nclass |\ndef )"
                match = re.search(class_pattern, content, re.DOTALL)
                if match:
                    snippet = match.group(1)[:500]
                    docs.append(f"```{lang}\n{snippet}\n```\n")

        if elements['functions']:
            docs.append("\n#### Functions\n")
            for func in elements['functions'][:20]:  # Detail first 20 functions
                docs.append(f"##### {func['name']} (Line {func['line']})\n")
                docs.append(f"**Parameters:** `{func.get('params', 'None')}`\n")

        # Usage examples
        docs.append("## Usage Examples\n")
        docs.append(f"To use this file in your project:\n")
        if ext == '.py':
            module_path = rel_path.replace('/', '.').replace('\\', '.').replace('.py', '')
            docs.append(f"```python\nfrom {module_path} import *\n```\n")
        elif ext in {'.js', '.ts'}:
            docs.append(f"```javascript\nimport {{ ... }} from './{rel_path}';\n```\n")

        # Performance and security notes
        docs.append("## Performance & Security Notes\n")
        docs.append("### Performance\n")
        docs.append(f"- File size: {file_size:,} bytes")
        docs.append(f"- Complexity: {len(elements['functions'])} functions, {len(elements['classes'])} classes\n")

        docs.append("### Security\n")
        docs.append("- **Recommendation:** Review this file for potential security vulnerabilities")
        # Check for potential security issues
        security_patterns = {
            'eval': r'\beval\s*\(',
            'exec': r'\bexec\s*\(',
            'shell': r'\bshell\s*=\s*True',
            'sql': r'(?:execute|query)\s*\([^)]*%[sd]',
        }
        issues_found = []
        for issue, pattern in security_patterns.items():
            if re.search(pattern, content, re.IGNORECASE):
                issues_found.append(issue)

        if issues_found:
            docs.append(f"- **Warning:** Potential security concerns found: {', '.join(issues_found)}")
        else:
            docs.append("- No obvious security concerns detected (basic scan)")
        docs.append("")

        # Related files
        docs.append("## Related Files\n")
        docs.append("*To be populated during folder indexing phase*\n")

        # Tests and how to run
        docs.append("## Testing\n")
        if 'test' in rel_path.lower():
            docs.append("This file is a test file.\n")
            docs.append("**How to run:**\n")
            docs.append("```bash\n")
            if ext == '.py':
                docs.append(f"pytest {rel_path}\n")
            docs.append("```\n")
        else:
            docs.append("Tests for this file may be located in the `test/` directory.\n")

        # Footer
        docs.append("---\n")
        docs.append(f"*Documentation generated on {datetime.now().isoformat()}*\n")

        return '\n'.join(docs)

    def generate_kw_md(self, filepath, rel_path, keywords):
        """Generate _kw.md keyword file"""
        content = self.safe_read_file(filepath)

        kw_docs = []
        kw_docs.append(f"# Keywords: {Path(rel_path).name}\n")
        kw_docs.append(f"**Source File:** `{rel_path}`")
        kw_docs.append(f"**Total Keywords:** {len(keywords)}\n")
        kw_docs.append("---\n")

        kw_docs.append("## Keyword Index (A-Z)\n")

        # Group keywords alphabetically
        keyword_groups = defaultdict(list)
        for kw in keywords:
            first_letter = kw[0].upper()
            keyword_groups[first_letter].append(kw)

        for letter in sorted(keyword_groups.keys()):
            kw_docs.append(f"### {letter}\n")
            for kw in sorted(keyword_groups[letter]):
                # Try to find context
                context = ""
                # Find keyword in content
                pattern = rf'\b{re.escape(kw)}\b'
                matches = list(re.finditer(pattern, content))

                if matches:
                    # Get first occurrence with context
                    match = matches[0]
                    start = max(0, match.start() - 100)
                    end = min(len(content), match.end() + 100)
                    snippet = content[start:end].replace('\n', ' ')
                    context = f"*...{snippet}...*"

                kw_docs.append(f"#### `{kw}`\n")
                kw_docs.append(f"- **Occurrences:** {len(matches)}")
                kw_docs.append(f"- **Context:** {context}")
                kw_docs.append(f"- **Link:** [View in docs](./{Path(rel_path).stem}_docs.md)\n")

        kw_docs.append("---\n")
        kw_docs.append(f"*Keywords extracted on {datetime.now().isoformat()}*\n")

        return '\n'.join(kw_docs)

    def process_file(self, rel_path):
        """Process a single file and generate its documentation"""
        filepath = self.repo_path / rel_path

        # Create docs directory structure
        docs_dir = self.docs_path / Path(rel_path).parent
        docs_dir.mkdir(parents=True, exist_ok=True)

        # Generate documentation
        try:
            # Generate _docs.md
            docs_content = self.generate_docs_md(filepath, rel_path)
            docs_filename = f"{Path(rel_path).stem}_docs.md"
            docs_path = docs_dir / docs_filename

            with open(docs_path, 'w', encoding='utf-8') as f:
                f.write(docs_content)

            docs_size = len(docs_content.encode('utf-8'))
            self.bytes_written += docs_size
            self.docs_created += 1

            # Generate _kw.md
            content = self.safe_read_file(filepath)
            keywords = self.extract_keywords(content, filepath)

            kw_content = self.generate_kw_md(filepath, rel_path, keywords)
            kw_filename = f"{Path(rel_path).stem}_kw.md"
            kw_path = docs_dir / kw_filename

            with open(kw_path, 'w', encoding='utf-8') as f:
                f.write(kw_content)

            kw_size = len(kw_content.encode('utf-8'))
            self.bytes_written += kw_size
            self.docs_created += 1

            # Track keywords globally
            for kw in keywords:
                self.keywords_global[kw].append(rel_path)

            # Log progress
            self.progress.append({
                'file': rel_path,
                'docs_created': 2,
                'bytes': docs_size + kw_size,
                'keywords': len(keywords),
                'status': 'success'
            })

            return True, None

        except Exception as e:
            self.progress.append({
                'file': rel_path,
                'status': 'error',
                'error': str(e)
            })
            return False, str(e)

# Main execution
if __name__ == '__main__':
    import sys

    # Load file classifications
    with open('/tmp/file_classifications.json', 'r') as f:
        classifications = json.load(f)

    text_files = classifications['text_files']

    generator = FileDocGenerator(
        '/home/user/lightweight-charts-python',
        '/home/user/lightweight-charts-python/docs'
    )

    print(f"Processing {len(text_files)} text files...")

    success_count = 0
    error_count = 0

    for i, rel_path in enumerate(text_files, 1):
        print(f"[{i}/{len(text_files)}] Processing: {rel_path}")
        success, error = generator.process_file(rel_path)

        if success:
            success_count += 1
        else:
            error_count += 1
            print(f"  ERROR: {error}")

        # Progress update every 10 files
        if i % 10 == 0:
            print(f"  Progress: {success_count} succeeded, {error_count} failed")
            print(f"  Docs created: {generator.docs_created}")
            print(f"  Bytes written: {generator.bytes_written:,}")

    # Save progress and keywords
    with open(generator.docs_path / '.file_progress.json', 'w') as f:
        json.dump(generator.progress, f, indent=2)

    with open('/tmp/keywords_global.json', 'w') as f:
        json.dump(dict(generator.keywords_global), f, indent=2)

    print(f"\n=== File Documentation Complete ===")
    print(f"Files processed: {len(text_files)}")
    print(f"Success: {success_count}")
    print(f"Errors: {error_count}")
    print(f"Docs created: {generator.docs_created}")
    print(f"Bytes written: {generator.bytes_written:,}")
    print(f"Unique keywords: {len(generator.keywords_global)}")
