# toolbox.py

**File Path:** `lightweight_charts/toolbox.py`

**File Size:** 1,521 bytes
**Lines of Code:** 46
**Language:** python

---

## File Metadata

- **Relative Path:** `lightweight_charts/toolbox.py`
- **File Type:** .py
- **Size:** 1,521 bytes
- **Total Lines:** 46
- **Programming Language:** python

## Quick Summary

This file is part of the lightweight-charts-python repository.
 It defines 1 class(es).


## Original Source Code

```python

import json


class ToolBox:
    def __init__(self, chart):
        self.run_script = chart.run_script
        self.id = chart.id
        self._save_under = None
        self.drawings = {}
        chart.win.handlers[f'save_drawings{self.id}'] = self._save_drawings
        self.run_script(f'{self.id}.createToolBox()')

    def save_drawings_under(self, widget: 'Widget'):
        """
        Drawings made on charts will be saved under the widget given. eg `chart.toolbox.save_drawings_under(chart.topbar['symbol'])`.
        """
        self._save_under = widget

    def load_drawings(self, tag: str):
        """
        Loads and displays the drawings on the chart stored under the tag given.
        """
        if not self.drawings.get(tag):
            return
        self.run_script(f'if ({self.id}.toolBox) {self.id}.toolBox.loadDrawings({json.dumps(self.drawings[tag])})')

    def import_drawings(self, file_path):
        """
        Imports a list of drawings stored at the given file path.
        """
        with open(file_path, 'r') as f:
            json_data = json.load(f)
            self.drawings = json_data

    def export_drawings(self, file_path):
        """
        Exports the current list of drawings to the given file path.
        """
        with open(file_path, 'w+') as f:
            json.dump(self.drawings, f, indent=4)

    def _save_drawings(self, drawings):
        if not self._save_under:
            return
        self.drawings[self._save_under.value] = json.loads(drawings)


```

## High-Level Overview

### Classes (1)

- **`ToolBox`** (line 4)

### Imports (1)

- `import json`

## Detailed Walkthrough

### Code Structure

This file contains 46 lines of python.

#### Classes

##### ToolBox (Line 4)

```python
    def __init__(self, chart):
        self.run_script = chart.run_script
        self.id = chart.id
        self._save_under = None
        self.drawings = {}
        chart.win.handlers[f'save_drawings{self.id}'] = self._save_drawings
        self.run_script(f'{self.id}.createToolBox()')
```

## Usage Examples

To use this file in your project:

```python
from lightweight_charts.toolbox import *
```

## Performance & Security Notes

### Performance

- File size: 1,521 bytes
- Complexity: 0 functions, 1 classes

### Security

- **Recommendation:** Review this file for potential security vulnerabilities
- No obvious security concerns detected (basic scan)

## Related Files

*To be populated during folder indexing phase*

## Testing

Tests for this file may be located in the `test/` directory.

---

*Documentation generated on 2025-11-18T21:53:49.237968*
