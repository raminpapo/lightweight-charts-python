# toolbox.md Documentation

## File Metadata
- **Path**: `docs/source/examples/toolbox.md`
- **Extension**: `.md`
- **Lines of Code**: 73
- **File Size**: 1881 bytes

## Original Source

```md
# Toolbox with persistent drawings

To get started, create a file called `drawings.json`, which should contain:
```
{}
```
___



```python
import pandas as pd
from lightweight_charts import Chart


def get_bar_data(symbol, timeframe):
    if symbol not in ('AAPL', 'GOOGL', 'TSLA'):
        print(f'No data for "{symbol}"')
        return pd.DataFrame()
    return pd.read_csv(f'bar_data/{symbol}_{timeframe}.csv')


def on_search(chart, searched_string):
    new_data = get_bar_data(searched_string, chart.topbar['timeframe'].value)
    if new_data.empty:
        return
    chart.topbar['symbol'].set(searched_string)
    chart.set(new_data)
    
    # Load the drawings saved under the symbol.
    chart.toolbox.load_drawings(searched_string)


def on_timeframe_selection(chart):
    new_data = get_bar_data(chart.topbar['symbol'].value, chart.topbar['timeframe'].value)
    if new_data.empty:
        return
    # The symbol has not changed, so we want to re-render the drawings.
    chart.set(new_data, keep_drawings=True)


if __name__ == '__main__':
    chart = Chart(toolbox=True)
    chart.legend(True)

    chart.events.search += on_search
    chart.topbar.textbox('symbol', 'TSLA')
    chart.topbar.switcher(
        'timeframe',
        ('1min', '5min', '30min'),
        default='5min',
        func=on_timeframe_selection
    )

    df = get_bar_data('TSLA', '5min')

    chart.set(df)

    # Imports the drawings saved in the JSON file.
    chart.toolbox.import_drawings('drawings.json')
    
    # Loads the drawings under the default symbol.
    chart.toolbox.load_drawings(chart.topbar['symbol'].value)  
    
    # Saves drawings based on the symbol.
    chart.toolbox.save_drawings_under(chart.topbar['symbol'])  

    chart.show(block=True)
    
    # Exports the drawings to the JSON file upon close.
    chart.toolbox.export_drawings('drawings.json')  

```
```

## Overview

This file is located at `docs/source/examples/toolbox.md` and contains 73 lines of code.

## Markdown Document Analysis

### Document Structure

- Toolbox with persistent drawings


## Related Files

This file is part of the repository structure. Related files may be found in the same directory or referenced in the code above.

## Tests

To test this file, refer to the repository's test suite in the `test/` directory.

## Performance & Security Notes

- Always review code for potential security vulnerabilities
- Ensure proper error handling is implemented
- Follow best practices for the language/framework being used
