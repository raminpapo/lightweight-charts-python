# test_toolbox.py

**File Path:** `test/test_toolbox.py`

**File Size:** 1,258 bytes
**Lines of Code:** 43
**Language:** python

---

## File Metadata

- **Relative Path:** `test/test_toolbox.py`
- **File Type:** .py
- **Size:** 1,258 bytes
- **Total Lines:** 43
- **Programming Language:** python

## Quick Summary

This file is part of the lightweight-charts-python repository.
 It defines 1 class(es).


## Original Source Code

```python

import unittest
import pandas as pd

from lightweight_charts import Chart
from util import BARS, Tester

from time import sleep


class TestToolBox(Tester):
    def test_create_horizontal_line(self):
        self.chart.set(BARS)
        horz_line = self.chart.horizontal_line(200, width=4)
        self.chart.show()
        result = self.chart.win.run_script_and_get(f"{horz_line.id}._options");
        self.assertTrue(result)
        self.chart.exit()

    def test_create_trend_line(self):
        self.chart.set(BARS)
        horz_line = self.chart.trend_line(BARS.iloc[-10]['date'], 180, BARS.iloc[-3]['date'], 190)
        self.chart.show()
        result = self.chart.win.run_script_and_get(f"{horz_line.id}._options");
        self.assertTrue(result)
        self.chart.exit()

    def test_create_box(self):
        self.chart.set(BARS)
        horz_line = self.chart.box(BARS.iloc[-10]['date'], 180, BARS.iloc[-3]['date'], 190)
        self.chart.show()
        result = self.chart.win.run_script_and_get(f"{horz_line.id}._options");
        self.assertTrue(result)
        self.chart.exit()

    def test_create_vertical_line(self):
        ...

    def test_create_vertical_span(self):
        ...


if __name__ == '__main__':
    unittest.main()

```

## High-Level Overview

### Classes (1)

- **`TestToolBox`** (line 10)

### Imports (5)

- `import unittest`
- `import pandas as pd`
- `from lightweight_charts import Chart`
- `from util import BARS, Tester`
- `from time import sleep`

## Detailed Walkthrough

### Code Structure

This file contains 43 lines of python.

#### Classes

##### TestToolBox (Line 10)

```python
    def test_create_horizontal_line(self):
        self.chart.set(BARS)
        horz_line = self.chart.horizontal_line(200, width=4)
        self.chart.show()
        result = self.chart.win.run_script_and_get(f"{horz_line.id}._options");
        self.assertTrue(result)
        self.chart.exit()
```

## Usage Examples

To use this file in your project:

```python
from test.test_toolbox import *
```

## Performance & Security Notes

### Performance

- File size: 1,258 bytes
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

pytest test/test_toolbox.py

```

---

*Documentation generated on 2025-11-18T21:53:49.016225*
