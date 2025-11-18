# Keywords: callbacks.py

**Source File:** `examples/6_callbacks/callbacks.py`
**Total Keywords:** 14

---

## Keyword Index (A-Z)

### A

#### `AAPL`

- **Occurrences:** 1
- **Context:** *... from lightweight_charts import Chart   def get_bar_data(symbol, timeframe):     if symbol not in ('AAPL', 'GOOGL', 'TSLA'):         print(f'No data for "{symbol}"')         return pd.DataFrame()     retu...*
- **Link:** [View in docs](./callbacks_docs.md)

### B

#### `bar_data`

- **Occurrences:** 1
- **Context:** *...'):         print(f'No data for "{symbol}"')         return pd.DataFrame()     return pd.read_csv(f'bar_data/{symbol}_{timeframe}.csv')   def on_search(chart, searched_string):  # Called when the user searche...*
- **Link:** [View in docs](./callbacks_docs.md)

### D

#### `DataFrame`

- **Occurrences:** 1
- **Context:** *...symbol not in ('AAPL', 'GOOGL', 'TSLA'):         print(f'No data for "{symbol}"')         return pd.DataFrame()     return pd.read_csv(f'bar_data/{symbol}_{timeframe}.csv')   def on_search(chart, searched_stri...*
- **Link:** [View in docs](./callbacks_docs.md)

### G

#### `GOOGL`

- **Occurrences:** 1
- **Context:** *...ghtweight_charts import Chart   def get_bar_data(symbol, timeframe):     if symbol not in ('AAPL', 'GOOGL', 'TSLA'):         print(f'No data for "{symbol}"')         return pd.DataFrame()     return pd.rea...*
- **Link:** [View in docs](./callbacks_docs.md)

#### `get_bar_data`

- **Occurrences:** 4
- **Context:** *...import pandas as pd from lightweight_charts import Chart   def get_bar_data(symbol, timeframe):     if symbol not in ('AAPL', 'GOOGL', 'TSLA'):         print(f'No data for "{s...*
- **Link:** [View in docs](./callbacks_docs.md)

### H

#### `horizontal_line`

- **Occurrences:** 1
- **Context:** *...   func=on_timeframe_selection)      df = get_bar_data('TSLA', '5min')     chart.set(df)      chart.horizontal_line(200, func=on_horizontal_line_move)      chart.show(block=True) ...*
- **Link:** [View in docs](./callbacks_docs.md)

### L

#### `lightweight_charts`

- **Occurrences:** 1
- **Context:** *...import pandas as pd from lightweight_charts import Chart   def get_bar_data(symbol, timeframe):     if symbol not in ('AAPL', 'GOOGL', 'TSLA'):...*
- **Link:** [View in docs](./callbacks_docs.md)

### N

#### `new_data`

- **Occurrences:** 6
- **Context:** *...l}_{timeframe}.csv')   def on_search(chart, searched_string):  # Called when the user searches.     new_data = get_bar_data(searched_string, chart.topbar['timeframe'].value)     if new_data.empty:         ret...*
- **Link:** [View in docs](./callbacks_docs.md)

### O

#### `on_horizontal_line_move`

- **Occurrences:** 2
- **Context:** *...opbar['timeframe'].value)     if new_data.empty:         return     chart.set(new_data, True)   def on_horizontal_line_move(chart, line):     print(f'Horizontal line moved to: {line.price}')   if __name__ == '__main__':    ...*
- **Link:** [View in docs](./callbacks_docs.md)

#### `on_search`

- **Occurrences:** 2
- **Context:** *...')         return pd.DataFrame()     return pd.read_csv(f'bar_data/{symbol}_{timeframe}.csv')   def on_search(chart, searched_string):  # Called when the user searches.     new_data = get_bar_data(searched_str...*
- **Link:** [View in docs](./callbacks_docs.md)

#### `on_timeframe_selection`

- **Occurrences:** 2
- **Context:** *...empty:         return     chart.topbar['symbol'].set(searched_string)     chart.set(new_data)   def on_timeframe_selection(chart):  # Called when the user changes the timeframe.     new_data = get_bar_data(chart.topbar['sy...*
- **Link:** [View in docs](./callbacks_docs.md)

### R

#### `read_csv`

- **Occurrences:** 1
- **Context:** *...OGL', 'TSLA'):         print(f'No data for "{symbol}"')         return pd.DataFrame()     return pd.read_csv(f'bar_data/{symbol}_{timeframe}.csv')   def on_search(chart, searched_string):  # Called when the u...*
- **Link:** [View in docs](./callbacks_docs.md)

### S

#### `searched_string`

- **Occurrences:** 3
- **Context:** *... pd.DataFrame()     return pd.read_csv(f'bar_data/{symbol}_{timeframe}.csv')   def on_search(chart, searched_string):  # Called when the user searches.     new_data = get_bar_data(searched_string, chart.topbar['time...*
- **Link:** [View in docs](./callbacks_docs.md)

### T

#### `TSLA`

- **Occurrences:** 3
- **Context:** *..._charts import Chart   def get_bar_data(symbol, timeframe):     if symbol not in ('AAPL', 'GOOGL', 'TSLA'):         print(f'No data for "{symbol}"')         return pd.DataFrame()     return pd.read_csv(f'...*
- **Link:** [View in docs](./callbacks_docs.md)

---

*Keywords extracted on 2025-11-18T21:53:49.000916*
