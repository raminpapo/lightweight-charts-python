# Keywords: repo_book_generator.py

**Source File:** `repo_book_generator.py`
**Total Keywords:** 44

---

## Keyword Index (A-Z)

### A

#### `all_files`

- **Occurrences:** 8
- **Context:** *...urn "binary"      def scan_repository(self):         """Scan all files and classify them"""         all_files = []          for root, dirs, files in os.walk(self.repo_path):             # Filter out ignored di...*
- **Link:** [View in docs](./repo_book_generator_docs.md)

### B

#### `binary_extensions`

- **Occurrences:** 2
- **Context:** *... self.ignore_patterns = {'.git', '__pycache__', 'node_modules', '.pyc', '.so', '.dll'}         self.binary_extensions = {             '.png', '.jpg', '.jpeg', '.gif', '.ico', '.svg', '.pdf', '.zip',             '.tar'...*
- **Link:** [View in docs](./repo_book_generator_docs.md)

#### `binary_files`

- **Occurrences:** 1
- **Context:** *...ns for further processing output = {     'text_files': generator.file_classifications['text'],     'binary_files': generator.file_classifications['binary'],     'large_files': generator.file_classifications['larg...*
- **Link:** [View in docs](./repo_book_generator_docs.md)

#### `bytes_written`

- **Occurrences:** 1
- **Context:** *...           "commit_sha": "",             "file_count": 0,             "docs_count": 0,             "bytes_written": 0,             "timestamp_start": datetime.now().isoformat(),             "timestamp_end": "",   ...*
- **Link:** [View in docs](./repo_book_generator_docs.md)

### C

#### `CamelCase`

- **Occurrences:** 1
- **Context:** *...', content):                 keywords.add(match.group(1))          # General identifier extraction (CamelCase, snake_case)         for match in re.finditer(r'\b([A-Z][a-z]+(?:[A-Z][a-z]+)+)\b', content):      ...*
- **Link:** [View in docs](./repo_book_generator_docs.md)

#### `classify_file`

- **Occurrences:** 2
- **Context:** *...atterns:             if pattern in parts:                 return True         return False      def classify_file(self, filepath):         """Classify file as text, binary, large, or ignored"""         if self.sho...*
- **Link:** [View in docs](./repo_book_generator_docs.md)

#### `commit_sha`

- **Occurrences:** 3
- **Context:** *... {             "repo_source": str(self.repo_path),             "repo_fingerprint": "",             "commit_sha": "",             "file_count": 0,             "docs_count": 0,             "bytes_written": 0,    ...*
- **Link:** [View in docs](./repo_book_generator_docs.md)

#### `compute_fingerprint`

- **Occurrences:** 2
- **Context:** *...th)).read().strip()             return result         except:             return "unknown"      def compute_fingerprint(self, file_list):         """Compute repository fingerprint from file list"""         hasher = hash...*
- **Link:** [View in docs](./repo_book_generator_docs.md)

### D

#### `docs_count`

- **Occurrences:** 1
- **Context:** *...    "repo_fingerprint": "",             "commit_sha": "",             "file_count": 0,             "docs_count": 0,             "bytes_written": 0,             "timestamp_start": datetime.now().isoformat(),    ...*
- **Link:** [View in docs](./repo_book_generator_docs.md)

#### `docs_path`

- **Occurrences:** 5
- **Context:** *...ollections import defaultdict import re  class RepoBookGenerator:     def __init__(self, repo_path, docs_path):         self.repo_path = Path(repo_path)         self.docs_path = Path(docs_path)         self.ma...*
- **Link:** [View in docs](./repo_book_generator_docs.md)

### E

#### `extract_keywords_from_code`

- **Occurrences:** 1
- **Context:** *...nifest['repo_fingerprint'] = self.compute_fingerprint(all_files)          return all_files      def extract_keywords_from_code(self, content, filepath):         """Extract keywords from source code"""         keywords = set() ...*
- **Link:** [View in docs](./repo_book_generator_docs.md)

### F

#### `file_classifications`

- **Occurrences:** 11
- **Context:** *..._version": "1.0.0",             "files_map": {},             "checksums": {}         }         self.file_classifications = {             "text": [],             "binary": [],             "large": [],             "ignored...*
- **Link:** [View in docs](./repo_book_generator_docs.md)

#### `file_count`

- **Occurrences:** 2
- **Context:** *...str(self.repo_path),             "repo_fingerprint": "",             "commit_sha": "",             "file_count": 0,             "docs_count": 0,             "bytes_written": 0,             "timestamp_start": da...*
- **Link:** [View in docs](./repo_book_generator_docs.md)

#### `file_list`

- **Occurrences:** 2
- **Context:** *...      return result         except:             return "unknown"      def compute_fingerprint(self, file_list):         """Compute repository fingerprint from file list"""         hasher = hashlib.sha256()    ...*
- **Link:** [View in docs](./repo_book_generator_docs.md)

#### `files_map`

- **Occurrences:** 2
- **Context:** *...soformat(),             "timestamp_end": "",             "generator_version": "1.0.0",             "files_map": {},             "checksums": {}         }         self.file_classifications = {             "text...*
- **Link:** [View in docs](./repo_book_generator_docs.md)

### G

#### `generator_version`

- **Occurrences:** 1
- **Context:** *...       "timestamp_start": datetime.now().isoformat(),             "timestamp_end": "",             "generator_version": "1.0.0",             "files_map": {},             "checksums": {}         }         self.file_cla...*
- **Link:** [View in docs](./repo_book_generator_docs.md)

#### `get_commit_sha`

- **Occurrences:** 2
- **Context:** *...3', '.wav',             '.avi', '.mov', '.pyc', '.pyo', '.pyd', '.db', '.sqlite'         }      def get_commit_sha(self):         """Get current git commit SHA"""         try:             result = os.popen('git -C ...*
- **Link:** [View in docs](./repo_book_generator_docs.md)

### H

#### `HEAD`

- **Occurrences:** 1
- **Context:** *...   """Get current git commit SHA"""         try:             result = os.popen('git -C {} rev-parse HEAD'.format(self.repo_path)).read().strip()             return result         except:             retur...*
- **Link:** [View in docs](./repo_book_generator_docs.md)

### I

#### `ignore_patterns`

- **Occurrences:** 2
- **Context:** *..., '.sass', '.less', '.dockerfile', '.lock'         }          # Binary/ignore patterns         self.ignore_patterns = {'.git', '__pycache__', 'node_modules', '.pyc', '.so', '.dll'}         self.binary_extensions = {...*
- **Link:** [View in docs](./repo_book_generator_docs.md)

### J

#### `JSON`

- **Occurrences:** 1
- **Context:** *...json.dump(self.progress_log, f, indent=2)      def save_manifest(self):         """Save manifest to JSON file"""         self.manifest['timestamp_end'] = datetime.now().isoformat()         manifest_path =...*
- **Link:** [View in docs](./repo_book_generator_docs.md)

#### `JavaScript`

- **Occurrences:** 1
- **Context:** *...er(r'(?:from|import)\s+([\w.]+)', content):                 keywords.add(match.group(1))          # JavaScript/TypeScript keyword extraction         elif ext in {'.js', '.ts', '.jsx', '.tsx'}:             # Fun...*
- **Link:** [View in docs](./repo_book_generator_docs.md)

### K

#### `keywords_global`

- **Occurrences:** 1
- **Context:** *...       "large": [],             "ignored": []         }         self.progress_log = []         self.keywords_global = defaultdict(list)          # File extensions for text files         self.text_extensions = {     ...*
- **Link:** [View in docs](./repo_book_generator_docs.md)

### L

#### `LICENSE`

- **Occurrences:** 1
- **Context:** *...html', '.css', '.sh', '.bash', '.xml',             '.rst', '.gitignore', '.env', '.editorconfig', '.LICENSE', '.rst',             '.tex', '.bib', '.c', '.cpp', '.h', '.hpp', '.java', '.go', '.rs',           ...*
- **Link:** [View in docs](./repo_book_generator_docs.md)

#### `large_files`

- **Occurrences:** 1
- **Context:** *...or.file_classifications['text'],     'binary_files': generator.file_classifications['binary'],     'large_files': generator.file_classifications['large'],     'total_files': len(all_files) }  with open('/tmp/fil...*
- **Link:** [View in docs](./repo_book_generator_docs.md)

### M

#### `manifest_path`

- **Occurrences:** 5
- **Context:** *...anifest to JSON file"""         self.manifest['timestamp_end'] = datetime.now().isoformat()         manifest_path = self.docs_path / 'manifest.json'         with open(manifest_path, 'w') as f:             json.dum...*
- **Link:** [View in docs](./repo_book_generator_docs.md)

### N

#### `node_modules`

- **Occurrences:** 1
- **Context:** *...        }          # Binary/ignore patterns         self.ignore_patterns = {'.git', '__pycache__', 'node_modules', '.pyc', '.so', '.dll'}         self.binary_extensions = {             '.png', '.jpg', '.jpeg', '....*
- **Link:** [View in docs](./repo_book_generator_docs.md)

### P

#### `progress_log`

- **Occurrences:** 2
- **Context:** *...            "binary": [],             "large": [],             "ignored": []         }         self.progress_log = []         self.keywords_global = defaultdict(list)          # File extensions for text files    ...*
- **Link:** [View in docs](./repo_book_generator_docs.md)

### R

#### `RepoBookGenerator`

- **Occurrences:** 2
- **Context:** *...hlib import Path from datetime import datetime from collections import defaultdict import re  class RepoBookGenerator:     def __init__(self, repo_path, docs_path):         self.repo_path = Path(repo_path)         sel...*
- **Link:** [View in docs](./repo_book_generator_docs.md)

#### `rel_path`

- **Occurrences:** 6
- **Context:** *...             for file in files:                 filepath = os.path.join(root, file)                 rel_path = os.path.relpath(filepath, self.repo_path)                  # Skip if in docs directory (our outpu...*
- **Link:** [View in docs](./repo_book_generator_docs.md)

#### `repo_fingerprint`

- **Occurrences:** 3
- **Context:** *...h(docs_path)         self.manifest = {             "repo_source": str(self.repo_path),             "repo_fingerprint": "",             "commit_sha": "",             "file_count": 0,             "docs_count": 0,      ...*
- **Link:** [View in docs](./repo_book_generator_docs.md)

#### `repo_path`

- **Occurrences:** 7
- **Context:** *...time from collections import defaultdict import re  class RepoBookGenerator:     def __init__(self, repo_path, docs_path):         self.repo_path = Path(repo_path)         self.docs_path = Path(docs_path)     ...*
- **Link:** [View in docs](./repo_book_generator_docs.md)

#### `repo_source`

- **Occurrences:** 1
- **Context:** *...h = Path(repo_path)         self.docs_path = Path(docs_path)         self.manifest = {             "repo_source": str(self.repo_path),             "repo_fingerprint": "",             "commit_sha": "",           ...*
- **Link:** [View in docs](./repo_book_generator_docs.md)

### S

#### `SHA`

- **Occurrences:** 2
- **Context:** *...'.pyd', '.db', '.sqlite'         }      def get_commit_sha(self):         """Get current git commit SHA"""         try:             result = os.popen('git -C {} rev-parse HEAD'.format(self.repo_path)).re...*
- **Link:** [View in docs](./repo_book_generator_docs.md)

#### `save_manifest`

- **Occurrences:** 2
- **Context:** *...s_path / '.progress.log', 'w') as f:             json.dump(self.progress_log, f, indent=2)      def save_manifest(self):         """Save manifest to JSON file"""         self.manifest['timestamp_end'] = datetime.n...*
- **Link:** [View in docs](./repo_book_generator_docs.md)

#### `save_progress`

- **Occurrences:** 1
- **Context:** *...oup(1)) > 3:                 keywords.add(match.group(1))          return sorted(keywords)      def save_progress(self):         """Save progress to log file"""         with open(self.docs_path / '.progress.log', ...*
- **Link:** [View in docs](./repo_book_generator_docs.md)

#### `scan_repository`

- **Occurrences:** 2
- **Context:** *...return "text"             except:                 return "binary"          return "binary"      def scan_repository(self):         """Scan all files and classify them"""         all_files = []          for root, dir...*
- **Link:** [View in docs](./repo_book_generator_docs.md)

#### `should_ignore`

- **Occurrences:** 3
- **Context:** *...e_list):             hasher.update(str(f).encode())         return hasher.hexdigest()[:16]      def should_ignore(self, path):         """Check if path should be ignored"""         parts = Path(path).parts        ...*
- **Link:** [View in docs](./repo_book_generator_docs.md)

#### `snake_case`

- **Occurrences:** 1
- **Context:** *...:                 keywords.add(match.group(1))          # General identifier extraction (CamelCase, snake_case)         for match in re.finditer(r'\b([A-Z][a-z]+(?:[A-Z][a-z]+)+)\b', content):             keywo...*
- **Link:** [View in docs](./repo_book_generator_docs.md)

### T

#### `TypeScript`

- **Occurrences:** 1
- **Context:** *...m|import)\s+([\w.]+)', content):                 keywords.add(match.group(1))          # JavaScript/TypeScript keyword extraction         elif ext in {'.js', '.ts', '.jsx', '.tsx'}:             # Functions     ...*
- **Link:** [View in docs](./repo_book_generator_docs.md)

#### `text_extensions`

- **Occurrences:** 2
- **Context:** *...    self.keywords_global = defaultdict(list)          # File extensions for text files         self.text_extensions = {             '.py', '.md', '.txt', '.json', '.yaml', '.yml', '.toml', '.cfg',             '.ini'...*
- **Link:** [View in docs](./repo_book_generator_docs.md)

#### `text_files`

- **Occurrences:** 1
- **Context:** *...nifest saved to: {manifest_path}")  # Output classifications for further processing output = {     'text_files': generator.file_classifications['text'],     'binary_files': generator.file_classifications['binar...*
- **Link:** [View in docs](./repo_book_generator_docs.md)

#### `timestamp_end`

- **Occurrences:** 2
- **Context:** *...        "bytes_written": 0,             "timestamp_start": datetime.now().isoformat(),             "timestamp_end": "",             "generator_version": "1.0.0",             "files_map": {},             "checksums...*
- **Link:** [View in docs](./repo_book_generator_docs.md)

#### `timestamp_start`

- **Occurrences:** 1
- **Context:** *...         "file_count": 0,             "docs_count": 0,             "bytes_written": 0,             "timestamp_start": datetime.now().isoformat(),             "timestamp_end": "",             "generator_version": "1....*
- **Link:** [View in docs](./repo_book_generator_docs.md)

#### `total_files`

- **Occurrences:** 1
- **Context:** *...or.file_classifications['binary'],     'large_files': generator.file_classifications['large'],     'total_files': len(all_files) }  with open('/tmp/file_classifications.json', 'w') as f:     json.dump(output, f,...*
- **Link:** [View in docs](./repo_book_generator_docs.md)

---

*Keywords extracted on 2025-11-18T21:53:48.994331*
