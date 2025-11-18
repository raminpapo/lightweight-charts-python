# test_topbar.py

**File Path:** `test/test_topbar.py`

**File Size:** 822 bytes
**Lines of Code:** 23
**Language:** python

---

## File Metadata

- **Relative Path:** `test/test_topbar.py`
- **File Type:** .py
- **Size:** 822 bytes
- **Total Lines:** 23
- **Programming Language:** python

## Quick Summary

This file is part of the lightweight-charts-python repository.
 It defines 1 class(es).


## Original Source Code

```python

import unittest
import pandas as pd

from lightweight_charts import Chart
from util import Tester


class TestTopBar(Tester):
    def test_switcher_fires_event(self):
        self.chart.topbar.switcher('a', ('1', '2'), func=lambda c: (self.assertEqual(c.topbar['a'].value, '2'), c.exit()))
        self.chart.run_script(f'{self.chart.topbar["a"].id}.intervalElements[1].dispatchEvent(new Event("click"))')
        self.chart.show(block=True)

    def test_button_fires_event(self):
        self.chart.topbar.button('a', '1', func=lambda c: (self.assertEqual(c.topbar['a'].value, '2'), c.exit()))
        self.chart.topbar['a'].set('2')
        self.chart.run_script(f'{self.chart.topbar["a"].id}.elem.dispatchEvent(new Event("click"))')
        self.chart.show(block=True)


if __name__ == '__main__':
    unittest.main()


```

## High-Level Overview

### Classes (1)

- **`TestTopBar`** (line 8)

### Imports (4)

- `import unittest`
- `import pandas as pd`
- `from lightweight_charts import Chart`
- `from util import Tester`

## Detailed Walkthrough

### Code Structure

This file contains 23 lines of python.

#### Classes

##### TestTopBar (Line 8)

```python
    def test_switcher_fires_event(self):
        self.chart.topbar.switcher('a', ('1', '2'), func=lambda c: (self.assertEqual(c.topbar['a'].value, '2'), c.exit()))
        self.chart.run_script(f'{self.chart.topbar["a"].id}.intervalElements[1].dispatchEvent(new Event("click"))')
        self.chart.show(block=True)
```

## Usage Examples

To use this file in your project:

```python
from test.test_topbar import *
```

## Performance & Security Notes

### Performance

- File size: 822 bytes
- Complexity: 0 functions, 1 classes

### Security

- **Recommendation:** Review this file for potential security vulnerabilities
- No obvious security concerns detected (basic scan)

## Related Files

*To be populated during folder indexing phase*

## Testing

This file is a test file.

**How to run:**

```bash

pytest test/test_topbar.py

```

---

*Documentation generated on 2025-11-18T21:53:49.018089*
