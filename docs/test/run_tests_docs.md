# run_tests.py

**File Path:** `test/run_tests.py`

**File Size:** 519 bytes
**Lines of Code:** 22
**Language:** python

---

## File Metadata

- **Relative Path:** `test/run_tests.py`
- **File Type:** .py
- **Size:** 519 bytes
- **Total Lines:** 22
- **Programming Language:** python

## Quick Summary

This file is part of the lightweight-charts-python repository.


## Original Source Code

```python

import unittest

from test_returns import TestReturns
from test_table import TestTable
from test_toolbox import TestToolBox
from test_topbar import TestTopBar
from test_chart import TestChart


TEST_CASES = [
    TestReturns,
    TestTable,
    TestToolBox,
    TestTopBar,
    TestChart,
]

if __name__ == '__main__':
    loader = unittest.TestLoader()
    cases = [loader.loadTestsFromTestCase(module) for module in TEST_CASES]
    suite = unittest.TestSuite(cases)
    unittest.TextTestRunner(verbosity=2).run(suite)

```

## High-Level Overview

### Imports (6)

- `import unittest`
- `from test_returns import TestReturns`
- `from test_table import TestTable`
- `from test_toolbox import TestToolBox`
- `from test_topbar import TestTopBar`
- `from test_chart import TestChart`

## Detailed Walkthrough

### Code Structure

This file contains 22 lines of python.
## Usage Examples

To use this file in your project:

```python
from test.run_tests import *
```

## Performance & Security Notes

### Performance

- File size: 519 bytes
- Complexity: 0 functions, 0 classes

### Security

- **Recommendation:** Review this file for potential security vulnerabilities
- No obvious security concerns detected (basic scan)

## Related Files

*To be populated during folder indexing phase*

## Testing

This file is a test file.

**How to run:**

```bash

pytest test/run_tests.py

```

---

*Documentation generated on 2025-11-18T21:53:49.010803*
