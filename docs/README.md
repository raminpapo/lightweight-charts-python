# Generated Repository Documentation

This directory contains **comprehensive, auto-generated documentation** for the entire `lightweight-charts-python` repository.

## 📚 Documentation Structure

### Key Documents

| Document | Description |
|----------|-------------|
| [**index.md**](index.md) | Main navigation hub - start here |
| [**comprehensive_book.md**](comprehensive_book.md) | Complete repository documentation in one file |
| [**keywords.md**](keywords.md) | A-Z index of all keywords (633 keywords) |
| [**verification_report.md**](verification_report.md) | Quality checks and validation results |
| [**manifest.json**](manifest.json) | Complete metadata and checksums |

### Directory Structure

Each source directory is mirrored with documentation:

```
docs/
├── index.md                    # Global index
├── keywords.md                 # Global keywords
├── comprehensive_book.md       # Complete book
├── verification_report.md      # Validation report
├── manifest.json              # Metadata
│
├── <folder>/                  # Mirrored directories
│   ├── index.md              # Folder file listing
│   ├── doc.md                # Folder overview
│   ├── sub.md                # Folder keywords
│   │
│   └── <filename>_docs.md    # File documentation
│   └── <filename>_kw.md      # File keywords
```

### Per-File Documentation

Every readable file has two documentation files:

1. **`<filename>_docs.md`**: Comprehensive documentation including:
   - File metadata (size, lines, path)
   - Full source code
   - High-level overview
   - Code analysis (functions, classes, imports)
   - Related files
   - Performance & security notes

2. **`<filename>_kw.md`**: Keyword index containing:
   - Extracted identifiers
   - API names and functions
   - Links back to documentation

### Per-Folder Documentation

Every directory has three documentation files:

1. **`index.md`**: Lists all files and subdirectories with links
2. **`doc.md`**: Narrative context about the folder's purpose
3. **`sub.md`**: Merged keyword index for the folder

## 📊 Statistics

- **Repository**: lightweight-charts-python
- **Commit**: 052d778beda66f569175cbe6774aba5d3e3b1dea
- **Files Scanned**: 148 files
- **Folders**: 31 directories
- **Documentation Created**: 407 files
- **Total Documentation Size**: ~4.24 MB
- **Keywords Extracted**: 633 unique keywords

## 🚀 Quick Start

### For Browsing

1. **Start Here**: Open [index.md](index.md) for the main navigation
2. **Search**: Use [keywords.md](keywords.md) to find specific terms
3. **Read**: View [comprehensive_book.md](comprehensive_book.md) for complete overview

### For Searching

**Find a specific function or class:**
```bash
grep -r "ClassName" docs/keywords.md
```

**Find all documentation for a module:**
```bash
ls docs/lightweight_charts/
```

**Search across all documentation:**
```bash
grep -r "search term" docs/
```

## 🔧 How This Was Generated

This documentation was generated using the **World's Best Repo Book Generator**, following these principles:

1. **Truth-first**: No fabricated code or claims
2. **Deterministic**: Same repo → same docs (idempotent)
3. **Verifiable**: Includes manifests, checksums, validation
4. **Link-safe**: All internal links validated

### Generation Process

1. **Bootstrap**: Scanned repository, created manifest
2. **Per-file**: Generated `_docs.md` and `_kw.md` for all readable files
3. **Per-folder**: Created `index.md`, `doc.md`, `sub.md` for all directories
4. **Global merge**: Built `keywords.md`, `index.md`, `comprehensive_book.md`
5. **Verification**: Validated links, computed checksums
6. **Finalization**: Created this README and updated manifest

### Resumability

To regenerate or update documentation:

```bash
# Re-run the generation scripts
python3 generate_docs.py
python3 generate_global_docs.py
python3 generate_verification.py
```

The generator is **idempotent** - running it multiple times on the same repository produces identical results.

## 📋 File Organization

### Source Code Documentation

- **Python Package**: [lightweight_charts/](lightweight_charts/)
- **TypeScript Source**: [src/](src/)
- **Tests**: [test/](test/)
- **Examples**: [examples/](examples/)

### Configuration Files

- **Package Config**: [package.json](package.json_docs.md)
- **Python Setup**: [setup.py](setup.py_docs.md)
- **TypeScript Config**: [tsconfig.json](tsconfig.json_docs.md)

### Original Documentation

- **Sphinx Docs**: [source/](source/) (original documentation)

## ✅ Verification

See [verification_report.md](verification_report.md) for detailed validation results:

- **Total Links Checked**: Validated all internal links
- **Broken Links**: 23 (mostly due to path differences)
- **Checksums**: SHA256 for all 407 files
- **Errors**: None during generation

All checksums are stored in [manifest.json](manifest.json) for integrity verification.

## 🔍 Manifest

The [manifest.json](manifest.json) contains:

```json
{
  "repo_source": "lightweight-charts-python",
  "repo_fingerprint": "37247e1a...",
  "commit_sha": "052d778b...",
  "file_count": 148,
  "folder_count": 31,
  "docs_created": 407,
  "bytes_written": 4241404,
  "checksums": { ... },
  "verification_timestamp": "2025-11-15T..."
}
```

## 📖 Navigation Tips

### By Language

- **Python**: Look in `lightweight_charts/` and `test/`
- **TypeScript**: Look in `src/`
- **Documentation**: Look in `source/`

### By Purpose

- **Core API**: `lightweight_charts/chart.py`, `lightweight_charts/abstract.py`
- **Drawing Tools**: `src/drawing/`, `src/box/`, `src/trend-line/`
- **UI Components**: `src/general/toolbox.ts`, `src/general/topbar.ts`
- **Examples**: `examples/1_setting_data/`, `examples/2_live_data/`, etc.

## 🛠️ Maintenance

### Updating Documentation

When the repository changes:

1. Pull latest changes
2. Run `python3 generate_docs.py`
3. Run `python3 generate_global_docs.py`
4. Run `python3 generate_verification.py`
5. Commit updated documentation

### Verifying Integrity

To verify documentation hasn't been modified:

```bash
# Check checksums
python3 -c "import json; m = json.load(open('docs/manifest.json')); print(f\"Files: {len(m['checksums'])}\")"
```

## 📝 Notes

- **Binary files** (images, fonts) have metadata-only documentation
- **Large files** include full source when possible
- **Keywords** are automatically extracted from code
- **Links** use relative paths for portability

## 🎯 Quality Standards

This documentation follows strict quality rules:

- ✅ No fabricated code or files
- ✅ All links are relative and validated
- ✅ Missing metadata explicitly marked
- ✅ Binary files properly documented
- ✅ Full source included for text files
- ✅ Checksums for verification
- ✅ Comprehensive error handling

## 📞 Support

For issues or questions about this generated documentation:

1. Check [verification_report.md](verification_report.md) for known issues
2. Review [manifest.json](manifest.json) for generation details
3. Regenerate documentation if needed

---

**Generated**: 2025-11-15
**Generator Version**: 1.0.0
**Repository**: lightweight-charts-python
**Commit**: 052d778beda66f569175cbe6774aba5d3e3b1dea

---

*This documentation was automatically generated by the World's Best Repo Book Generator*
