# Keywords: tick_data.py

**Source File:** `examples/3_tick_data/tick_data.py`
**Total Keywords:** 3

---

## Keyword Index (A-Z)

### L

#### `lightweight_charts`

- **Occurrences:** 1
- **Context:** *...import pandas as pd from time import sleep from lightweight_charts import Chart  if __name__ == '__main__':      df1 = pd.read_csv('ohlc.csv')      # Columns: time | ...*
- **Link:** [View in docs](./tick_data_docs.md)

### R

#### `read_csv`

- **Occurrences:** 2
- **Context:** *...om time import sleep from lightweight_charts import Chart  if __name__ == '__main__':      df1 = pd.read_csv('ohlc.csv')      # Columns: time | price     df2 = pd.read_csv('ticks.csv')      chart = Chart()   ...*
- **Link:** [View in docs](./tick_data_docs.md)

### U

#### `update_from_tick`

- **Occurrences:** 1
- **Context:** *...t = Chart()      chart.set(df1)      chart.show()      for i, tick in df2.iterrows():         chart.update_from_tick(tick)         sleep(0.03) ...*
- **Link:** [View in docs](./tick_data_docs.md)

---

*Keywords extracted on 2025-11-18T21:53:48.999341*
