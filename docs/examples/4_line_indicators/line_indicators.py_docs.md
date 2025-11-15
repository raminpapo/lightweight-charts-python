# line_indicators.py Documentation

## File Metadata
- **Path**: `examples/4_line_indicators/line_indicators.py`
- **Extension**: `.py`
- **Lines of Code**: 24
- **File Size**: 505 bytes

## Original Source

```py
import pandas as pd
from lightweight_charts import Chart


def calculate_sma(df, period: int = 50):
    return pd.DataFrame({
        'time': df['date'],
        f'SMA {period}': df['close'].rolling(window=period).mean()
    }).dropna()


if __name__ == '__main__':
    chart = Chart()
    chart.legend(visible=True)

    df = pd.read_csv('ohlcv.csv')
    chart.set(df)

    line = chart.create_line('SMA 50')
    sma_data = calculate_sma(df, period=50)
    line.set(sma_data)

    chart.show(block=True)

```

## Overview

This file is located at `examples/4_line_indicators/line_indicators.py` and contains 24 lines of code.

## Python Code Analysis

### Functions

- **calculate_sma**(df, period: int = 50): Function implementation

### Dependencies

- pandas as pd
- Chart


## Related Files

This file is part of the repository structure. Related files may be found in the same directory or referenced in the code above.

## Tests

To test this file, refer to the repository's test suite in the `test/` directory.

## Performance & Security Notes

- Always review code for potential security vulnerabilities
- Ensure proper error handling is implemented
- Follow best practices for the language/framework being used
