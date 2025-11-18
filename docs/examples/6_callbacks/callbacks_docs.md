# callbacks.py

**File Path:** `examples/6_callbacks/callbacks.py`

**File Size:** 1,329 bytes
**Lines of Code:** 47
**Language:** python

---

## File Metadata

- **Relative Path:** `examples/6_callbacks/callbacks.py`
- **File Type:** .py
- **Size:** 1,329 bytes
- **Total Lines:** 47
- **Programming Language:** python

## Quick Summary

This file is part of the lightweight-charts-python repository.
 It contains 4 function(s).


## Original Source Code

```python

import pandas as pd
from lightweight_charts import Chart


def get_bar_data(symbol, timeframe):
    if symbol not in ('AAPL', 'GOOGL', 'TSLA'):
        print(f'No data for "{symbol}"')
        return pd.DataFrame()
    return pd.read_csv(f'bar_data/{symbol}_{timeframe}.csv')


def on_search(chart, searched_string):  # Called when the user searches.
    new_data = get_bar_data(searched_string, chart.topbar['timeframe'].value)
    if new_data.empty:
        return
    chart.topbar['symbol'].set(searched_string)
    chart.set(new_data)


def on_timeframe_selection(chart):  # Called when the user changes the timeframe.
    new_data = get_bar_data(chart.topbar['symbol'].value, chart.topbar['timeframe'].value)
    if new_data.empty:
        return
    chart.set(new_data, True)


def on_horizontal_line_move(chart, line):
    print(f'Horizontal line moved to: {line.price}')


if __name__ == '__main__':
    chart = Chart(toolbox=True)
    chart.legend(True)

    chart.events.search += on_search

    chart.topbar.textbox('symbol', 'TSLA')
    chart.topbar.switcher('timeframe', ('1min', '5min', '30min'), default='5min',
                          func=on_timeframe_selection)

    df = get_bar_data('TSLA', '5min')
    chart.set(df)

    chart.horizontal_line(200, func=on_horizontal_line_move)

    chart.show(block=True)


```

## High-Level Overview

### Functions (4)

- **`get_bar_data(symbol, timeframe)`** (line 5)
- **`on_search(chart, searched_string)`** (line 12)
- **`on_timeframe_selection(chart)`** (line 20)
- **`on_horizontal_line_move(chart, line)`** (line 27)

### Imports (2)

- `import pandas as pd`
- `from lightweight_charts import Chart`

## Detailed Walkthrough

### Code Structure

This file contains 47 lines of python.

#### Functions

##### get_bar_data (Line 5)

**Parameters:** `symbol, timeframe`

##### on_search (Line 12)

**Parameters:** `chart, searched_string`

##### on_timeframe_selection (Line 20)

**Parameters:** `chart`

##### on_horizontal_line_move (Line 27)

**Parameters:** `chart, line`

## Usage Examples

To use this file in your project:

```python
from examples.6_callbacks.callbacks import *
```

## Performance & Security Notes

### Performance

- File size: 1,329 bytes
- Complexity: 4 functions, 0 classes

### Security

- **Recommendation:** Review this file for potential security vulnerabilities
- No obvious security concerns detected (basic scan)

## Related Files

*To be populated during folder indexing phase*

## Testing

Tests for this file may be located in the `test/` directory.

---

*Documentation generated on 2025-11-18T21:53:49.000102*
