#!/usr/bin/env python3
"""
Per-Folder Documentation Generator
Generates index.md, doc.md, and sub.md for each folder
"""

import os
import json
from pathlib import Path
from datetime import datetime
from collections import defaultdict

class FolderDocGenerator:
    def __init__(self, repo_path, docs_path):
        self.repo_path = Path(repo_path)
        self.docs_path = Path(docs_path)
        self.folders_processed = 0
        self.bytes_written = 0

        # Load file classifications
        with open('/tmp/file_classifications.json', 'r') as f:
            self.classifications = json.load(f)

        # Load global keywords
        with open('/tmp/keywords_global.json', 'r') as f:
            self.keywords_global = json.load(f)

    def get_all_folders(self):
        """Get all unique folder paths from text files"""
        folders = set()
        folders.add('')  # Root folder

        for filepath in self.classifications['text_files']:
            folder = str(Path(filepath).parent)
            if folder and folder != '.':
                folders.add(folder)
                # Add all parent folders
                parts = Path(folder).parts
                for i in range(1, len(parts)):
                    parent = str(Path(*parts[:i]))
                    folders.add(parent)

        return sorted(folders)

    def get_folder_contents(self, folder):
        """Get files and subfolders for a specific folder"""
        folder_path = folder if folder else ''

        files = []
        subfolders = set()

        # Get files in this folder
        for filepath in self.classifications['text_files']:
            file_parent = str(Path(filepath).parent)
            if file_parent == folder_path:
                files.append(filepath)

        # Get immediate subfolders
        all_folders = self.get_all_folders()
        for f in all_folders:
            if f and f != folder_path:
                parent = str(Path(f).parent)
                if parent == folder_path:
                    subfolders.add(f)

        return sorted(files), sorted(subfolders)

    def generate_index_md(self, folder):
        """Generate index.md for a folder"""
        files, subfolders = self.get_folder_contents(folder)

        index = []
        folder_name = Path(folder).name if folder else "Root"
        index.append(f"# Index: {folder_name}\n")
        index.append(f"**Folder Path:** `{folder or '/'}`\n")
        index.append("---\n")

        # Subfolders
        if subfolders:
            index.append(f"## Subfolders ({len(subfolders)})\n")
            for subfolder in subfolders:
                subfolder_name = Path(subfolder).name
                # Relative link to subfolder index
                rel_link = f"{subfolder_name}/index.md"
                index.append(f"- **[{subfolder_name}]({rel_link})**")
            index.append("")

        # Files
        if files:
            index.append(f"## Files ({len(files)})\n")
            for filepath in files:
                filename = Path(filepath).name
                # Link to _docs.md file
                docs_link = f"{Path(filepath).stem}_docs.md"
                kw_link = f"{Path(filepath).stem}_kw.md"
                index.append(f"- **{filename}**")
                index.append(f"  - [Documentation]({docs_link})")
                index.append(f"  - [Keywords]({kw_link})")
            index.append("")

        # Navigation
        index.append("## Navigation\n")
        if folder:
            parent = str(Path(folder).parent)
            if parent and parent != '.':
                index.append(f"- [⬆️ Parent Folder](../index.md)")
            else:
                index.append(f"- [⬆️ Root](../index.md)")
        index.append("- [📚 Documentation Overview](../../index.md)" if folder else "- [📚 Documentation Overview](./index.md)")
        index.append("- [🔍 Global Keywords](../../keywords.md)" if folder else "- [🔍 Global Keywords](./keywords.md)")
        index.append("")

        index.append("---\n")
        index.append(f"*Index generated on {datetime.now().isoformat()}*\n")

        return '\n'.join(index)

    def generate_doc_md(self, folder):
        """Generate doc.md with narrative description"""
        files, subfolders = self.get_folder_contents(folder)

        doc = []
        folder_name = Path(folder).name if folder else "Root"
        doc.append(f"# Documentation: {folder_name}\n")
        doc.append(f"**Folder Path:** `{folder or '/'}`\n")
        doc.append("---\n")

        # Overview
        doc.append("## Overview\n")

        if not folder:
            doc.append("This is the root directory of the **lightweight-charts-python** repository.")
            doc.append("This project provides Python bindings for the TradingView Lightweight Charts library.\n")
        else:
            # Infer purpose from folder name
            folder_descriptions = {
                'examples': "Contains example scripts demonstrating how to use the lightweight-charts-python library.",
                'test': "Contains test files for validating the functionality of the library.",
                'src': "Contains TypeScript/JavaScript source code for the frontend components.",
                'lightweight_charts': "Core Python package containing the main library code.",
                '.github': "GitHub-specific configuration files including issue templates and funding information.",
                'docs': "Documentation files for the project (source files, not the generated book).",
            }

            folder_base = Path(folder).parts[0] if Path(folder).parts else folder

            if folder_base in folder_descriptions:
                doc.append(folder_descriptions[folder_base])
            else:
                doc.append(f"This folder contains {len(files)} file(s) and {len(subfolders)} subfolder(s).")

            doc.append("")

        # Contents summary
        doc.append("## Contents Summary\n")
        doc.append(f"- **Files:** {len(files)}")
        doc.append(f"- **Subfolders:** {len(subfolders)}\n")

        # File breakdown
        if files:
            # Count by extension
            extensions = defaultdict(int)
            for f in files:
                ext = Path(f).suffix or 'no extension'
                extensions[ext] += 1

            doc.append("### File Types\n")
            for ext, count in sorted(extensions.items()):
                doc.append(f"- **{ext}**: {count} file(s)")
            doc.append("")

        # Purpose and role
        doc.append("## Purpose & Role\n")

        if not folder:
            doc.append("The root directory serves as the entry point to the repository, containing:")
            doc.append("- Configuration files (package.json, setup.py, etc.)")
            doc.append("- Documentation and README")
            doc.append("- Build scripts and tooling configuration")
        elif 'example' in folder.lower():
            doc.append("This folder demonstrates practical usage patterns and features of the library.")
            doc.append("Each example is self-contained and can be run independently.")
        elif 'test' in folder.lower():
            doc.append("This folder contains automated tests ensuring code quality and functionality.")
            doc.append("Tests validate API contracts, edge cases, and expected behavior.")
        elif 'src' in folder.lower():
            doc.append("This folder contains source code for the project's frontend components.")
            doc.append("Code here is typically compiled/bundled for distribution.")
        else:
            doc.append(f"This folder plays a role in the overall architecture of the project.")

        doc.append("")

        # Relationships
        if subfolders:
            doc.append("## Subfolders\n")
            for subfolder in subfolders:
                subfolder_name = Path(subfolder).name
                doc.append(f"### {subfolder_name}\n")
                sub_files, sub_subfolders = self.get_folder_contents(subfolder)
                doc.append(f"Contains {len(sub_files)} file(s) and {len(sub_subfolders)} subfolder(s).\n")

        # Key files
        if files:
            doc.append("## Key Files\n")
            for filepath in files[:10]:  # Highlight first 10 files
                filename = Path(filepath).name
                doc.append(f"### {filename}\n")
                # Link to documentation
                docs_link = f"{Path(filepath).stem}_docs.md"
                doc.append(f"[View Documentation]({docs_link})\n")

            if len(files) > 10:
                doc.append(f"*...and {len(files) - 10} more files. See [index.md](./index.md) for complete list.*\n")

        doc.append("---\n")
        doc.append(f"*Documentation generated on {datetime.now().isoformat()}*\n")

        return '\n'.join(doc)

    def generate_sub_md(self, folder):
        """Generate sub.md with merged keywords from descendant files"""
        # Get all files in this folder and descendants
        descendant_files = []

        for filepath in self.classifications['text_files']:
            if not folder:
                # Root - include everything
                descendant_files.append(filepath)
            elif filepath.startswith(folder + '/') or filepath.startswith(folder + '\\'):
                descendant_files.append(filepath)

        # Collect keywords from all descendant files
        folder_keywords = defaultdict(list)

        for filepath in descendant_files:
            if filepath in self.keywords_global:
                for keyword in self.keywords_global[filepath]:
                    folder_keywords[keyword].append(filepath)

        # Build sub.md
        sub = []
        folder_name = Path(folder).name if folder else "Root"
        sub.append(f"# Merged Keywords: {folder_name}\n")
        sub.append(f"**Folder Path:** `{folder or '/'}`")
        sub.append(f"**Total Unique Keywords:** {len(folder_keywords)}")
        sub.append(f"**Files Indexed:** {len(descendant_files)}\n")
        sub.append("---\n")

        sub.append("## Keyword Index (A-Z)\n")

        # Group alphabetically
        keyword_groups = defaultdict(list)
        for kw in sorted(folder_keywords.keys()):
            first_letter = kw[0].upper() if kw else '?'
            keyword_groups[first_letter].append(kw)

        for letter in sorted(keyword_groups.keys()):
            sub.append(f"### {letter}\n")
            for kw in sorted(keyword_groups[letter]):
                files_with_kw = folder_keywords[kw]
                sub.append(f"#### `{kw}`\n")
                sub.append(f"**Found in {len(files_with_kw)} file(s):**")

                for filepath in files_with_kw[:5]:  # Show first 5
                    rel_to_folder = filepath
                    if folder and filepath.startswith(folder + '/'):
                        rel_to_folder = filepath[len(folder)+1:]
                    docs_link = f"{Path(filepath).stem}_docs.md"
                    # Calculate relative path
                    if folder:
                        # Link relative to current folder
                        depth = len(Path(folder).parts)
                        if filepath.startswith(folder + '/'):
                            # Same folder or descendant
                            rel_parts = Path(filepath[len(folder)+1:]).parts
                            if len(rel_parts) > 1:
                                docs_link = '/'.join(rel_parts[:-1]) + '/' + f"{Path(filepath).stem}_docs.md"
                            else:
                                docs_link = f"{Path(filepath).stem}_docs.md"
                        else:
                            # Different branch - use absolute from docs root
                            docs_link = '../../' * (depth + 1) + filepath.replace(Path(filepath).name, '') + f"{Path(filepath).stem}_docs.md"

                    sub.append(f"- [{Path(filepath).name}]({docs_link})")

                if len(files_with_kw) > 5:
                    sub.append(f"- *...and {len(files_with_kw) - 5} more*")
                sub.append("")

        sub.append("---\n")
        sub.append(f"*Keywords merged on {datetime.now().isoformat()}*\n")

        return '\n'.join(sub)

    def process_folder(self, folder):
        """Process a single folder and generate its documentation"""
        # Create folder in docs
        if folder:
            docs_folder = self.docs_path / folder
        else:
            docs_folder = self.docs_path

        docs_folder.mkdir(parents=True, exist_ok=True)

        try:
            # Generate index.md
            index_content = self.generate_index_md(folder)
            index_path = docs_folder / 'index.md'
            with open(index_path, 'w', encoding='utf-8') as f:
                f.write(index_content)
            self.bytes_written += len(index_content.encode('utf-8'))

            # Generate doc.md
            doc_content = self.generate_doc_md(folder)
            doc_path = docs_folder / 'doc.md'
            with open(doc_path, 'w', encoding='utf-8') as f:
                f.write(doc_content)
            self.bytes_written += len(doc_content.encode('utf-8'))

            # Generate sub.md
            sub_content = self.generate_sub_md(folder)
            sub_path = docs_folder / 'sub.md'
            with open(sub_path, 'w', encoding='utf-8') as f:
                f.write(sub_content)
            self.bytes_written += len(sub_content.encode('utf-8'))

            self.folders_processed += 1
            return True, None

        except Exception as e:
            return False, str(e)

# Main execution
if __name__ == '__main__':
    generator = FolderDocGenerator(
        '/home/user/lightweight-charts-python',
        '/home/user/lightweight-charts-python/docs'
    )

    folders = generator.get_all_folders()
    print(f"Processing {len(folders)} folders...")

    success_count = 0
    error_count = 0

    for i, folder in enumerate(folders, 1):
        folder_display = folder if folder else "/"
        print(f"[{i}/{len(folders)}] Processing: {folder_display}")

        success, error = generator.process_folder(folder)

        if success:
            success_count += 1
        else:
            error_count += 1
            print(f"  ERROR: {error}")

    print(f"\n=== Folder Documentation Complete ===")
    print(f"Folders processed: {len(folders)}")
    print(f"Success: {success_count}")
    print(f"Errors: {error_count}")
    print(f"Bytes written: {generator.bytes_written:,}")
    print(f"Total docs created: {success_count * 3}")
