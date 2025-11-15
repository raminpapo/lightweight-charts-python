# test_chart.py Documentation

## File Metadata
- **Path**: `test/test_chart.py`
- **Extension**: `.py`
- **Lines of Code**: 21
- **File Size**: 768 bytes

## Original Source

```py
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

## Overview

This file is located at `test/test_chart.py` and contains 21 lines of code.

## Python Code Analysis

### Classes

- **TestChart**: Class defined in this file

### Functions

- **test_data_is_renamed**(self): Function implementation
- **test_line_in_list**(self): Function implementation

### Dependencies

- unittest
- pandas as pd
- BARS, Tester
- Chart


## Related Files

This file is part of the repository structure. Related files may be found in the same directory or referenced in the code above.

## Tests

To test this file, refer to the repository's test suite in the `test/` directory.

## Performance & Security Notes

- Always review code for potential security vulnerabilities
- Ensure proper error handling is implemented
- Follow best practices for the language/framework being used
