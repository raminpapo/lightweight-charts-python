# tick_data.py Documentation

## File Metadata
- **Path**: `examples/3_tick_data/tick_data.py`
- **Extension**: `.py`
- **Lines of Code**: 21
- **File Size**: 359 bytes

## Original Source

```py
import pandas as pd
from time import sleep
from lightweight_charts import Chart

if __name__ == '__main__':

    df1 = pd.read_csv('ohlc.csv')

    # Columns: time | price
    df2 = pd.read_csv('ticks.csv')

    chart = Chart()

    chart.set(df1)

    chart.show()

    for i, tick in df2.iterrows():
        chart.update_from_tick(tick)
        sleep(0.03)

```

## Overview

This file is located at `examples/3_tick_data/tick_data.py` and contains 21 lines of code.

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
