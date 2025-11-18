# Keywords: run_tests.py

**Source File:** `test/run_tests.py`
**Total Keywords:** 14

---

## Keyword Index (A-Z)

### T

#### `TEST_CASES`

- **Occurrences:** 2
- **Context:** *...st_toolbox import TestToolBox from test_topbar import TestTopBar from test_chart import TestChart   TEST_CASES = [     TestReturns,     TestTable,     TestToolBox,     TestTopBar,     TestChart, ]  if __name__ ...*
- **Link:** [View in docs](./run_tests_docs.md)

#### `TestChart`

- **Occurrences:** 2
- **Context:** *...able from test_toolbox import TestToolBox from test_topbar import TestTopBar from test_chart import TestChart   TEST_CASES = [     TestReturns,     TestTable,     TestToolBox,     TestTopBar,     TestChart, ] ...*
- **Link:** [View in docs](./run_tests_docs.md)

#### `TestLoader`

- **Occurrences:** 1
- **Context:** *...    TestToolBox,     TestTopBar,     TestChart, ]  if __name__ == '__main__':     loader = unittest.TestLoader()     cases = [loader.loadTestsFromTestCase(module) for module in TEST_CASES]     suite = unittest....*
- **Link:** [View in docs](./run_tests_docs.md)

#### `TestReturns`

- **Occurrences:** 2
- **Context:** *...import unittest  from test_returns import TestReturns from test_table import TestTable from test_toolbox import TestToolBox from test_topbar import TestT...*
- **Link:** [View in docs](./run_tests_docs.md)

#### `TestSuite`

- **Occurrences:** 1
- **Context:** *...()     cases = [loader.loadTestsFromTestCase(module) for module in TEST_CASES]     suite = unittest.TestSuite(cases)     unittest.TextTestRunner(verbosity=2).run(suite)...*
- **Link:** [View in docs](./run_tests_docs.md)

#### `TestTable`

- **Occurrences:** 2
- **Context:** *...import unittest  from test_returns import TestReturns from test_table import TestTable from test_toolbox import TestToolBox from test_topbar import TestTopBar from test_chart import Test...*
- **Link:** [View in docs](./run_tests_docs.md)

#### `TestToolBox`

- **Occurrences:** 2
- **Context:** *...est  from test_returns import TestReturns from test_table import TestTable from test_toolbox import TestToolBox from test_topbar import TestTopBar from test_chart import TestChart   TEST_CASES = [     TestReturn...*
- **Link:** [View in docs](./run_tests_docs.md)

#### `TestTopBar`

- **Occurrences:** 2
- **Context:** *...turns from test_table import TestTable from test_toolbox import TestToolBox from test_topbar import TestTopBar from test_chart import TestChart   TEST_CASES = [     TestReturns,     TestTable,     TestToolBox, ...*
- **Link:** [View in docs](./run_tests_docs.md)

#### `TextTestRunner`

- **Occurrences:** 1
- **Context:** *...tsFromTestCase(module) for module in TEST_CASES]     suite = unittest.TestSuite(cases)     unittest.TextTestRunner(verbosity=2).run(suite)...*
- **Link:** [View in docs](./run_tests_docs.md)

#### `test_chart`

- **Occurrences:** 1
- **Context:** *...table import TestTable from test_toolbox import TestToolBox from test_topbar import TestTopBar from test_chart import TestChart   TEST_CASES = [     TestReturns,     TestTable,     TestToolBox,     TestTopBar, ...*
- **Link:** [View in docs](./run_tests_docs.md)

#### `test_returns`

- **Occurrences:** 1
- **Context:** *...import unittest  from test_returns import TestReturns from test_table import TestTable from test_toolbox import TestToolBox from test_...*
- **Link:** [View in docs](./run_tests_docs.md)

#### `test_table`

- **Occurrences:** 1
- **Context:** *...import unittest  from test_returns import TestReturns from test_table import TestTable from test_toolbox import TestToolBox from test_topbar import TestTopBar from test_...*
- **Link:** [View in docs](./run_tests_docs.md)

#### `test_toolbox`

- **Occurrences:** 1
- **Context:** *...import unittest  from test_returns import TestReturns from test_table import TestTable from test_toolbox import TestToolBox from test_topbar import TestTopBar from test_chart import TestChart   TEST_CASES...*
- **Link:** [View in docs](./run_tests_docs.md)

#### `test_topbar`

- **Occurrences:** 1
- **Context:** *...turns import TestReturns from test_table import TestTable from test_toolbox import TestToolBox from test_topbar import TestTopBar from test_chart import TestChart   TEST_CASES = [     TestReturns,     TestTable,...*
- **Link:** [View in docs](./run_tests_docs.md)

---

*Keywords extracted on 2025-11-18T21:53:49.011799*
