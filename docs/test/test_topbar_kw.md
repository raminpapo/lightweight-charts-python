# Keywords: test_topbar.py

**Source File:** `test/test_topbar.py`
**Total Keywords:** 5

---

## Keyword Index (A-Z)

### L

#### `lightweight_charts`

- **Occurrences:** 1
- **Context:** *...import unittest import pandas as pd  from lightweight_charts import Chart from util import Tester   class TestTopBar(Tester):     def test_switcher_fires_event(...*
- **Link:** [View in docs](./test_topbar_docs.md)

### R

#### `run_script`

- **Occurrences:** 2
- **Context:** *...1', '2'), func=lambda c: (self.assertEqual(c.topbar['a'].value, '2'), c.exit()))         self.chart.run_script(f'{self.chart.topbar["a"].id}.intervalElements[1].dispatchEvent(new Event("click"))')         self....*
- **Link:** [View in docs](./test_topbar_docs.md)

### T

#### `TestTopBar`

- **Occurrences:** 1
- **Context:** *... unittest import pandas as pd  from lightweight_charts import Chart from util import Tester   class TestTopBar(Tester):     def test_switcher_fires_event(self):         self.chart.topbar.switcher('a', ('1', '2'...*
- **Link:** [View in docs](./test_topbar_docs.md)

#### `test_button_fires_event`

- **Occurrences:** 1
- **Context:** *...ntervalElements[1].dispatchEvent(new Event("click"))')         self.chart.show(block=True)      def test_button_fires_event(self):         self.chart.topbar.button('a', '1', func=lambda c: (self.assertEqual(c.topbar['a'].va...*
- **Link:** [View in docs](./test_topbar_docs.md)

#### `test_switcher_fires_event`

- **Occurrences:** 1
- **Context:** *...d  from lightweight_charts import Chart from util import Tester   class TestTopBar(Tester):     def test_switcher_fires_event(self):         self.chart.topbar.switcher('a', ('1', '2'), func=lambda c: (self.assertEqual(c.topba...*
- **Link:** [View in docs](./test_topbar_docs.md)

---

*Keywords extracted on 2025-11-18T21:53:49.018795*
