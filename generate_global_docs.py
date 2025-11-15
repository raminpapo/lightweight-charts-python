#!/usr/bin/env python3
"""
Generate global documentation artifacts: keywords.md, index.md, comprehensive_book.md
"""

import os
import json
import re
import hashlib
from pathlib import Path
from collections import defaultdict

def load_manifest():
    with open('docs/manifest.json', 'r') as f:
        return json.load(f)

def read_file_safe(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except:
        return ""

def generate_global_keywords():
    """Generate global keywords.md from all _kw.md files"""
    print("Generating global keywords index...")

    global_keywords = defaultdict(list)

    # Find all _kw.md files
    for root, dirs, files in os.walk('docs'):
        for file in files:
            if file.endswith('_kw.md'):
                kw_path = Path(root) / file
                content = read_file_safe(kw_path)

                # Extract keywords
                keywords = re.findall(r'^### (.+)$', content, re.MULTILINE)

                # Get source file path
                source_file = file.replace('_kw.md', '')
                rel_path = os.path.relpath(root, 'docs')

                for kw in keywords:
                    if rel_path == '.':
                        file_ref = f"{source_file}"
                    else:
                        file_ref = f"{rel_path}/{source_file}"
                    global_keywords[kw].append(file_ref)

    # Write global keywords
    kw_content = """# Global Keywords Index

## All Keywords from Repository (A-Z)

This index contains all keywords extracted from the entire repository, sorted alphabetically.

---

"""

    for kw in sorted(global_keywords.keys()):
        kw_content += f"### {kw}\n\n"
        files = global_keywords[kw]
        kw_content += f"**Found in {len(files)} file(s)**:\n\n"
        for f in sorted(set(files))[:10]:  # Limit to 10 occurrences
            kw_content += f"- `{f}`\n"
        if len(set(files)) > 10:
            kw_content += f"- ... and {len(set(files)) - 10} more\n"
        kw_content += "\n---\n\n"

    with open('docs/keywords.md', 'w') as f:
        f.write(kw_content)

    print(f"  Created keywords.md with {len(global_keywords)} keywords")
    return len(kw_content)

def generate_global_index():
    """Generate root index.md linking to all folders"""
    print("Generating global index...")

    manifest = load_manifest()

    index_content = f"""# Repository Documentation Index

## {manifest['repo_source']}

**Generated**: {manifest.get('processing_timestamp', 'Unknown')}
**Commit**: {manifest['commit_sha'][:8]}
**Files Documented**: {manifest['file_count']}
**Documentation Files Created**: {manifest['docs_created']}

---

## Quick Links

- [Comprehensive Book](comprehensive_book.md) - Complete repository documentation in one document
- [Global Keywords](keywords.md) - A-Z index of all keywords
- [Verification Report](verification_report.md) - Validation and quality checks

---

## Directory Structure

"""

    # Add root files
    root_files = [f for f in manifest['files'] if '/' not in f['path']]
    if root_files:
        index_content += "### Root Directory Files\n\n"
        for f in sorted(root_files, key=lambda x: x['path']):
            fname = f['path']
            index_content += f"- [{fname}]({fname}_docs.md)\n"
        index_content += "\n"

    # Add all folders with hierarchy
    index_content += "### Project Directories\n\n"
    folders = sorted(manifest['folders'])

    for folder in folders:
        level = folder.count('/') + 1
        indent = "  " * level
        folder_name = Path(folder).name
        index_content += f"{indent}- [{folder_name}]({folder}/index.md)\n"

    index_content += """

---

## Navigation Guide

### By Category

- **Source Code**: See `src/` and `lightweight_charts/` directories
- **Tests**: See `test/` directory
- **Examples**: See `examples/` directory
- **Documentation**: See `docs/source/` directory

### By File Type

- **Python Files**: Look for `.py` extensions
- **TypeScript Files**: Look for `.ts` extensions
- **Configuration**: Look for `.json`, `.yaml`, `.config.js` files

---

## How to Use This Documentation

1. Start with the [Comprehensive Book](comprehensive_book.md) for a complete overview
2. Use the [Keywords Index](keywords.md) to find specific functions, classes, or terms
3. Navigate through directory indexes to explore specific modules
4. Each file has detailed documentation in `<filename>_docs.md`

---

## Metadata

- **Repository**: {manifest['repo_source']}
- **Fingerprint**: {manifest['repo_fingerprint'][:16]}...
- **Total Bytes**: {manifest['total_bytes']:,}
- **Documentation Bytes**: {manifest['bytes_written']:,}

"""

    with open('docs/index.md', 'w') as f:
        f.write(index_content)

    print(f"  Created index.md")
    return len(index_content)

def generate_comprehensive_book():
    """Generate comprehensive_book.md by stitching together all documentation"""
    print("Generating comprehensive book...")

    manifest = load_manifest()

    book_content = f"""# {manifest['repo_source']} - Comprehensive Documentation Book

**Generated**: {manifest.get('processing_timestamp', 'Unknown')}
**Commit SHA**: {manifest['commit_sha']}

---

## Table of Contents

1. [Introduction](#introduction)
2. [Repository Overview](#repository-overview)
3. [Directory Documentation](#directory-documentation)
4. [File Documentation](#file-documentation)
5. [Appendix](#appendix)

---

## Introduction

This comprehensive book contains complete documentation for the {manifest['repo_source']} repository.

**Statistics**:
- Total Files: {manifest['file_count']}
- Total Folders: {manifest['folder_count']}
- Total Size: {manifest['total_bytes']:,} bytes
- Documentation Files: {manifest['docs_created']}

---

## Repository Overview

{manifest['repo_source']} is a Python library for creating lightweight financial charts with a Python interface.

### Repository Structure

The repository is organized into several main directories:

"""

    # Add folder summaries
    for folder in sorted(manifest['folders'])[:20]:  # Limit for book size
        book_content += f"- **{folder}**: "

        # Read folder doc.md if exists
        doc_path = Path('docs') / folder / 'doc.md'
        if doc_path.exists():
            doc_content = read_file_safe(doc_path)
            # Extract overview
            overview_match = re.search(r'## Purpose\s+(.+?)(?=##|$)', doc_content, re.DOTALL)
            if overview_match:
                overview = overview_match.group(1).strip()[:200]
                book_content += overview + "\n"
            else:
                book_content += "Directory documentation available\n"
        else:
            book_content += "Part of the project structure\n"

    book_content += "\n---\n\n## Directory Documentation\n\n"

    # Include each folder's doc.md content
    for folder in sorted(manifest['folders'])[:15]:  # Limit to first 15 folders
        doc_path = Path('docs') / folder / 'doc.md'
        if doc_path.exists():
            book_content += f"### {folder}\n\n"
            doc_content = read_file_safe(doc_path)
            book_content += doc_content + "\n\n---\n\n"

    book_content += "## File Documentation\n\n"
    book_content += "### Summary of Key Files\n\n"

    # Add summaries of important files (not full content to keep book manageable)
    important_files = [
        'README.md',
        'setup.py',
        'package.json',
        'lightweight_charts/__init__.py',
        'lightweight_charts/chart.py',
        'src/index.ts'
    ]

    for filepath in important_files:
        file_info = next((f for f in manifest['files'] if f['path'] == filepath), None)
        if file_info:
            book_content += f"#### {filepath}\n\n"
            book_content += f"**Size**: {file_info['size']} bytes | **Type**: {file_info['type']}\n\n"

            # Try to read the _docs.md summary
            doc_path = Path('docs') / filepath / f"{Path(filepath).name}_docs.md"
            if not doc_path.exists():
                doc_path = Path('docs') / f"{filepath}_docs.md"

            if doc_path.exists():
                doc_content = read_file_safe(doc_path)
                # Extract overview section only
                overview_match = re.search(r'## Overview\s+(.+?)(?=##|$)', doc_content, re.DOTALL)
                if overview_match:
                    book_content += overview_match.group(1).strip()[:500] + "\n\n"

    book_content += """

---

## Appendix

### Full Documentation

For complete documentation of every file, see the individual `_docs.md` files in this documentation tree.

### Keywords

See [keywords.md](keywords.md) for a complete alphabetical index.

### Navigation

Return to [index.md](index.md) for the main navigation.

---

**End of Comprehensive Book**

"""

    with open('docs/comprehensive_book.md', 'w') as f:
        f.write(book_content)

    print(f"  Created comprehensive_book.md ({len(book_content):,} bytes)")
    return len(book_content)

def main():
    """Generate all global documentation"""
    total_bytes = 0

    total_bytes += generate_global_keywords()
    total_bytes += generate_global_index()
    total_bytes += generate_comprehensive_book()

    print(f"\nGlobal documentation complete!")
    print(f"  Total bytes written: {total_bytes:,}")

    # Update manifest
    manifest = load_manifest()
    manifest['bytes_written'] += total_bytes
    manifest['docs_created'] += 3

    with open('docs/manifest.json', 'w') as f:
        json.dump(manifest, f, indent=2)

    return {
        'bytes_written': total_bytes,
        'docs_created': 3
    }

if __name__ == '__main__':
    result = main()
    print(json.dumps(result, indent=2))
