# Keywords: live_data.py

**Source File:** `examples/2_live_data/live_data.py`
**Total Keywords:** 4

---

## Keyword Index (A-Z)

### L

#### `last_close`

- **Occurrences:** 3
- **Context:** *...csv('ohlcv.csv')     df2 = pd.read_csv('next_ohlcv.csv')      chart.set(df1)      chart.show()      last_close = df1.iloc[-1]['close']      for i, series in df2.iterrows():         chart.update(series)         ...*
- **Link:** [View in docs](./live_data_docs.md)

#### `lightweight_charts`

- **Occurrences:** 1
- **Context:** *...import pandas as pd from time import sleep from lightweight_charts import Chart  if __name__ == '__main__':      chart = Chart()      df1 = pd.read_csv('ohlcv.csv')  ...*
- **Link:** [View in docs](./live_data_docs.md)

### N

#### `next_ohlcv`

- **Occurrences:** 1
- **Context:** *...me__ == '__main__':      chart = Chart()      df1 = pd.read_csv('ohlcv.csv')     df2 = pd.read_csv('next_ohlcv.csv')      chart.set(df1)      chart.show()      last_close = df1.iloc[-1]['close']      for i, ser...*
- **Link:** [View in docs](./live_data_docs.md)

### R

#### `read_csv`

- **Occurrences:** 2
- **Context:** *...from lightweight_charts import Chart  if __name__ == '__main__':      chart = Chart()      df1 = pd.read_csv('ohlcv.csv')     df2 = pd.read_csv('next_ohlcv.csv')      chart.set(df1)      chart.show()      las...*
- **Link:** [View in docs](./live_data_docs.md)

---

*Keywords extracted on 2025-11-18T21:53:49.002094*
