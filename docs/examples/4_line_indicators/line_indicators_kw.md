# Keywords: line_indicators.py

**Source File:** `examples/4_line_indicators/line_indicators.py`
**Total Keywords:** 7

---

## Keyword Index (A-Z)

### C

#### `calculate_sma`

- **Occurrences:** 2
- **Context:** *...import pandas as pd from lightweight_charts import Chart   def calculate_sma(df, period: int = 50):     return pd.DataFrame({         'time': df['date'],         f'SMA {period}...*
- **Link:** [View in docs](./line_indicators_docs.md)

#### `create_line`

- **Occurrences:** 1
- **Context:** *...  chart.legend(visible=True)      df = pd.read_csv('ohlcv.csv')     chart.set(df)      line = chart.create_line('SMA 50')     sma_data = calculate_sma(df, period=50)     line.set(sma_data)      chart.show(block=...*
- **Link:** [View in docs](./line_indicators_docs.md)

### D

#### `DataFrame`

- **Occurrences:** 1
- **Context:** *...as pd from lightweight_charts import Chart   def calculate_sma(df, period: int = 50):     return pd.DataFrame({         'time': df['date'],         f'SMA {period}': df['close'].rolling(window=period).mean()   ...*
- **Link:** [View in docs](./line_indicators_docs.md)

### L

#### `lightweight_charts`

- **Occurrences:** 1
- **Context:** *...import pandas as pd from lightweight_charts import Chart   def calculate_sma(df, period: int = 50):     return pd.DataFrame({         'time': d...*
- **Link:** [View in docs](./line_indicators_docs.md)

### R

#### `read_csv`

- **Occurrences:** 1
- **Context:** *...opna()   if __name__ == '__main__':     chart = Chart()     chart.legend(visible=True)      df = pd.read_csv('ohlcv.csv')     chart.set(df)      line = chart.create_line('SMA 50')     sma_data = calculate_sma...*
- **Link:** [View in docs](./line_indicators_docs.md)

### S

#### `SMA`

- **Occurrences:** 2
- **Context:** *...alculate_sma(df, period: int = 50):     return pd.DataFrame({         'time': df['date'],         f'SMA {period}': df['close'].rolling(window=period).mean()     }).dropna()   if __name__ == '__main__':  ...*
- **Link:** [View in docs](./line_indicators_docs.md)

#### `sma_data`

- **Occurrences:** 2
- **Context:** *...e)      df = pd.read_csv('ohlcv.csv')     chart.set(df)      line = chart.create_line('SMA 50')     sma_data = calculate_sma(df, period=50)     line.set(sma_data)      chart.show(block=True) ...*
- **Link:** [View in docs](./line_indicators_docs.md)

---

*Keywords extracted on 2025-11-18T21:53:49.006005*
