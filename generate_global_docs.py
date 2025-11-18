#!/usr/bin/env python3
"""
Global Documentation Generator
Generates keywords.md, index.md, and comprehensive_book.md
"""

import os
import json
from pathlib import Path
from datetime import datetime
from collections import defaultdict

class GlobalDocGenerator:
    def __init__(self, repo_path, docs_path):
        self.repo_path = Path(repo_path)
        self.docs_path = Path(docs_path)

        # Load data
        with open('/tmp/file_classifications.json', 'r') as f:
            self.classifications = json.load(f)

        with open('/tmp/keywords_global.json', 'r') as f:
            self.keywords_global = json.load(f)

        with open(self.docs_path / 'manifest.json', 'r') as f:
            self.manifest = json.load(f)

    def get_all_folders(self):
        """Get all unique folder paths"""
        folders = set()
        folders.add('')  # Root

        for filepath in self.classifications['text_files']:
            folder = str(Path(filepath).parent)
            if folder and folder != '.':
                folders.add(folder)
                parts = Path(folder).parts
                for i in range(1, len(parts)):
                    parent = str(Path(*parts[:i]))
                    folders.add(parent)

        return sorted(folders)

    def generate_keywords_md(self):
        """Generate global keywords.md"""
        kw = []
        kw.append("# Global Keyword Index\n")
        kw.append("**Repository:** lightweight-charts-python")
        kw.append(f"**Total Keywords:** {len(self.keywords_global)}")
        kw.append(f"**Generated:** {datetime.now().isoformat()}\n")
        kw.append("---\n")

        kw.append("## About This Index\n")
        kw.append("This is a comprehensive, deduplicated index of all keywords, identifiers, ")
        kw.append("functions, classes, and significant terms found across the entire repository.\n")
        kw.append("Each keyword links to the files where it appears.\n")

        kw.append("## Keyword Index (A-Z)\n")

        # Group alphabetically
        keyword_groups = defaultdict(list)
        for keyword in sorted(self.keywords_global.keys()):
            first_letter = keyword[0].upper() if keyword else '?'
            keyword_groups[first_letter].append(keyword)

        for letter in sorted(keyword_groups.keys()):
            kw.append(f"### {letter}\n")

            for keyword in sorted(keyword_groups[letter]):
                files = self.keywords_global[keyword]
                kw.append(f"#### `{keyword}`\n")
                kw.append(f"**Found in {len(files)} file(s):**\n")

                for filepath in files[:10]:  # Show first 10
                    filename = Path(filepath).name
                    # Create link to _docs.md
                    folder = str(Path(filepath).parent)
                    if folder and folder != '.':
                        docs_link = f"{folder}/{Path(filepath).stem}_docs.md"
                    else:
                        docs_link = f"{Path(filepath).stem}_docs.md"

                    kw.append(f"- [{filename}]({docs_link})")

                if len(files) > 10:
                    kw.append(f"- *...and {len(files) - 10} more files*")

                kw.append("")

        kw.append("---\n")
        kw.append(f"*Global keyword index generated on {datetime.now().isoformat()}*\n")

        return '\n'.join(kw)

    def generate_index_md(self):
        """Generate global index.md"""
        idx = []
        idx.append("# Documentation Index\n")
        idx.append("## lightweight-charts-python Repository Documentation\n")
        idx.append(f"**Generated:** {datetime.now().isoformat()}")
        idx.append(f"**Repository Commit:** {self.manifest.get('commit_sha', 'unknown')}")
        idx.append(f"**Files Documented:** {self.manifest.get('file_count', 0)}\n")
        idx.append("---\n")

        idx.append("## Quick Navigation\n")
        idx.append("- [📖 Comprehensive Book](./comprehensive_book.md) - Complete repository documentation in book form")
        idx.append("- [🔍 Global Keywords](./keywords.md) - Searchable keyword index (A-Z)")
        idx.append("- [✅ Verification Report](./verification_report.md) - Quality checks and validation")
        idx.append("- [📋 Manifest](./manifest.json) - Repository metadata and checksums\n")

        idx.append("## Folder Structure\n")

        folders = self.get_all_folders()

        # Build tree structure
        idx.append("### Root Directory\n")
        idx.append("- [📁 Root Documentation](./doc.md)")
        idx.append("- [📑 Root Index](./index.md)")
        idx.append("- [🏷️ Root Keywords](./sub.md)\n")

        # Group folders by depth
        depth_groups = defaultdict(list)
        for folder in folders:
            if folder:
                depth = len(Path(folder).parts)
                depth_groups[depth].append(folder)

        # First level folders
        if 1 in depth_groups:
            idx.append("### Top-Level Folders\n")
            for folder in sorted(depth_groups[1]):
                folder_name = Path(folder).name
                idx.append(f"#### {folder_name}\n")
                idx.append(f"- [📁 Documentation](./{folder}/doc.md)")
                idx.append(f"- [📑 Index](./{folder}/index.md)")
                idx.append(f"- [🏷️ Keywords](./{folder}/sub.md)")

                # Show immediate subfolders
                if 2 in depth_groups:
                    subfolders = [f for f in depth_groups[2] if str(Path(f).parent) == folder]
                    if subfolders:
                        idx.append(f"  - **Subfolders:** {', '.join([Path(f).name for f in sorted(subfolders)])}")

                idx.append("")

        # Stats
        idx.append("## Repository Statistics\n")
        idx.append(f"- **Total Folders:** {len(folders)}")
        idx.append(f"- **Text Files:** {len(self.classifications['text_files'])}")
        idx.append(f"- **Binary Files:** {len(self.classifications['binary_files'])}")
        idx.append(f"- **Unique Keywords:** {len(self.keywords_global)}")
        idx.append(f"- **Documentation Files Created:** {self.manifest.get('docs_count', 0)}")
        idx.append(f"- **Total Bytes Written:** {self.manifest.get('bytes_written', 0):,}\n")

        idx.append("## How to Use This Documentation\n")
        idx.append("1. **Browse by folder:** Navigate through folder indices to explore the codebase structure")
        idx.append("2. **Search by keyword:** Use the keywords.md file to find specific terms and their locations")
        idx.append("3. **Read the book:** For a linear, comprehensive overview, see comprehensive_book.md")
        idx.append("4. **Verify completeness:** Check verification_report.md for any issues or missing documentation\n")

        idx.append("---\n")
        idx.append(f"*Index generated on {datetime.now().isoformat()}*\n")

        return '\n'.join(idx)

    def generate_comprehensive_book_md(self):
        """Generate comprehensive book from all content"""
        book = []

        book.append("# Comprehensive Repository Book\n")
        book.append("# lightweight-charts-python\n")
        book.append(f"**Generated:** {datetime.now().isoformat()}")
        book.append(f"**Repository Commit:** {self.manifest.get('commit_sha', 'unknown')}\n")
        book.append("---\n")

        # Table of contents
        book.append("## Table of Contents\n")
        book.append("1. [Introduction](#introduction)")
        book.append("2. [Repository Overview](#repository-overview)")
        book.append("3. [Folder Documentation](#folder-documentation)")
        book.append("4. [File Summaries](#file-summaries)")
        book.append("5. [Keyword Index](#keyword-index)")
        book.append("6. [Appendix](#appendix)\n")
        book.append("---\n")

        # Introduction
        book.append("## Introduction\n")
        book.append("This book provides comprehensive documentation for the **lightweight-charts-python** repository. ")
        book.append("It is automatically generated and includes detailed analysis of every file, folder, and code element.\n")

        book.append("### What is lightweight-charts-python?\n")
        book.append("A Python library providing bindings for TradingView's Lightweight Charts library, ")
        book.append("enabling beautiful, performant financial charts in Python applications.\n")

        book.append("### Book Structure\n")
        book.append("- **Repository Overview:** High-level statistics and structure")
        book.append("- **Folder Documentation:** Narrative descriptions of each folder's purpose")
        book.append("- **File Summaries:** Quick summaries of each file")
        book.append("- **Keyword Index:** Searchable index of all identifiers")
        book.append("- **Appendix:** Additional resources and metadata\n")

        book.append("---\n")

        # Repository Overview
        book.append("## Repository Overview\n")
        book.append(f"**Commit SHA:** `{self.manifest.get('commit_sha', 'unknown')}`")
        book.append(f"**Fingerprint:** `{self.manifest.get('repo_fingerprint', 'unknown')}`")
        book.append(f"**Total Files:** {self.manifest.get('file_count', 0)}")
        book.append(f"**Text Files:** {len(self.classifications['text_files'])}")
        book.append(f"**Binary Files:** {len(self.classifications['binary_files'])}\n")

        book.append("### Technology Stack\n")
        # Analyze file types
        extensions = defaultdict(int)
        for f in self.classifications['text_files']:
            ext = Path(f).suffix or 'no extension'
            extensions[ext] += 1

        book.append("| Language/Type | Files |")
        book.append("|--------------|-------|")
        for ext, count in sorted(extensions.items(), key=lambda x: -x[1])[:10]:
            book.append(f"| {ext} | {count} |")
        book.append("")

        # Folder Documentation
        book.append("---\n")
        book.append("## Folder Documentation\n")
        book.append("This section provides narrative descriptions of each folder in the repository.\n")

        folders = self.get_all_folders()
        for folder in folders:
            folder_name = Path(folder).name if folder else "Root"
            folder_path = folder if folder else "/"

            book.append(f"### {folder_path}\n")

            # Read the doc.md for this folder
            if folder:
                doc_path = self.docs_path / folder / 'doc.md'
            else:
                doc_path = self.docs_path / 'doc.md'

            if doc_path.exists():
                try:
                    with open(doc_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        # Extract just the overview and purpose sections
                        lines = content.split('\n')
                        in_relevant_section = False
                        for line in lines:
                            if line.startswith('## Overview') or line.startswith('## Purpose'):
                                in_relevant_section = True
                            elif line.startswith('##') and in_relevant_section:
                                break
                            elif in_relevant_section:
                                book.append(line)
                except:
                    book.append("*Documentation unavailable*")

            book.append("")

        # File Summaries
        book.append("---\n")
        book.append("## File Summaries\n")
        book.append("Quick summaries of each file in the repository.\n")

        for filepath in sorted(self.classifications['text_files'])[:50]:  # First 50 files
            filename = Path(filepath).name

            book.append(f"### {filepath}\n")

            # Read summary from _docs.md
            folder = str(Path(filepath).parent)
            if folder and folder != '.':
                docs_path = self.docs_path / folder / f"{Path(filepath).stem}_docs.md"
            else:
                docs_path = self.docs_path / f"{Path(filepath).stem}_docs.md"

            if docs_path.exists():
                try:
                    with open(docs_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        # Extract Quick Summary
                        if '## Quick Summary' in content:
                            parts = content.split('## Quick Summary')
                            if len(parts) > 1:
                                summary = parts[1].split('##')[0].strip()
                                book.append(summary[:500])  # First 500 chars
                except:
                    book.append("*Summary unavailable*")

            book.append("")

        if len(self.classifications['text_files']) > 50:
            book.append(f"*...and {len(self.classifications['text_files']) - 50} more files. See individual documentation for details.*\n")

        # Keyword Index (abbreviated in book)
        book.append("---\n")
        book.append("## Keyword Index\n")
        book.append("For the complete keyword index, see [keywords.md](./keywords.md).\n")
        book.append(f"**Total Keywords:** {len(self.keywords_global)}\n")

        # Show top 20 most common keywords
        keyword_counts = [(kw, len(files)) for kw, files in self.keywords_global.items()]
        keyword_counts.sort(key=lambda x: -x[1])

        book.append("### Most Common Keywords\n")
        book.append("| Keyword | Occurrences |")
        book.append("|---------|-------------|")
        for kw, count in keyword_counts[:20]:
            book.append(f"| `{kw}` | {count} |")
        book.append("")

        # Appendix
        book.append("---\n")
        book.append("## Appendix\n")
        book.append("### Generation Metadata\n")
        book.append(f"- **Generator Version:** {self.manifest.get('generator_version', '1.0.0')}")
        book.append(f"- **Generation Started:** {self.manifest.get('timestamp_start', 'unknown')}")
        book.append(f"- **Generation Completed:** {datetime.now().isoformat()}")
        book.append(f"- **Documentation Files Created:** {self.manifest.get('docs_count', 0)}")
        book.append(f"- **Total Bytes Written:** {self.manifest.get('bytes_written', 0):,}\n")

        book.append("### How to Navigate\n")
        book.append("- Use your text editor's search function to find specific terms")
        book.append("- Follow markdown links to detailed documentation")
        book.append("- Refer to the main index.md for structured navigation\n")

        book.append("---\n")
        book.append("**End of Comprehensive Book**\n")
        book.append(f"*Generated on {datetime.now().isoformat()}*\n")

        return '\n'.join(book)

    def save_all(self):
        """Generate and save all global documentation files"""
        results = {}

        # Generate keywords.md
        print("Generating keywords.md...")
        keywords_content = self.generate_keywords_md()
        keywords_path = self.docs_path / 'keywords.md'
        with open(keywords_path, 'w', encoding='utf-8') as f:
            f.write(keywords_content)
        results['keywords_md'] = {
            'path': str(keywords_path),
            'size': len(keywords_content.encode('utf-8'))
        }
        print(f"  Created: {keywords_path} ({len(keywords_content.encode('utf-8')):,} bytes)")

        # Generate main index.md
        print("Generating main index.md...")
        index_content = self.generate_index_md()
        index_path = self.docs_path / 'index.md'
        # Rename existing if from folder generation
        if index_path.exists():
            os.rename(index_path, self.docs_path / 'index_folder.md')
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(index_content)
        results['index_md'] = {
            'path': str(index_path),
            'size': len(index_content.encode('utf-8'))
        }
        print(f"  Created: {index_path} ({len(index_content.encode('utf-8')):,} bytes)")

        # Generate comprehensive_book.md
        print("Generating comprehensive_book.md...")
        book_content = self.generate_comprehensive_book_md()
        book_path = self.docs_path / 'comprehensive_book.md'
        with open(book_path, 'w', encoding='utf-8') as f:
            f.write(book_content)
        results['book_md'] = {
            'path': str(book_path),
            'size': len(book_content.encode('utf-8'))
        }
        print(f"  Created: {book_path} ({len(book_content.encode('utf-8')):,} bytes)")

        return results

# Main execution
if __name__ == '__main__':
    generator = GlobalDocGenerator(
        '/home/user/lightweight-charts-python',
        '/home/user/lightweight-charts-python/docs'
    )

    results = generator.save_all()

    print(f"\n=== Global Documentation Complete ===")
    total_bytes = sum(r['size'] for r in results.values())
    print(f"Files created: {len(results)}")
    print(f"Total bytes: {total_bytes:,}")
    for name, info in results.items():
        print(f"  - {name}: {info['size']:,} bytes")
