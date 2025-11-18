# Keywords: toolbox.py

**Source File:** `lightweight_charts/toolbox.py`
**Total Keywords:** 9

---

## Keyword Index (A-Z)

### E

#### `export_drawings`

- **Occurrences:** 1
- **Context:** *...ath, 'r') as f:             json_data = json.load(f)             self.drawings = json_data      def export_drawings(self, file_path):         """         Exports the current list of drawings to the given file path. ...*
- **Link:** [View in docs](./toolbox_docs.md)

### F

#### `file_path`

- **Occurrences:** 4
- **Context:** *...) {self.id}.toolBox.loadDrawings({json.dumps(self.drawings[tag])})')      def import_drawings(self, file_path):         """         Imports a list of drawings stored at the given file path.         """        ...*
- **Link:** [View in docs](./toolbox_docs.md)

### I

#### `import_drawings`

- **Occurrences:** 1
- **Context:** *...'if ({self.id}.toolBox) {self.id}.toolBox.loadDrawings({json.dumps(self.drawings[tag])})')      def import_drawings(self, file_path):         """         Imports a list of drawings stored at the given file path.    ...*
- **Link:** [View in docs](./toolbox_docs.md)

### J

#### `json_data`

- **Occurrences:** 2
- **Context:** *...ings stored at the given file path.         """         with open(file_path, 'r') as f:             json_data = json.load(f)             self.drawings = json_data      def export_drawings(self, file_path):    ...*
- **Link:** [View in docs](./toolbox_docs.md)

### L

#### `load_drawings`

- **Occurrences:** 1
- **Context:** *...ave_drawings_under(chart.topbar['symbol'])`.         """         self._save_under = widget      def load_drawings(self, tag: str):         """         Loads and displays the drawings on the chart stored under the ...*
- **Link:** [View in docs](./toolbox_docs.md)

### R

#### `run_script`

- **Occurrences:** 4
- **Context:** *...import json   class ToolBox:     def __init__(self, chart):         self.run_script = chart.run_script         self.id = chart.id         self._save_under = None         self.drawings...*
- **Link:** [View in docs](./toolbox_docs.md)

### S

#### `save_drawings`

- **Occurrences:** 1
- **Context:** *... = chart.id         self._save_under = None         self.drawings = {}         chart.win.handlers[f'save_drawings{self.id}'] = self._save_drawings         self.run_script(f'{self.id}.createToolBox()')      def sav...*
- **Link:** [View in docs](./toolbox_docs.md)

#### `save_drawings_under`

- **Occurrences:** 2
- **Context:** *...ngs{self.id}'] = self._save_drawings         self.run_script(f'{self.id}.createToolBox()')      def save_drawings_under(self, widget: 'Widget'):         """         Drawings made on charts will be saved under the widget...*
- **Link:** [View in docs](./toolbox_docs.md)

### T

#### `ToolBox`

- **Occurrences:** 1
- **Context:** *...import json   class ToolBox:     def __init__(self, chart):         self.run_script = chart.run_script         self.id = chart....*
- **Link:** [View in docs](./toolbox_docs.md)

---

*Keywords extracted on 2025-11-18T21:53:49.238804*
