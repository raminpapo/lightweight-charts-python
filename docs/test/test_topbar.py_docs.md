# test_topbar.py Documentation

## File Metadata
- **Path**: `test/test_topbar.py`
- **Extension**: `.py`
- **Lines of Code**: 23
- **File Size**: 822 bytes

## Original Source

```py
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

## Overview

This file is located at `test/test_topbar.py` and contains 23 lines of code.

## Python Code Analysis

### Classes

- **TestTopBar**: Class defined in this file

### Functions

- **test_switcher_fires_event**(self): Function implementation
- **test_button_fires_event**(self): Function implementation

### Dependencies

- unittest
- pandas as pd
- Chart
- Tester


## Related Files

This file is part of the repository structure. Related files may be found in the same directory or referenced in the code above.

## Tests

To test this file, refer to the repository's test suite in the `test/` directory.

## Performance & Security Notes

- Always review code for potential security vulnerabilities
- Ensure proper error handling is implemented
- Follow best practices for the language/framework being used
