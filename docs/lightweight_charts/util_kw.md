# Keywords: util.py

**Source File:** `lightweight_charts/util.py`
**Total Keywords:** 44

---

## Keyword Index (A-Z)

### A

#### `add_script`

- **Occurrences:** 1
- **Context:** *...nabled = False         self.script_func('\n'.join(self.scripts))         self.scripts = []      def add_script(self, script):         self.scripts.append(script) ...*
- **Link:** [View in docs](./util_docs.md)

#### `arrow_down`

- **Occurrences:** 2
- **Context:** *...otted']  MARKER_POSITION = Literal['above', 'below', 'inside']  MARKER_SHAPE = Literal['arrow_up', 'arrow_down', 'circle', 'square']  CROSSHAIR_MODE = Literal['normal', 'magnet', 'hidden']  PRICE_SCALE_MODE = L...*
- **Link:** [View in docs](./util_docs.md)

#### `arrow_up`

- **Occurrences:** 2
- **Context:** *...', 'sparse_dotted']  MARKER_POSITION = Literal['above', 'below', 'inside']  MARKER_SHAPE = Literal['arrow_up', 'arrow_down', 'circle', 'square']  CROSSHAIR_MODE = Literal['normal', 'magnet', 'hidden']  PRICE_...*
- **Link:** [View in docs](./util_docs.md)

#### `as_enum`

- **Occurrences:** 1
- **Context:** *...tamp, str, float]  NUM = Union[float, int]  FLOAT = Literal['left', 'right', 'top', 'bottom']   def as_enum(value, string_types):     types = string_types.__args__     return -1 if value not in types else ty...*
- **Link:** [View in docs](./util_docs.md)

### B

#### `BulkRunScript`

- **Occurrences:** 1
- **Context:** *...lambda func, c, *args: func(c, *[float(a) if a != 'null' else None for a in args])         )  class BulkRunScript:     def __init__(self, script_func):         self.enabled = False         self.scripts = []       ...*
- **Link:** [View in docs](./util_docs.md)

#### `bulk_run`

- **Occurrences:** 2
- **Context:** *...t Window         self.win: Window = window         self.run_script = window.run_script         self.bulk_run = window.bulk_run         if hasattr(self, 'id'):             return         self.id = Window._id_g...*
- **Link:** [View in docs](./util_docs.md)

### C

#### `CROSSHAIR_MODE`

- **Occurrences:** 1
- **Context:** *...['above', 'below', 'inside']  MARKER_SHAPE = Literal['arrow_up', 'arrow_down', 'circle', 'square']  CROSSHAIR_MODE = Literal['normal', 'magnet', 'hidden']  PRICE_SCALE_MODE = Literal['normal', 'logarithmic', 'perce...*
- **Link:** [View in docs](./util_docs.md)

#### `create_task`

- **Occurrences:** 1
- **Context:** *...self._callable:             if asyncio.iscoroutinefunction(self._callable):                 asyncio.create_task(self._callable(*args))             else:                 self._callable(*args)   class JSEmitter:  ...*
- **Link:** [View in docs](./util_docs.md)

### D

#### `DataFrame`

- **Occurrences:** 2
- **Context:** *...gs.split(';;;')     func = window.handlers[name]     return func, args   def js_data(data: Union[pd.DataFrame, pd.Series]):     if isinstance(data, pd.DataFrame):         d = data.to_dict(orient='records')    ...*
- **Link:** [View in docs](./util_docs.md)

### E

#### `Emitter`

- **Occurrences:** 2
- **Context:** *...  'above': 'aboveBar',         'below': 'belowBar',         'inside': 'inBar',     }.get(p)   class Emitter:     def __init__(self):         self._callable = None      def __iadd__(self, other):         self...*
- **Link:** [View in docs](./util_docs.md)

#### `Events`

- **Occurrences:** 1
- **Context:** *...oroutinefunction(other) else final_wrapper         self._on_iadd(other)         return self   class Events:     def __init__(self, chart):         self.new_bar = Emitter()         self.search = JSEmitter(ch...*
- **Link:** [View in docs](./util_docs.md)

### F

#### `FLOAT`

- **Occurrences:** 1
- **Context:** *...ercentage', 'index100']  TIME = Union[datetime, pd.Timestamp, str, float]  NUM = Union[float, int]  FLOAT = Literal['left', 'right', 'top', 'bottom']   def as_enum(value, string_types):     types = string_...*
- **Link:** [View in docs](./util_docs.md)

#### `filtered_dict`

- **Occurrences:** 3
- **Context:** *...')     return components[0] + ''.join(x.title() for x in components[1:])  def js_json(d: dict):     filtered_dict = {}     for key, val in d.items():         if key in ('self') or val in (None,):             conti...*
- **Link:** [View in docs](./util_docs.md)

#### `filtered_records`

- **Occurrences:** 3
- **Context:** *...Series]):     if isinstance(data, pd.DataFrame):         d = data.to_dict(orient='records')         filtered_records = [{k: v for k, v in record.items() if v is not None and not pd.isna(v)} for record in d]     else:...*
- **Link:** [View in docs](./util_docs.md)

#### `final_async_wrapper`

- **Occurrences:** 2
- **Context:** *...f._chart, *arg) if not self._wrapper else self._wrapper(other, self._chart, *arg)         async def final_async_wrapper(*arg):             await other(self._chart, *arg) if not self._wrapper else await self._wrapper(oth...*
- **Link:** [View in docs](./util_docs.md)

#### `final_wrapper`

- **Occurrences:** 2
- **Context:** *...      self._name = name         self._wrapper = wrapper      def __iadd__(self, other):         def final_wrapper(*arg):             other(self._chart, *arg) if not self._wrapper else self._wrapper(other, self._ch...*
- **Link:** [View in docs](./util_docs.md)

### I

#### `IDGen`

- **Occurrences:** 1
- **Context:** *...     if hasattr(self, 'id'):             return         self.id = Window._id_gen.generate()   class IDGen(list):     ascii = 'abcdefghijklmnopqrstuvwxyz'      def generate(self) -> str:         var = ''.jo...*
- **Link:** [View in docs](./util_docs.md)

### J

#### `JSEmitter`

- **Occurrences:** 4
- **Context:** *....create_task(self._callable(*args))             else:                 self._callable(*args)   class JSEmitter:     def __init__(self, chart, name, on_iadd, wrapper=None):         self._on_iadd = on_iadd       ...*
- **Link:** [View in docs](./util_docs.md)

#### `JSON`

- **Occurrences:** 1
- **Context:** *... if '_' in key:             key = snake_to_camel(key)         filtered_dict[key] = val     return f"JSON.parse('{json.dumps(filtered_dict)}')"   def jbool(b: bool): return 'true' if b is True else 'false'...*
- **Link:** [View in docs](./util_docs.md)

#### `jbool`

- **Occurrences:** 1
- **Context:** *...key)         filtered_dict[key] = val     return f"JSON.parse('{json.dumps(filtered_dict)}')"   def jbool(b: bool): return 'true' if b is True else 'false' if b is False else None   LINE_STYLE = Literal['s...*
- **Link:** [View in docs](./util_docs.md)

#### `js_data`

- **Occurrences:** 1
- **Context:** *...it('_~_')     args = args.split(';;;')     func = window.handlers[name]     return func, args   def js_data(data: Union[pd.DataFrame, pd.Series]):     if isinstance(data, pd.DataFrame):         d = data.to_d...*
- **Link:** [View in docs](./util_docs.md)

#### `js_json`

- **Occurrences:** 1
- **Context:** *...omponents = s.split('_')     return components[0] + ''.join(x.title() for x in components[1:])  def js_json(d: dict):     filtered_dict = {}     for key, val in d.items():         if key in ('self') or val i...*
- **Link:** [View in docs](./util_docs.md)

### L

#### `LINE_STYLE`

- **Occurrences:** 1
- **Context:** *...d_dict)}')"   def jbool(b: bool): return 'true' if b is True else 'false' if b is False else None   LINE_STYLE = Literal['solid', 'dotted', 'dashed', 'large_dashed', 'sparse_dotted']  MARKER_POSITION = Literal[...*
- **Link:** [View in docs](./util_docs.md)

#### `large_dashed`

- **Occurrences:** 1
- **Context:** *...b is True else 'false' if b is False else None   LINE_STYLE = Literal['solid', 'dotted', 'dashed', 'large_dashed', 'sparse_dotted']  MARKER_POSITION = Literal['above', 'below', 'inside']  MARKER_SHAPE = Literal['...*
- **Link:** [View in docs](./util_docs.md)

#### `lightweight_charts`

- **Occurrences:** 1
- **Context:** *...om numpy import isin import pandas as pd   class Pane:     def __init__(self, window):         from lightweight_charts import Window         self.win: Window = window         self.run_script = window.run_script        ...*
- **Link:** [View in docs](./util_docs.md)

### M

#### `MARKER_POSITION`

- **Occurrences:** 2
- **Context:** *...lse else None   LINE_STYLE = Literal['solid', 'dotted', 'dashed', 'large_dashed', 'sparse_dotted']  MARKER_POSITION = Literal['above', 'below', 'inside']  MARKER_SHAPE = Literal['arrow_up', 'arrow_down', 'circle', '...*
- **Link:** [View in docs](./util_docs.md)

#### `MARKER_SHAPE`

- **Occurrences:** 2
- **Context:** *... 'dashed', 'large_dashed', 'sparse_dotted']  MARKER_POSITION = Literal['above', 'below', 'inside']  MARKER_SHAPE = Literal['arrow_up', 'arrow_down', 'circle', 'square']  CROSSHAIR_MODE = Literal['normal', 'magnet...*
- **Link:** [View in docs](./util_docs.md)

#### `marker_position`

- **Occurrences:** 1
- **Context:** *...{         'arrow_up': 'arrowUp',         'arrow_down': 'arrowDown',     }.get(shape) or shape   def marker_position(p: MARKER_POSITION):     return {         'above': 'aboveBar',         'below': 'belowBar',        ...*
- **Link:** [View in docs](./util_docs.md)

#### `marker_shape`

- **Occurrences:** 1
- **Context:** *...    types = string_types.__args__     return -1 if value not in types else types.index(value)   def marker_shape(shape: MARKER_SHAPE):     return {         'arrow_up': 'arrowUp',         'arrow_down': 'arrowDown'...*
- **Link:** [View in docs](./util_docs.md)

### N

#### `NUM`

- **Occurrences:** 1
- **Context:** *...ormal', 'logarithmic', 'percentage', 'index100']  TIME = Union[datetime, pd.Timestamp, str, float]  NUM = Union[float, int]  FLOAT = Literal['left', 'right', 'top', 'bottom']   def as_enum(value, string_...*
- **Link:** [View in docs](./util_docs.md)

#### `new_bar`

- **Occurrences:** 1
- **Context:** *...elf._on_iadd(other)         return self   class Events:     def __init__(self, chart):         self.new_bar = Emitter()         self.search = JSEmitter(chart, f'search{chart.id}',             lambda o: chart...*
- **Link:** [View in docs](./util_docs.md)

### O

#### `on_iadd`

- **Occurrences:** 2
- **Context:** *... else:                 self._callable(*args)   class JSEmitter:     def __init__(self, chart, name, on_iadd, wrapper=None):         self._on_iadd = on_iadd         self._chart = chart         self._name = na...*
- **Link:** [View in docs](./util_docs.md)

### P

#### `PRICE_SCALE_MODE`

- **Occurrences:** 1
- **Context:** *...row_up', 'arrow_down', 'circle', 'square']  CROSSHAIR_MODE = Literal['normal', 'magnet', 'hidden']  PRICE_SCALE_MODE = Literal['normal', 'logarithmic', 'percentage', 'index100']  TIME = Union[datetime, pd.Timestamp, ...*
- **Link:** [View in docs](./util_docs.md)

#### `Pane`

- **Occurrences:** 1
- **Context:** *...import choices from typing import Literal, Union from numpy import isin import pandas as pd   class Pane:     def __init__(self, window):         from lightweight_charts import Window         self.win: Wi...*
- **Link:** [View in docs](./util_docs.md)

#### `parse_event_message`

- **Occurrences:** 1
- **Context:** *...self:             self.append(var)             return f'window.{var}'         self.generate()   def parse_event_message(window, string):     name, args = string.split('_~_')     args = args.split(';;;')     func = windo...*
- **Link:** [View in docs](./util_docs.md)

### R

#### `range_change`

- **Occurrences:** 3
- **Context:** *...{chart.id})             ''')         )         salt = chart.id[chart.id.index('.')+1:]         self.range_change = JSEmitter(chart, f'range_change{salt}',             lambda o: chart.run_script(f'''             l...*
- **Link:** [View in docs](./util_docs.md)

#### `run_script`

- **Occurrences:** 5
- **Context:** *...ndow):         from lightweight_charts import Window         self.win: Window = window         self.run_script = window.run_script         self.bulk_run = window.bulk_run         if hasattr(self, 'id'):        ...*
- **Link:** [View in docs](./util_docs.md)

### S

#### `script_func`

- **Occurrences:** 4
- **Context:** *...(a) if a != 'null' else None for a in args])         )  class BulkRunScript:     def __init__(self, script_func):         self.enabled = False         self.scripts = []         self.script_func = script_func    ...*
- **Link:** [View in docs](./util_docs.md)

#### `snake_to_camel`

- **Occurrences:** 2
- **Context:** *...ered_records = {k: v for k, v in d.items()}     return json.dumps(filtered_records, indent=2)   def snake_to_camel(s: str):     components = s.split('_')     return components[0] + ''.join(x.title() for x in compon...*
- **Link:** [View in docs](./util_docs.md)

#### `sparse_dotted`

- **Occurrences:** 1
- **Context:** *...false' if b is False else None   LINE_STYLE = Literal['solid', 'dotted', 'dashed', 'large_dashed', 'sparse_dotted']  MARKER_POSITION = Literal['above', 'below', 'inside']  MARKER_SHAPE = Literal['arrow_up', 'arrow...*
- **Link:** [View in docs](./util_docs.md)

#### `string_types`

- **Occurrences:** 2
- **Context:** *...t]  NUM = Union[float, int]  FLOAT = Literal['left', 'right', 'top', 'bottom']   def as_enum(value, string_types):     types = string_types.__args__     return -1 if value not in types else types.index(value)   d...*
- **Link:** [View in docs](./util_docs.md)

#### `subscribe_click`

- **Occurrences:** 2
- **Context:** *...ambda o, c, *arg: o(c, *[float(a) for a in arg])         )          self.click = JSEmitter(chart, f'subscribe_click{salt}',             lambda o: chart.run_script(f'''             let clickHandler{salt} = (param) =>...*
- **Link:** [View in docs](./util_docs.md)

### T

#### `TIME`

- **Occurrences:** 1
- **Context:** *...'magnet', 'hidden']  PRICE_SCALE_MODE = Literal['normal', 'logarithmic', 'percentage', 'index100']  TIME = Union[datetime, pd.Timestamp, str, float]  NUM = Union[float, int]  FLOAT = Literal['left', 'righ...*
- **Link:** [View in docs](./util_docs.md)

#### `to_dict`

- **Occurrences:** 2
- **Context:** *...data(data: Union[pd.DataFrame, pd.Series]):     if isinstance(data, pd.DataFrame):         d = data.to_dict(orient='records')         filtered_records = [{k: v for k, v in record.items() if v is not None and...*
- **Link:** [View in docs](./util_docs.md)

---

*Keywords extracted on 2025-11-18T21:53:49.237144*
