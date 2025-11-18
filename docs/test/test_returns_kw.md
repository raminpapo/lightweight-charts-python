# Keywords: test_returns.py

**Source File:** `test/test_returns.py`
**Total Keywords:** 13

---

## Keyword Index (A-Z)

### B

#### `BARS`

- **Occurrences:** 3
- **Context:** *... unittest import pandas as pd from lightweight_charts import Chart import asyncio  from util import BARS, Tester    class TestReturns(Tester):     def test_screenshot_returns_value(self):         self.cha...*
- **Link:** [View in docs](./test_returns_docs.md)

### C

#### `create_task`

- **Occurrences:** 1
- **Context:** *...screenshot_data)      def test_save_drawings(self):           async def main():             asyncio.create_task(self.chart.show_async());              await asyncio.sleep(2)             self.chart.toolbox.drawin...*
- **Link:** [View in docs](./test_returns_docs.md)

### I

#### `import_drawings`

- **Occurrences:** 1
- **Context:** *...     self.chart.toolbox.save_drawings_under(self.chart.topbar['symbol'])         self.chart.toolbox.import_drawings("drawings.json")         self.chart.toolbox.load_drawings("SYM")         asyncio.run(main())   if _...*
- **Link:** [View in docs](./test_returns_docs.md)

### L

#### `lightweight_charts`

- **Occurrences:** 1
- **Context:** *...import unittest import pandas as pd from lightweight_charts import Chart import asyncio  from util import BARS, Tester    class TestReturns(Tester):     def te...*
- **Link:** [View in docs](./test_returns_docs.md)

#### `load_drawings`

- **Occurrences:** 1
- **Context:** *...r['symbol'])         self.chart.toolbox.import_drawings("drawings.json")         self.chart.toolbox.load_drawings("SYM")         asyncio.run(main())   if __name__ == '__main__':     unittest.main()...*
- **Link:** [View in docs](./test_returns_docs.md)

### R

#### `run_script`

- **Occurrences:** 1
- **Context:** *...in python             self.assertTrue(len(self.chart.toolbox.drawings) == 0)             self.chart.run_script(f'{self.chart.id}.toolBox.saveDrawings();')             await asyncio.sleep(1)  # resave them, and ...*
- **Link:** [View in docs](./test_returns_docs.md)

### S

#### `SYM`

- **Occurrences:** 2
- **Context:** *...e, width=100, height=100)         self.chart.set(BARS)         self.chart.topbar.textbox('symbol', 'SYM', align='right')         self.chart.toolbox.save_drawings_under(self.chart.topbar['symbol'])       ...*
- **Link:** [View in docs](./test_returns_docs.md)

#### `save_drawings_under`

- **Occurrences:** 1
- **Context:** *...(BARS)         self.chart.topbar.textbox('symbol', 'SYM', align='right')         self.chart.toolbox.save_drawings_under(self.chart.topbar['symbol'])         self.chart.toolbox.import_drawings("drawings.json")         se...*
- **Link:** [View in docs](./test_returns_docs.md)

#### `screenshot_data`

- **Occurrences:** 2
- **Context:** *...test_screenshot_returns_value(self):         self.chart.set(BARS)         self.chart.show()         screenshot_data = self.chart.screenshot()         self.assertIsNotNone(screenshot_data)      def test_save_drawings...*
- **Link:** [View in docs](./test_returns_docs.md)

#### `show_async`

- **Occurrences:** 1
- **Context:** *...ef test_save_drawings(self):           async def main():             asyncio.create_task(self.chart.show_async());              await asyncio.sleep(2)             self.chart.toolbox.drawings.clear() # clear dra...*
- **Link:** [View in docs](./test_returns_docs.md)

### T

#### `TestReturns`

- **Occurrences:** 1
- **Context:** *...s as pd from lightweight_charts import Chart import asyncio  from util import BARS, Tester    class TestReturns(Tester):     def test_screenshot_returns_value(self):         self.chart.set(BARS)         self.cha...*
- **Link:** [View in docs](./test_returns_docs.md)

#### `test_save_drawings`

- **Occurrences:** 1
- **Context:** *...   screenshot_data = self.chart.screenshot()         self.assertIsNotNone(screenshot_data)      def test_save_drawings(self):           async def main():             asyncio.create_task(self.chart.show_async());       ...*
- **Link:** [View in docs](./test_returns_docs.md)

#### `test_screenshot_returns_value`

- **Occurrences:** 1
- **Context:** *...ts import Chart import asyncio  from util import BARS, Tester    class TestReturns(Tester):     def test_screenshot_returns_value(self):         self.chart.set(BARS)         self.chart.show()         screenshot_data = self.chart....*
- **Link:** [View in docs](./test_returns_docs.md)

---

*Keywords extracted on 2025-11-18T21:53:49.015332*
