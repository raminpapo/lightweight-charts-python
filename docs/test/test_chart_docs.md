# test_chart.py

**File Path:** `test/test_chart.py`

**File Size:** 768 bytes
**Lines of Code:** 21
**Language:** python

---

## File Metadata

- **Relative Path:** `test/test_chart.py`
- **File Type:** .py
- **Size:** 768 bytes
- **Total Lines:** 21
- **Programming Language:** python

## Quick Summary

This file is part of the lightweight-charts-python repository.
 It defines 1 class(es).


## Original Source Code

```python

import unittest
import pandas as pd
from util import BARS, Tester
from lightweight_charts import Chart


class TestChart(Tester):
    def test_data_is_renamed(self):
        uppercase_df = pd.DataFrame(BARS.copy()).rename({'date': 'Date', 'open': 'OPEN', 'high': 'HIgh', 'low': 'Low', 'close': 'close', 'volUME': 'volume'})
        result = self.chart._df_datetime_format(uppercase_df)
        self.assertEqual(list(result.columns), list(BARS.rename(columns={'date': 'time'}).columns))

    def test_line_in_list(self):
        result0 = self.chart.create_line()
        result1 = self.chart.create_line()
        self.assertEqual(result0, self.chart.lines()[0])
        self.assertEqual(result1, self.chart.lines()[1])


if __name__ == '__main__':
    unittest.main()

```

## High-Level Overview

### Classes (1)

- **`TestChart`** (line 7)

### Imports (4)

- `import unittest`
- `import pandas as pd`
- `from util import BARS, Tester`
- `from lightweight_charts import Chart`

## Detailed Walkthrough

### Code Structure

This file contains 21 lines of python.

#### Classes

##### TestChart (Line 7)

```python
    def test_data_is_renamed(self):
        uppercase_df = pd.DataFrame(BARS.copy()).rename({'date': 'Date', 'open': 'OPEN', 'high': 'HIgh', 'low': 'Low', 'close': 'close', 'volUME': 'volume'})
        result = self.chart._df_datetime_format(uppercase_df)
        self.assertEqual(list(result.columns), list(BARS.rename(columns={'date': 'time'}).columns))
```

## Usage Examples

To use this file in your project:

```python
from test.test_chart import *
```

## Performance & Security Notes

### Performance

- File size: 768 bytes
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

pytest test/test_chart.py

```

---

*Documentation generated on 2025-11-18T21:53:49.007983*
