# test_returns.py Documentation

## File Metadata
- **Path**: `test/test_returns.py`
- **Extension**: `.py`
- **Lines of Code**: 41
- **File Size**: 1311 bytes

## Original Source

```py
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

## Overview

This file is located at `test/test_returns.py` and contains 41 lines of code.

## Python Code Analysis

### Classes

- **TestReturns**: Class defined in this file

### Functions

- **test_screenshot_returns_value**(self): Function implementation
- **test_save_drawings**(self): Function implementation
- **main**(): Function implementation

### Dependencies

- unittest
- pandas as pd
- Chart
- asyncio
- BARS, Tester


## Related Files

This file is part of the repository structure. Related files may be found in the same directory or referenced in the code above.

## Tests

To test this file, refer to the repository's test suite in the `test/` directory.

## Performance & Security Notes

- Always review code for potential security vulnerabilities
- Ensure proper error handling is implemented
- Follow best practices for the language/framework being used
