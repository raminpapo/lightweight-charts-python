# repo_book_generator.py

**File Path:** `repo_book_generator.py`

**File Size:** 8,396 bytes
**Lines of Code:** 233
**Language:** python

---

## File Metadata

- **Relative Path:** `repo_book_generator.py`
- **File Type:** .py
- **Size:** 8,396 bytes
- **Total Lines:** 233
- **Programming Language:** python

## Quick Summary

This file is part of the lightweight-charts-python repository.
 It defines 1 class(es).


## Original Source Code

```python

#!/usr/bin/env python3
"""
World's Best Repo Book Generator and Index Builder
Generates comprehensive documentation for the entire repository
"""

import os
import json
import hashlib
import mimetypes
from pathlib import Path
from datetime import datetime
from collections import defaultdict
import re

class RepoBookGenerator:
    def __init__(self, repo_path, docs_path):
        self.repo_path = Path(repo_path)
        self.docs_path = Path(docs_path)
        self.manifest = {
            "repo_source": str(self.repo_path),
            "repo_fingerprint": "",
            "commit_sha": "",
            "file_count": 0,
            "docs_count": 0,
            "bytes_written": 0,
            "timestamp_start": datetime.now().isoformat(),
            "timestamp_end": "",
            "generator_version": "1.0.0",
            "files_map": {},
            "checksums": {}
        }
        self.file_classifications = {
            "text": [],
            "binary": [],
            "large": [],
            "ignored": []
        }
        self.progress_log = []
        self.keywords_global = defaultdict(list)

        # File extensions for text files
        self.text_extensions = {
            '.py', '.md', '.txt', '.json', '.yaml', '.yml', '.toml', '.cfg',
            '.ini', '.js', '.ts', '.html', '.css', '.sh', '.bash', '.xml',
            '.rst', '.gitignore', '.env', '.editorconfig', '.LICENSE', '.rst',
            '.tex', '.bib', '.c', '.cpp', '.h', '.hpp', '.java', '.go', '.rs',
            '.rb', '.php', '.pl', '.r', '.R', '.sql', '.lua', '.vim', '.jsx',
            '.tsx', '.vue', '.scss', '.sass', '.less', '.dockerfile', '.lock'
        }

        # Binary/ignore patterns
        self.ignore_patterns = {'.git', '__pycache__', 'node_modules', '.pyc', '.so', '.dll'}
        self.binary_extensions = {
            '.png', '.jpg', '.jpeg', '.gif', '.ico', '.svg', '.pdf', '.zip',
            '.tar', '.gz', '.bz2', '.xz', '.7z', '.rar', '.exe', '.bin', '.whl',
            '.egg', '.woff', '.woff2', '.ttf', '.eot', '.mp4', '.mp3', '.wav',
            '.avi', '.mov', '.pyc', '.pyo', '.pyd', '.db', '.sqlite'
        }

    def get_commit_sha(self):
        """Get current git commit SHA"""
        try:
            result = os.popen('git -C {} rev-parse HEAD'.format(self.repo_path)).read().strip()
            return result
        except:
            return "unknown"

    def compute_fingerprint(self, file_list):
        """Compute repository fingerprint from file list"""
        hasher = hashlib.sha256()
        for f in sorted(file_list):
            hasher.update(str(f).encode())
        return hasher.hexdigest()[:16]

    def should_ignore(self, path):
        """Check if path should be ignored"""
        parts = Path(path).parts
        for pattern in self.ignore_patterns:
            if pattern in parts:
                return True
        return False

    def classify_file(self, filepath):
        """Classify file as text, binary, large, or ignored"""
        if self.should_ignore(filepath):
            return "ignored"

        ext = Path(filepath).suffix.lower()

        # Check if binary
        if ext in self.binary_extensions:
            return "binary"

        # Check size
        try:
            size = os.path.getsize(filepath)
            if size > 100 * 1024 * 1024:  # 100MB
                return "large"
        except:
            return "ignored"

        # Check if text
        if ext in self.text_extensions or ext == '':
            # Try to read as text
            try:
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                    f.read(1024)
                return "text"
            except:
                return "binary"

        return "binary"

    def scan_repository(self):
        """Scan all files and classify them"""
        all_files = []

        for root, dirs, files in os.walk(self.repo_path):
            # Filter out ignored directories
            dirs[:] = [d for d in dirs if not self.should_ignore(os.path.join(root, d))]

            for file in files:
                filepath = os.path.join(root, file)
                rel_path = os.path.relpath(filepath, self.repo_path)

                # Skip if in docs directory (our output)
                if rel_path.startswith('docs/') or rel_path.startswith('docs\\'):
                    continue

                classification = self.classify_file(filepath)
                self.file_classifications[classification].append(rel_path)
                all_files.append(rel_path)

                self.manifest['files_map'][rel_path] = {
                    'type': classification,
                    'size': os.path.getsize(filepath) if os.path.exists(filepath) else 0,
                    'extension': Path(filepath).suffix
                }

        self.manifest['file_count'] = len(all_files)
        self.manifest['commit_sha'] = self.get_commit_sha()
        self.manifest['repo_fingerprint'] = self.compute_fingerprint(all_files)

        return all_files

    def extract_keywords_from_code(self, content, filepath):
        """Extract keywords from source code"""
        keywords = set()
        ext = Path(filepath).suffix

        # Python-specific keyword extraction
        if ext == '.py':
            # Classes
            for match in re.finditer(r'class\s+(\w+)', content):
                keywords.add(match.group(1))
            # Functions
            for match in re.finditer(r'def\s+(\w+)', content):
                keywords.add(match.group(1))
            # Imports
            for match in re.finditer(r'(?:from|import)\s+([\w.]+)', content):
                keywords.add(match.group(1))

        # JavaScript/TypeScript keyword extraction
        elif ext in {'.js', '.ts', '.jsx', '.tsx'}:
            # Functions
            for match in re.finditer(r'function\s+(\w+)', content):
                keywords.add(match.group(1))
            # Classes
            for match in re.finditer(r'class\s+(\w+)', content):
                keywords.add(match.group(1))
            # Const/let/var
            for match in re.finditer(r'(?:const|let|var)\s+(\w+)', content):
                keywords.add(match.group(1))

        # General identifier extraction (CamelCase, snake_case)
        for match in re.finditer(r'\b([A-Z][a-z]+(?:[A-Z][a-z]+)+)\b', content):
            keywords.add(match.group(1))
        for match in re.finditer(r'\b([a-z]+_[a-z_]+)\b', content):
            if len(match.group(1)) > 3:
                keywords.add(match.group(1))

        return sorted(keywords)

    def save_progress(self):
        """Save progress to log file"""
        with open(self.docs_path / '.progress.log', 'w') as f:
            json.dump(self.progress_log, f, indent=2)

    def save_manifest(self):
        """Save manifest to JSON file"""
        self.manifest['timestamp_end'] = datetime.now().isoformat()
        manifest_path = self.docs_path / 'manifest.json'
        with open(manifest_path, 'w') as f:
            json.dump(self.manifest, f, indent=2)
        return manifest_path

# Initialize generator
generator = RepoBookGenerator(
    '/home/user/lightweight-charts-python',
    '/home/user/lightweight-charts-python/docs'
)

# Execute scan
print("Scanning repository...")
all_files = generator.scan_repository()

print(f"\n=== Repository Scan Results ===")
print(f"Total files: {len(all_files)}")
print(f"Text files: {len(generator.file_classifications['text'])}")
print(f"Binary files: {len(generator.file_classifications['binary'])}")
print(f"Large files: {len(generator.file_classifications['large'])}")
print(f"Ignored files: {len(generator.file_classifications['ignored'])}")
print(f"Commit SHA: {generator.manifest['commit_sha']}")
print(f"Fingerprint: {generator.manifest['repo_fingerprint']}")

# Save initial manifest
manifest_path = generator.save_manifest()
print(f"\nInitial manifest saved to: {manifest_path}")

# Output classifications for further processing
output = {
    'text_files': generator.file_classifications['text'],
    'binary_files': generator.file_classifications['binary'],
    'large_files': generator.file_classifications['large'],
    'total_files': len(all_files)
}

with open('/tmp/file_classifications.json', 'w') as f:
    json.dump(output, f, indent=2)

print("\nFile classifications saved to /tmp/file_classifications.json")


```

## High-Level Overview

### Classes (1)

- **`RepoBookGenerator`** (line 16)

### Imports (8)

- `import os`
- `import json`
- `import hashlib`
- `import mimetypes`
- `from pathlib import Path`
- `from datetime import datetime`
- `from collections import defaultdict`
- `import re`

## Detailed Walkthrough

### Code Structure

This file contains 233 lines of python.

#### Classes

##### RepoBookGenerator (Line 16)

```python
    def __init__(self, repo_path, docs_path):
        self.repo_path = Path(repo_path)
        self.docs_path = Path(docs_path)
        self.manifest = {
            "repo_source": str(self.repo_path),
            "repo_fingerprint": "",
            "commit_sha": "",
            "file_count": 0,
            "docs_count": 0,
            "bytes_written": 0,
            "timestamp_start": datetime.now().isoformat(),
            "timestamp_end": "",
            "generator_version": "1.0.0",
        
```

## Usage Examples

To use this file in your project:

```python
from repo_book_generator import *
```

## Performance & Security Notes

### Performance

- File size: 8,396 bytes
- Complexity: 0 functions, 1 classes

### Security

- **Recommendation:** Review this file for potential security vulnerabilities
- No obvious security concerns detected (basic scan)

## Related Files

*To be populated during folder indexing phase*

## Testing

Tests for this file may be located in the `test/` directory.

---

*Documentation generated on 2025-11-18T21:53:48.988421*
