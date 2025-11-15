# live_data.py Documentation

## File Metadata
- **Path**: `examples/2_live_data/live_data.py`
- **Extension**: `.py`
- **Lines of Code**: 26
- **File Size**: 517 bytes

## Original Source

```py
import pandas as pd
from time import sleep
from lightweight_charts import Chart

if __name__ == '__main__':

    chart = Chart()

    df1 = pd.read_csv('ohlcv.csv')
    df2 = pd.read_csv('next_ohlcv.csv')

    chart.set(df1)

    chart.show()

    last_close = df1.iloc[-1]['close']

    for i, series in df2.iterrows():
        chart.update(series)

        if series['close'] > 20 and last_close < 20:
            chart.marker(text='The price crossed $20!')

        last_close = series['close']
        sleep(0.1)

```

## Overview

This file is located at `examples/2_live_data/live_data.py` and contains 26 lines of code.

## Python Code Analysis

### Dependencies

- pandas as pd
- sleep
- Chart


## Related Files

This file is part of the repository structure. Related files may be found in the same directory or referenced in the code above.

## Tests

To test this file, refer to the repository's test suite in the `test/` directory.

## Performance & Security Notes

- Always review code for potential security vulnerabilities
- Ensure proper error handling is implemented
- Follow best practices for the language/framework being used
