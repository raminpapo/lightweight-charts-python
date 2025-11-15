# callbacks.py Documentation

## File Metadata
- **Path**: `examples/6_callbacks/callbacks.py`
- **Extension**: `.py`
- **Lines of Code**: 47
- **File Size**: 1329 bytes

## Original Source

```py
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

## Overview

This file is located at `examples/6_callbacks/callbacks.py` and contains 47 lines of code.

## Python Code Analysis

### Functions

- **get_bar_data**(symbol, timeframe): Function implementation
- **on_search**(chart, searched_string): Function implementation
- **on_timeframe_selection**(chart): Function implementation
- **on_horizontal_line_move**(chart, line): Function implementation

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
