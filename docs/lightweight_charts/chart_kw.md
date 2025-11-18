# Keywords: chart.py

**Source File:** `lightweight_charts/chart.py`
**Total Keywords:** 39

---

## Keyword Index (A-Z)

### A

#### `AbstractChart`

- **Occurrences:** 1
- **Context:** *...process.terminate()             self.wv_process.join()         self._reset()   class Chart(abstract.AbstractChart):     _main_window_handlers = None     WV: WebviewHandler = WebviewHandler()      def __init__(    ...*
- **Link:** [View in docs](./chart_docs.md)

#### `active_screen`

- **Occurrences:** 3
- **Context:** *...if screen is not None else None         if maximize:             if screen is None:                 active_screen = webview.screens[0]                 width, height = active_screen.width, active_screen.height     ...*
- **Link:** [View in docs](./chart_docs.md)

#### `async_set`

- **Occurrences:** 1
- **Context:** *...y:             from lightweight_charts import polygon             [asyncio.create_task(self.polygon.async_set(*args)) for args in polygon._set_on_load]             while 1:                 while Chart.WV.emit_...*
- **Link:** [View in docs](./chart_docs.md)

### B

#### `background_color`

- **Occurrences:** 1
- **Context:** *...            x=x,             y=y,             screen=screen,             on_top=on_top,             background_color='#000000')         )          self.windows[-1].events.loaded += lambda: self.loaded_event.set()    ...*
- **Link:** [View in docs](./chart_docs.md)

### C

#### `CallbackAPI`

- **Occurrences:** 2
- **Context:** *...ts import abstract from .util import parse_event_message, FLOAT  import os import threading   class CallbackAPI:     def __init__(self, emit_queue):         self.emit_queue = emit_queue      def callback(self, m...*
- **Link:** [View in docs](./chart_docs.md)

#### `Chart`

- **Occurrences:** 14
- **Context:** *...       self.wv_process.terminate()             self.wv_process.join()         self._reset()   class Chart(abstract.AbstractChart):     _main_window_handlers = None     WV: WebviewHandler = WebviewHandler()...*
- **Link:** [View in docs](./chart_docs.md)

#### `callback_api`

- **Occurrences:** 2
- **Context:** *...queue = emit_q         self.loaded_event = loaded_event          self.is_alive = True          self.callback_api = CallbackAPI(emit_q)         self.windows: typing.List[webview.Window] = []         self.loop()   ...*
- **Link:** [View in docs](./chart_docs.md)

#### `create_task`

- **Occurrences:** 1
- **Context:** *...w(block=False)         try:             from lightweight_charts import polygon             [asyncio.create_task(self.polygon.async_set(*args)) for args in polygon._set_on_load]             while 1:              ...*
- **Link:** [View in docs](./chart_docs.md)

#### `create_window`

- **Occurrences:** 7
- **Context:** *...ackAPI(emit_q)         self.windows: typing.List[webview.Window] = []         self.loop()       def create_window(         self, width, height, x, y, screen=None, on_top=False,         maximize=False, title=''    ...*
- **Link:** [View in docs](./chart_docs.md)

### E

#### `emit_q`

- **Occurrences:** 3
- **Context:** *...k(self, message: str):         self.emit_queue.put(message)   class PyWV:     def __init__(self, q, emit_q, return_q, loaded_event):         self.queue = q         self.return_queue = return_q         self....*
- **Link:** [View in docs](./chart_docs.md)

#### `emit_queue`

- **Occurrences:** 10
- **Context:** *... parse_event_message, FLOAT  import os import threading   class CallbackAPI:     def __init__(self, emit_queue):         self.emit_queue = emit_queue      def callback(self, message: str):         self.emit_que...*
- **Link:** [View in docs](./chart_docs.md)

#### `evaluate_js`

- **Occurrences:** 4
- **Context:** *...                   if '_~_~RETURN~_~_' in arg:                         self.return_queue.put(window.evaluate_js(arg[14:]))                     else:                         window.evaluate_js(arg)               ...*
- **Link:** [View in docs](./chart_docs.md)

### F

#### `FLOAT`

- **Occurrences:** 2
- **Context:** *...JavascriptException  from lightweight_charts import abstract from .util import parse_event_message, FLOAT  import os import threading   class CallbackAPI:     def __init__(self, emit_queue):         self.e...*
- **Link:** [View in docs](./chart_docs.md)

#### `function_call_queue`

- **Occurrences:** 7
- **Context:** *...t(self):         self.loaded_event = mp.Event()         self.return_queue = mp.Queue()         self.function_call_queue = mp.Queue()         self.emit_queue = mp.Queue()         self.wv_process = mp.Process(            ...*
- **Link:** [View in docs](./chart_docs.md)

### I

#### `INDEX`

- **Occurrences:** 1
- **Context:** *...ght          self.windows.append(webview.create_window(             title,             url=abstract.INDEX,             js_api=self.callback_api,             width=width,             height=height,         ...*
- **Link:** [View in docs](./chart_docs.md)

#### `inner_height`

- **Occurrences:** 3
- **Context:** *...      debug: bool = False,         toolbox: bool = False,         inner_width: float = 1.0,         inner_height: float = 1.0,         scale_candles_only: bool = False,         position: FLOAT = 'left'     ):    ...*
- **Link:** [View in docs](./chart_docs.md)

#### `inner_width`

- **Occurrences:** 3
- **Context:** *...        maximize: bool = False,         debug: bool = False,         toolbox: bool = False,         inner_width: float = 1.0,         inner_height: float = 1.0,         scale_candles_only: bool = False,         ...*
- **Link:** [View in docs](./chart_docs.md)

#### `is_alive`

- **Occurrences:** 9
- **Context:** *... = return_q         self.emit_queue = emit_q         self.loaded_event = loaded_event          self.is_alive = True          self.callback_api = CallbackAPI(emit_q)         self.windows: typing.List[webview.W...*
- **Link:** [View in docs](./chart_docs.md)

### J

#### `JavascriptException`

- **Occurrences:** 3
- **Context:** *...io import json import multiprocessing as mp import typing import webview from webview.errors import JavascriptException  from lightweight_charts import abstract from .util import parse_event_message, FLOAT  import os im...*
- **Link:** [View in docs](./chart_docs.md)

#### `js_api`

- **Occurrences:** 1
- **Context:** *...indows.append(webview.create_window(             title,             url=abstract.INDEX,             js_api=self.callback_api,             width=width,             height=height,             x=x,            ...*
- **Link:** [View in docs](./chart_docs.md)

#### `js_api_code`

- **Occurrences:** 1
- **Context:** *...ow(                     script_func=lambda s: Chart.WV.evaluate_js(self._i, s),                     js_api_code='pywebview.api.callback'                 )          abstract.Window._return_q = Chart.WV.return_que...*
- **Link:** [View in docs](./chart_docs.md)

### K

#### `KeyError`

- **Occurrences:** 1
- **Context:** *...))                     else:                         window.evaluate_js(arg)                 except KeyError as e:                     return                 except JavascriptException as e:                  ...*
- **Link:** [View in docs](./chart_docs.md)

#### `KeyboardInterrupt`

- **Occurrences:** 1
- **Context:** *...             await func(*args) if asyncio.iscoroutinefunction(func) else func(*args)         except KeyboardInterrupt:             return      def hide(self):         """         Hides the chart window.\n         """ ...*
- **Link:** [View in docs](./chart_docs.md)

### L

#### `lightweight_charts`

- **Occurrences:** 2
- **Context:** *...iprocessing as mp import typing import webview from webview.errors import JavascriptException  from lightweight_charts import abstract from .util import parse_event_message, FLOAT  import os import threading   class Ca...*
- **Link:** [View in docs](./chart_docs.md)

#### `loaded_event`

- **Occurrences:** 9
- **Context:** *...tr):         self.emit_queue.put(message)   class PyWV:     def __init__(self, q, emit_q, return_q, loaded_event):         self.queue = q         self.return_queue = return_q         self.emit_queue = emit_q     ...*
- **Link:** [View in docs](./chart_docs.md)

### M

#### `max_window_num`

- **Occurrences:** 3
- **Context:** *... self.return_queue, self.loaded_event             ),             daemon=True         )         self.max_window_num = -1      def create_window(         self, width, height, x, y, screen=None, on_top=False,         ...*
- **Link:** [View in docs](./chart_docs.md)

### O

#### `on_js_load`

- **Occurrences:** 1
- **Context:** *...osed.         """         if not self.win.loaded:             Chart.WV.start()             self.win.on_js_load()         else:             Chart.WV.show(self._i)         if block:             asyncio.run(self.s...*
- **Link:** [View in docs](./chart_docs.md)

#### `on_top`

- **Occurrences:** 7
- **Context:** *...] = []         self.loop()       def create_window(         self, width, height, x, y, screen=None, on_top=False,         maximize=False, title=''     ):         screen = webview.screens[screen] if screen i...*
- **Link:** [View in docs](./chart_docs.md)

### P

#### `PyWV`

- **Occurrences:** 2
- **Context:** *...ue = emit_queue      def callback(self, message: str):         self.emit_queue.put(message)   class PyWV:     def __init__(self, q, emit_q, return_q, loaded_event):         self.queue = q         self.ret...*
- **Link:** [View in docs](./chart_docs.md)

#### `parse_event_message`

- **Occurrences:** 2
- **Context:** *...ebview.errors import JavascriptException  from lightweight_charts import abstract from .util import parse_event_message, FLOAT  import os import threading   class CallbackAPI:     def __init__(self, emit_queue):        ...*
- **Link:** [View in docs](./chart_docs.md)

### R

#### `RETURN`

- **Occurrences:** 1
- **Context:** *...':                 window.hide()             else:                 try:                     if '_~_~RETURN~_~_' in arg:                         self.return_queue.put(window.evaluate_js(arg[14:]))           ...*
- **Link:** [View in docs](./chart_docs.md)

#### `return_q`

- **Occurrences:** 2
- **Context:** *...message: str):         self.emit_queue.put(message)   class PyWV:     def __init__(self, q, emit_q, return_q, loaded_event):         self.queue = q         self.return_queue = return_q         self.emit_queue...*
- **Link:** [View in docs](./chart_docs.md)

#### `return_queue`

- **Occurrences:** 5
- **Context:** *...yWV:     def __init__(self, q, emit_q, return_q, loaded_event):         self.queue = q         self.return_queue = return_q         self.emit_queue = emit_q         self.loaded_event = loaded_event          self....*
- **Link:** [View in docs](./chart_docs.md)

### S

#### `scale_candles_only`

- **Occurrences:** 3
- **Context:** *...toolbox: bool = False,         inner_width: float = 1.0,         inner_height: float = 1.0,         scale_candles_only: bool = False,         position: FLOAT = 'left'     ):         Chart.WV.debug = debug         self....*
- **Link:** [View in docs](./chart_docs.md)

#### `script_func`

- **Occurrences:** 1
- **Context:** *...n, on_top, maximize, title                 )          window = abstract.Window(                     script_func=lambda s: Chart.WV.evaluate_js(self._i, s),                     js_api_code='pywebview.api.callback...*
- **Link:** [View in docs](./chart_docs.md)

#### `show_async`

- **Occurrences:** 2
- **Context:** *...d()         else:             Chart.WV.show(self._i)         if block:             asyncio.run(self.show_async())      async def show_async(self):         self.show(block=False)         try:             from li...*
- **Link:** [View in docs](./chart_docs.md)

### W

#### `WebviewHandler`

- **Occurrences:** 3
- **Context:** *...ript -> '{arg}',\nerror -> {msg['name']}[{msg['line']}:{msg['column']}]\n{msg['message']}")   class WebviewHandler():     def __init__(self) -> None:         self._reset()         self.debug = False      def _reset...*
- **Link:** [View in docs](./chart_docs.md)

#### `window_num`

- **Occurrences:** 6
- **Context:** *...function_call_queue.put(('start', self.debug))         self.loaded_event.wait()      def show(self, window_num):         self.function_call_queue.put((window_num, 'show'))      def hide(self, window_num):      ...*
- **Link:** [View in docs](./chart_docs.md)

#### `wv_process`

- **Occurrences:** 5
- **Context:** *...e()         self.function_call_queue = mp.Queue()         self.emit_queue = mp.Queue()         self.wv_process = mp.Process(             target=PyWV, args=(                 self.function_call_queue, self.emit_q...*
- **Link:** [View in docs](./chart_docs.md)

---

*Keywords extracted on 2025-11-18T21:53:49.244890*
