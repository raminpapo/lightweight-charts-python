# Keywords: test_chart.py

**Source File:** `test/test_chart.py`
**Total Keywords:** 9

---

## Keyword Index (A-Z)

### B

#### `BARS`

- **Occurrences:** 3
- **Context:** *...import unittest import pandas as pd from util import BARS, Tester from lightweight_charts import Chart   class TestChart(Tester):     def test_data_is_rename...*
- **Link:** [View in docs](./test_chart_docs.md)

### C

#### `create_line`

- **Occurrences:** 2
- **Context:** *...(columns={'date': 'time'}).columns))      def test_line_in_list(self):         result0 = self.chart.create_line()         result1 = self.chart.create_line()         self.assertEqual(result0, self.chart.lines()[0...*
- **Link:** [View in docs](./test_chart_docs.md)

### D

#### `DataFrame`

- **Occurrences:** 1
- **Context:** *...port Chart   class TestChart(Tester):     def test_data_is_renamed(self):         uppercase_df = pd.DataFrame(BARS.copy()).rename({'date': 'Date', 'open': 'OPEN', 'high': 'HIgh', 'low': 'Low', 'close': 'close'...*
- **Link:** [View in docs](./test_chart_docs.md)

### L

#### `lightweight_charts`

- **Occurrences:** 1
- **Context:** *...import unittest import pandas as pd from util import BARS, Tester from lightweight_charts import Chart   class TestChart(Tester):     def test_data_is_renamed(self):         uppercase_df = ...*
- **Link:** [View in docs](./test_chart_docs.md)

### O

#### `OPEN`

- **Occurrences:** 1
- **Context:** *...is_renamed(self):         uppercase_df = pd.DataFrame(BARS.copy()).rename({'date': 'Date', 'open': 'OPEN', 'high': 'HIgh', 'low': 'Low', 'close': 'close', 'volUME': 'volume'})         result = self.chart....*
- **Link:** [View in docs](./test_chart_docs.md)

### T

#### `TestChart`

- **Occurrences:** 1
- **Context:** *...test import pandas as pd from util import BARS, Tester from lightweight_charts import Chart   class TestChart(Tester):     def test_data_is_renamed(self):         uppercase_df = pd.DataFrame(BARS.copy()).renam...*
- **Link:** [View in docs](./test_chart_docs.md)

#### `test_data_is_renamed`

- **Occurrences:** 1
- **Context:** *...om util import BARS, Tester from lightweight_charts import Chart   class TestChart(Tester):     def test_data_is_renamed(self):         uppercase_df = pd.DataFrame(BARS.copy()).rename({'date': 'Date', 'open': 'OPEN', 'hi...*
- **Link:** [View in docs](./test_chart_docs.md)

#### `test_line_in_list`

- **Occurrences:** 1
- **Context:** *...elf.assertEqual(list(result.columns), list(BARS.rename(columns={'date': 'time'}).columns))      def test_line_in_list(self):         result0 = self.chart.create_line()         result1 = self.chart.create_line()       ...*
- **Link:** [View in docs](./test_chart_docs.md)

### U

#### `uppercase_df`

- **Occurrences:** 2
- **Context:** *...htweight_charts import Chart   class TestChart(Tester):     def test_data_is_renamed(self):         uppercase_df = pd.DataFrame(BARS.copy()).rename({'date': 'Date', 'open': 'OPEN', 'high': 'HIgh', 'low': 'Low', '...*
- **Link:** [View in docs](./test_chart_docs.md)

---

*Keywords extracted on 2025-11-18T21:53:49.008785*
