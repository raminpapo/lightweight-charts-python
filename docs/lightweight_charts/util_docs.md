# util.py

**File Path:** `lightweight_charts/util.py`

**File Size:** 6,104 bytes
**Lines of Code:** 192
**Language:** python

---

## File Metadata

- **Relative Path:** `lightweight_charts/util.py`
- **File Type:** .py
- **Size:** 6,104 bytes
- **Total Lines:** 192
- **Programming Language:** python

## Quick Summary

This file is part of the lightweight-charts-python repository.
 It defines 6 class(es).
 It contains 8 function(s).


## Original Source Code

```python

import asyncio
import json
from datetime import datetime
from random import choices
from typing import Literal, Union
from numpy import isin
import pandas as pd


class Pane:
    def __init__(self, window):
        from lightweight_charts import Window
        self.win: Window = window
        self.run_script = window.run_script
        self.bulk_run = window.bulk_run
        if hasattr(self, 'id'):
            return
        self.id = Window._id_gen.generate()


class IDGen(list):
    ascii = 'abcdefghijklmnopqrstuvwxyz'

    def generate(self) -> str:
        var = ''.join(choices(self.ascii, k=8))
        if var not in self:
            self.append(var)
            return f'window.{var}'
        self.generate()


def parse_event_message(window, string):
    name, args = string.split('_~_')
    args = args.split(';;;')
    func = window.handlers[name]
    return func, args


def js_data(data: Union[pd.DataFrame, pd.Series]):
    if isinstance(data, pd.DataFrame):
        d = data.to_dict(orient='records')
        filtered_records = [{k: v for k, v in record.items() if v is not None and not pd.isna(v)} for record in d]
    else:
        d = data.to_dict()
        filtered_records = {k: v for k, v in d.items()}
    return json.dumps(filtered_records, indent=2)


def snake_to_camel(s: str):
    components = s.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

def js_json(d: dict):
    filtered_dict = {}
    for key, val in d.items():
        if key in ('self') or val in (None,):
            continue
        if '_' in key:
            key = snake_to_camel(key)
        filtered_dict[key] = val
    return f"JSON.parse('{json.dumps(filtered_dict)}')"


def jbool(b: bool): return 'true' if b is True else 'false' if b is False else None


LINE_STYLE = Literal['solid', 'dotted', 'dashed', 'large_dashed', 'sparse_dotted']

MARKER_POSITION = Literal['above', 'below', 'inside']

MARKER_SHAPE = Literal['arrow_up', 'arrow_down', 'circle', 'square']

CROSSHAIR_MODE = Literal['normal', 'magnet', 'hidden']

PRICE_SCALE_MODE = Literal['normal', 'logarithmic', 'percentage', 'index100']

TIME = Union[datetime, pd.Timestamp, str, float]

NUM = Union[float, int]

FLOAT = Literal['left', 'right', 'top', 'bottom']


def as_enum(value, string_types):
    types = string_types.__args__
    return -1 if value not in types else types.index(value)


def marker_shape(shape: MARKER_SHAPE):
    return {
        'arrow_up': 'arrowUp',
        'arrow_down': 'arrowDown',
    }.get(shape) or shape


def marker_position(p: MARKER_POSITION):
    return {
        'above': 'aboveBar',
        'below': 'belowBar',
        'inside': 'inBar',
    }.get(p)


class Emitter:
    def __init__(self):
        self._callable = None

    def __iadd__(self, other):
        self._callable = other
        return self

    def _emit(self, *args):
        if self._callable:
            if asyncio.iscoroutinefunction(self._callable):
                asyncio.create_task(self._callable(*args))
            else:
                self._callable(*args)


class JSEmitter:
    def __init__(self, chart, name, on_iadd, wrapper=None):
        self._on_iadd = on_iadd
        self._chart = chart
        self._name = name
        self._wrapper = wrapper

    def __iadd__(self, other):
        def final_wrapper(*arg):
            other(self._chart, *arg) if not self._wrapper else self._wrapper(other, self._chart, *arg)
        async def final_async_wrapper(*arg):
            await other(self._chart, *arg) if not self._wrapper else await self._wrapper(other, self._chart, *arg)

        self._chart.win.handlers[self._name] = final_async_wrapper if asyncio.iscoroutinefunction(other) else final_wrapper
        self._on_iadd(other)
        return self


class Events:
    def __init__(self, chart):
        self.new_bar = Emitter()
        self.search = JSEmitter(chart, f'search{chart.id}',
            lambda o: chart.run_script(f'''
            Lib.Handler.makeSpinner({chart.id})
            {chart.id}.search = Lib.Handler.makeSearchBox({chart.id})
            ''')
        )
        salt = chart.id[chart.id.index('.')+1:]
        self.range_change = JSEmitter(chart, f'range_change{salt}',
            lambda o: chart.run_script(f'''
            let checkLogicalRange{salt} = (logical) => {{
                {chart.id}.chart.timeScale().unsubscribeVisibleLogicalRangeChange(checkLogicalRange{salt})
                
                let barsInfo = {chart.id}.series.barsInLogicalRange(logical)
                if (barsInfo) window.callbackFunction(`range_change{salt}_~_${{barsInfo.barsBefore}};;;${{barsInfo.barsAfter}}`)
                    
                setTimeout(() => {chart.id}.chart.timeScale().subscribeVisibleLogicalRangeChange(checkLogicalRange{salt}), 50)
            }}
            {chart.id}.chart.timeScale().subscribeVisibleLogicalRangeChange(checkLogicalRange{salt})
            '''),
            wrapper=lambda o, c, *arg: o(c, *[float(a) for a in arg])
        )

        self.click = JSEmitter(chart, f'subscribe_click{salt}',
            lambda o: chart.run_script(f'''
            let clickHandler{salt} = (param) => {{
                if (!param.point) return;
                const time = {chart.id}.chart.timeScale().coordinateToTime(param.point.x)
                const price = {chart.id}.series.coordinateToPrice(param.point.y);
                window.callbackFunction(`subscribe_click{salt}_~_${{time}};;;${{price}}`)
            }}
            {chart.id}.chart.subscribeClick(clickHandler{salt})
            '''),
            wrapper=lambda func, c, *args: func(c, *[float(a) if a != 'null' else None for a in args])
        )

class BulkRunScript:
    def __init__(self, script_func):
        self.enabled = False
        self.scripts = []
        self.script_func = script_func

    def __enter__(self):
        self.enabled = True

    def __exit__(self, *args):
        self.enabled = False
        self.script_func('\n'.join(self.scripts))
        self.scripts = []

    def add_script(self, script):
        self.scripts.append(script)


```

## High-Level Overview

### Classes (6)

- **`Pane`** (line 10)
- **`IDGen`** (line 21)
- **`Emitter`** (line 104)
- **`JSEmitter`** (line 120)
- **`Events`** (line 138)
- **`BulkRunScript`** (line 176)

### Functions (8)

- **`parse_event_message(window, string)`** (line 32)
- **`js_data(data: Union[pd.DataFrame, pd.Series])`** (line 39)
- **`snake_to_camel(s: str)`** (line 49)
- **`js_json(d: dict)`** (line 53)
- **`jbool(b: bool)`** (line 64)
- **`as_enum(value, string_types)`** (line 84)
- **`marker_shape(shape: MARKER_SHAPE)`** (line 89)
- **`marker_position(p: MARKER_POSITION)`** (line 96)

### Imports (7)

- `import asyncio`
- `import json`
- `from datetime import datetime`
- `from random import choices`
- `from typing import Literal, Union`
- `from numpy import isin`
- `import pandas as pd`

## Detailed Walkthrough

### Code Structure

This file contains 192 lines of python.

#### Classes

##### Pane (Line 10)

```python
    def __init__(self, window):
        from lightweight_charts import Window
        self.win: Window = window
        self.run_script = window.run_script
        self.bulk_run = window.bulk_run
        if hasattr(self, 'id'):
            return
        self.id = Window._id_gen.generate()
```

##### IDGen (Line 21)

```python
    ascii = 'abcdefghijklmnopqrstuvwxyz'
```

##### Emitter (Line 104)

```python
    def __init__(self):
        self._callable = None
```

##### JSEmitter (Line 120)

```python
    def __init__(self, chart, name, on_iadd, wrapper=None):
        self._on_iadd = on_iadd
        self._chart = chart
        self._name = name
        self._wrapper = wrapper
```

##### Events (Line 138)

```python
    def __init__(self, chart):
        self.new_bar = Emitter()
        self.search = JSEmitter(chart, f'search{chart.id}',
            lambda o: chart.run_script(f'''
            Lib.Handler.makeSpinner({chart.id})
            {chart.id}.search = Lib.Handler.makeSearchBox({chart.id})
            ''')
        )
        salt = chart.id[chart.id.index('.')+1:]
        self.range_change = JSEmitter(chart, f'range_change{salt}',
            lambda o: chart.run_script(f'''
            let checkLogica
```

##### BulkRunScript (Line 176)

```python
    def __init__(self, script_func):
        self.enabled = False
        self.scripts = []
        self.script_func = script_func
```


#### Functions

##### parse_event_message (Line 32)

**Parameters:** `window, string`

##### js_data (Line 39)

**Parameters:** `data: Union[pd.DataFrame, pd.Series]`

##### snake_to_camel (Line 49)

**Parameters:** `s: str`

##### js_json (Line 53)

**Parameters:** `d: dict`

##### jbool (Line 64)

**Parameters:** `b: bool`

##### as_enum (Line 84)

**Parameters:** `value, string_types`

##### marker_shape (Line 89)

**Parameters:** `shape: MARKER_SHAPE`

##### marker_position (Line 96)

**Parameters:** `p: MARKER_POSITION`

## Usage Examples

To use this file in your project:

```python
from lightweight_charts.util import *
```

## Performance & Security Notes

### Performance

- File size: 6,104 bytes
- Complexity: 8 functions, 6 classes

### Security

- **Recommendation:** Review this file for potential security vulnerabilities
- No obvious security concerns detected (basic scan)

## Related Files

*To be populated during folder indexing phase*

## Testing

Tests for this file may be located in the `test/` directory.

---

*Documentation generated on 2025-11-18T21:53:49.232218*
