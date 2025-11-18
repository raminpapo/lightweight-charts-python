# Keywords: test_toolbox.py

**Source File:** `test/test_toolbox.py`
**Total Keywords:** 12

---

## Keyword Index (A-Z)

### B

#### `BARS`

- **Occurrences:** 8
- **Context:** *...import unittest import pandas as pd  from lightweight_charts import Chart from util import BARS, Tester  from time import sleep   class TestToolBox(Tester):     def test_create_horizontal_line(se...*
- **Link:** [View in docs](./test_toolbox_docs.md)

### H

#### `horizontal_line`

- **Occurrences:** 1
- **Context:** *... def test_create_horizontal_line(self):         self.chart.set(BARS)         horz_line = self.chart.horizontal_line(200, width=4)         self.chart.show()         result = self.chart.win.run_script_and_get(f"{horz_...*
- **Link:** [View in docs](./test_toolbox_docs.md)

#### `horz_line`

- **Occurrences:** 6
- **Context:** *...estToolBox(Tester):     def test_create_horizontal_line(self):         self.chart.set(BARS)         horz_line = self.chart.horizontal_line(200, width=4)         self.chart.show()         result = self.chart.wi...*
- **Link:** [View in docs](./test_toolbox_docs.md)

### L

#### `lightweight_charts`

- **Occurrences:** 1
- **Context:** *...import unittest import pandas as pd  from lightweight_charts import Chart from util import BARS, Tester  from time import sleep   class TestToolBox(Tester):    ...*
- **Link:** [View in docs](./test_toolbox_docs.md)

### R

#### `run_script_and_get`

- **Occurrences:** 3
- **Context:** *... self.chart.horizontal_line(200, width=4)         self.chart.show()         result = self.chart.win.run_script_and_get(f"{horz_line.id}._options");         self.assertTrue(result)         self.chart.exit()      def tes...*
- **Link:** [View in docs](./test_toolbox_docs.md)

### T

#### `TestToolBox`

- **Occurrences:** 1
- **Context:** *... from lightweight_charts import Chart from util import BARS, Tester  from time import sleep   class TestToolBox(Tester):     def test_create_horizontal_line(self):         self.chart.set(BARS)         horz_line ...*
- **Link:** [View in docs](./test_toolbox_docs.md)

#### `test_create_box`

- **Occurrences:** 1
- **Context:** *...get(f"{horz_line.id}._options");         self.assertTrue(result)         self.chart.exit()      def test_create_box(self):         self.chart.set(BARS)         horz_line = self.chart.box(BARS.iloc[-10]['date'], 180,...*
- **Link:** [View in docs](./test_toolbox_docs.md)

#### `test_create_horizontal_line`

- **Occurrences:** 1
- **Context:** *...rt Chart from util import BARS, Tester  from time import sleep   class TestToolBox(Tester):     def test_create_horizontal_line(self):         self.chart.set(BARS)         horz_line = self.chart.horizontal_line(200, width=4)   ...*
- **Link:** [View in docs](./test_toolbox_docs.md)

#### `test_create_trend_line`

- **Occurrences:** 1
- **Context:** *...get(f"{horz_line.id}._options");         self.assertTrue(result)         self.chart.exit()      def test_create_trend_line(self):         self.chart.set(BARS)         horz_line = self.chart.trend_line(BARS.iloc[-10]['date'...*
- **Link:** [View in docs](./test_toolbox_docs.md)

#### `test_create_vertical_line`

- **Occurrences:** 1
- **Context:** *...get(f"{horz_line.id}._options");         self.assertTrue(result)         self.chart.exit()      def test_create_vertical_line(self):         ...      def test_create_vertical_span(self):         ...   if __name__ == '__main__...*
- **Link:** [View in docs](./test_toolbox_docs.md)

#### `test_create_vertical_span`

- **Occurrences:** 1
- **Context:** *...ue(result)         self.chart.exit()      def test_create_vertical_line(self):         ...      def test_create_vertical_span(self):         ...   if __name__ == '__main__':     unittest.main()...*
- **Link:** [View in docs](./test_toolbox_docs.md)

#### `trend_line`

- **Occurrences:** 1
- **Context:** *...      def test_create_trend_line(self):         self.chart.set(BARS)         horz_line = self.chart.trend_line(BARS.iloc[-10]['date'], 180, BARS.iloc[-3]['date'], 190)         self.chart.show()         result =...*
- **Link:** [View in docs](./test_toolbox_docs.md)

---

*Keywords extracted on 2025-11-18T21:53:49.017238*
