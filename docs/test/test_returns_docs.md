# test_returns.py

**File Path:** `test/test_returns.py`

**File Size:** 1,311 bytes
**Lines of Code:** 41
**Language:** python

---

## File Metadata

- **Relative Path:** `test/test_returns.py`
- **File Type:** .py
- **Size:** 1,311 bytes
- **Total Lines:** 41
- **Programming Language:** python

## Quick Summary

This file is part of the lightweight-charts-python repository.
 It defines 1 class(es).


## Original Source Code

```python

import unittest
import pandas as pd
from lightweight_charts import Chart
import asyncio

from util import BARS, Tester



class TestReturns(Tester):
    def test_screenshot_returns_value(self):
        self.chart.set(BARS)
        self.chart.show()
        screenshot_data = self.chart.screenshot()
        self.assertIsNotNone(screenshot_data)

    def test_save_drawings(self):


        async def main():
            asyncio.create_task(self.chart.show_async());

            await asyncio.sleep(2)
            self.chart.toolbox.drawings.clear() # clear drawings in python
            self.assertTrue(len(self.chart.toolbox.drawings) == 0)
            self.chart.run_script(f'{self.chart.id}.toolBox.saveDrawings();')
            await asyncio.sleep(1)  # resave them, and assert they exist
            self.assertTrue(len(self.chart.toolbox.drawings) > 0)
            self.chart.exit()

        self.chart = Chart(toolbox=True, width=100, height=100)
        self.chart.set(BARS)
        self.chart.topbar.textbox('symbol', 'SYM', align='right')
        self.chart.toolbox.save_drawings_under(self.chart.topbar['symbol'])
        self.chart.toolbox.import_drawings("drawings.json")
        self.chart.toolbox.load_drawings("SYM")
        asyncio.run(main())


if __name__ == '__main__':
    unittest.main()

```

## High-Level Overview

### Classes (1)

- **`TestReturns`** (line 10)

### Imports (5)

- `import unittest`
- `import pandas as pd`
- `from lightweight_charts import Chart`
- `import asyncio`
- `from util import BARS, Tester`

## Detailed Walkthrough

### Code Structure

This file contains 41 lines of python.

#### Classes

##### TestReturns (Line 10)

```python
    def test_screenshot_returns_value(self):
        self.chart.set(BARS)
        self.chart.show()
        screenshot_data = self.chart.screenshot()
        self.assertIsNotNone(screenshot_data)
```

## Usage Examples

To use this file in your project:

```python
from test.test_returns import *
```

## Performance & Security Notes

### Performance

- File size: 1,311 bytes
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

pytest test/test_returns.py

```

---

*Documentation generated on 2025-11-18T21:53:49.013942*
