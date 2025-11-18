# Keywords: widgets.py

**Source File:** `lightweight_charts/widgets.py`
**Total Keywords:** 38

---

## Keyword Index (A-Z)

### A

#### `AbstractChart`

- **Occurrences:** 3
- **Context:** *...te_task(func(*args)) if asyncio.iscoroutinefunction(func) else func(*args)   class WxChart(abstract.AbstractChart):     def __init__(self, parent, inner_width: float = 1.0, inner_height: float = 1.0,              ...*
- **Link:** [View in docs](./widgets_docs.md)

#### `AddScriptMessageHandler`

- **Occurrences:** 1
- **Context:** *...IEW_SCRIPT_MESSAGE_RECEIVED, lambda e: emit_callback(self.win, e.GetString()))         self.webview.AddScriptMessageHandler('wx_msg')          self.webview.LoadURL("file://"+abstract.INDEX)      def get_webview(self):      ...*
- **Link:** [View in docs](./widgets_docs.md)

### C

#### `CallLater`

- **Occurrences:** 1
- **Context:** *..., scale_candles_only, toolbox)          self.webview.Bind(wx.html2.EVT_WEBVIEW_LOADED, lambda e: wx.CallLater(500, self.win.on_js_load))         self.webview.Bind(wx.html2.EVT_WEBVIEW_SCRIPT_MESSAGE_RECEIVED, ...*
- **Link:** [View in docs](./widgets_docs.md)

#### `ContextMenuPolicy`

- **Occurrences:** 1
- **Context:** *...0, self.win.on_js_load))         if using_pyside6:             self.webview.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)         self.webview.load(QUrl.fromLocalFile(abstract.INDEX))       def get_webview(...*
- **Link:** [View in docs](./widgets_docs.md)

#### `create_task`

- **Occurrences:** 1
- **Context:** *...def emit_callback(window, string):     func, args = parse_event_message(window, string)     asyncio.create_task(func(*args)) if asyncio.iscoroutinefunction(func) else func(*args)   class WxChart(abstract.Abstrac...*
- **Link:** [View in docs](./widgets_docs.md)

### E

#### `EVT_WEBVIEW_LOADED`

- **Occurrences:** 1
- **Context:** *...        inner_width, inner_height, scale_candles_only, toolbox)          self.webview.Bind(wx.html2.EVT_WEBVIEW_LOADED, lambda e: wx.CallLater(500, self.win.on_js_load))         self.webview.Bind(wx.html2.EVT_WEBVIEW_S...*
- **Link:** [View in docs](./widgets_docs.md)

#### `EVT_WEBVIEW_SCRIPT_MESSAGE_RECEIVED`

- **Occurrences:** 1
- **Context:** *...EBVIEW_LOADED, lambda e: wx.CallLater(500, self.win.on_js_load))         self.webview.Bind(wx.html2.EVT_WEBVIEW_SCRIPT_MESSAGE_RECEIVED, lambda e: emit_callback(self.win, e.GetString()))         self.webview.AddScriptMessageHandler('wx...*
- **Link:** [View in docs](./widgets_docs.md)

#### `emit_callback`

- **Occurrences:** 3
- **Context:** *...          self.win = chart.win          @Slot(str)         def callback(self, message):             emit_callback(self.win, message)  try:     from streamlit.components.v1 import html as sthtml except ImportError:...*
- **Link:** [View in docs](./widgets_docs.md)

### F

#### `final_scripts`

- **Occurrences:** 2
- **Context:** *...height      def run_script(self, script, run_last=False):         if run_last:             self.win.final_scripts.append(script)         else:             self._html += '\n' + script      def load(self):         i...*
- **Link:** [View in docs](./widgets_docs.md)

### G

#### `GetString`

- **Occurrences:** 1
- **Context:** *...self.webview.Bind(wx.html2.EVT_WEBVIEW_SCRIPT_MESSAGE_RECEIVED, lambda e: emit_callback(self.win, e.GetString()))         self.webview.AddScriptMessageHandler('wx_msg')          self.webview.LoadURL("file://"+...*
- **Link:** [View in docs](./widgets_docs.md)

#### `get_webview`

- **Occurrences:** 2
- **Context:** *....AddScriptMessageHandler('wx_msg')          self.webview.LoadURL("file://"+abstract.INDEX)      def get_webview(self):         return self.webview   class QtChart(abstract.AbstractChart):     def __init__(self, ...*
- **Link:** [View in docs](./widgets_docs.md)

### H

#### `HTML`

- **Occurrences:** 5
- **Context:** *...1 import html as sthtml except ImportError:     sthtml = None  try:     from IPython.display import HTML, display     import warnings     warnings.filterwarnings("ignore", category=UserWarning, module="IP...*
- **Link:** [View in docs](./widgets_docs.md)

#### `html_code`

- **Occurrences:** 2
- **Context:** *...oundError('IPython.display.HTML was not found, and must be installed to use JupyterChart.')         html_code = html.escape(f"{self._html}</script></body></html>")         iframe = f'<iframe width="{self.width...*
- **Link:** [View in docs](./widgets_docs.md)

### I

#### `INDEX`

- **Occurrences:** 6
- **Context:** *...    self.webview.AddScriptMessageHandler('wx_msg')          self.webview.LoadURL("file://"+abstract.INDEX)      def get_webview(self):         return self.webview   class QtChart(abstract.AbstractChart):  ...*
- **Link:** [View in docs](./widgets_docs.md)

#### `ImportError`

- **Occurrences:** 6
- **Context:** *...import parse_event_message from lightweight_charts import abstract  try:     import wx.html2 except ImportError:     wx = None  try:     using_pyside6 = False     from PyQt5.QtWebEngineWidgets import QWebEngineV...*
- **Link:** [View in docs](./widgets_docs.md)

#### `inner_height`

- **Occurrences:** 10
- **Context:** *...)   class WxChart(abstract.AbstractChart):     def __init__(self, parent, inner_width: float = 1.0, inner_height: float = 1.0,                  scale_candles_only: bool = False, toolbox: bool = False):         if...*
- **Link:** [View in docs](./widgets_docs.md)

#### `inner_width`

- **Occurrences:** 10
- **Context:** *...tion(func) else func(*args)   class WxChart(abstract.AbstractChart):     def __init__(self, parent, inner_width: float = 1.0, inner_height: float = 1.0,                  scale_candles_only: bool = False, toolbox...*
- **Link:** [View in docs](./widgets_docs.md)

### J

#### `JupyterChart`

- **Occurrences:** 2
- **Context:** *...       sthtml(f'{self._html}</script></body></html>', width=self.width, height=self.height)   class JupyterChart(StaticLWC):     def __init__(self, width: int = 800, height=350, inner_width=1, inner_height=1, sca...*
- **Link:** [View in docs](./widgets_docs.md)

### L

#### `lightweight_charts`

- **Occurrences:** 1
- **Context:** *...import asyncio import html  from .util import parse_event_message from lightweight_charts import abstract  try:     import wx.html2 except ImportError:     wx = None  try:     using_pyside6...*
- **Link:** [View in docs](./widgets_docs.md)

### M

#### `ModuleNotFoundError`

- **Occurrences:** 4
- **Context:** *... scale_candles_only: bool = False, toolbox: bool = False):         if wx is None:             raise ModuleNotFoundError('wx.html2 was not found, and must be installed to use WxChart.')         self.webview: wx.html2.Web...*
- **Link:** [View in docs](./widgets_docs.md)

### N

#### `NoContextMenu`

- **Occurrences:** 1
- **Context:** *...load))         if using_pyside6:             self.webview.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)         self.webview.load(QUrl.fromLocalFile(abstract.INDEX))       def get_webview(self): return ...*
- **Link:** [View in docs](./widgets_docs.md)

### O

#### `on_js_load`

- **Occurrences:** 2
- **Context:** *...olbox)          self.webview.Bind(wx.html2.EVT_WEBVIEW_LOADED, lambda e: wx.CallLater(500, self.win.on_js_load))         self.webview.Bind(wx.html2.EVT_WEBVIEW_SCRIPT_MESSAGE_RECEIVED, lambda e: emit_callback(s...*
- **Link:** [View in docs](./widgets_docs.md)

### P

#### `parse_event_message`

- **Occurrences:** 2
- **Context:** *...import asyncio import html  from .util import parse_event_message from lightweight_charts import abstract  try:     import wx.html2 except ImportError:     wx = None...*
- **Link:** [View in docs](./widgets_docs.md)

### Q

#### `QtChart`

- **Occurrences:** 2
- **Context:** *...w.LoadURL("file://"+abstract.INDEX)      def get_webview(self):         return self.webview   class QtChart(abstract.AbstractChart):     def __init__(self, widget=None, inner_width: float = 1.0, inner_height...*
- **Link:** [View in docs](./widgets_docs.md)

#### `QtCore`

- **Occurrences:** 3
- **Context:** *...ebEngineWidgets import QWebEngineView     from PyQt5.QtWebChannel import QWebChannel     from PyQt5.QtCore import QObject, pyqtSlot as Slot, QUrl, QTimer except ImportError:     using_pyside6 = True     try...*
- **Link:** [View in docs](./widgets_docs.md)

#### `QtWebChannel`

- **Occurrences:** 3
- **Context:** *...y:     using_pyside6 = False     from PyQt5.QtWebEngineWidgets import QWebEngineView     from PyQt5.QtWebChannel import QWebChannel     from PyQt5.QtCore import QObject, pyqtSlot as Slot, QUrl, QTimer except Impo...*
- **Link:** [View in docs](./widgets_docs.md)

#### `QtWebEngineWidgets`

- **Occurrences:** 3
- **Context:** *...   import wx.html2 except ImportError:     wx = None  try:     using_pyside6 = False     from PyQt5.QtWebEngineWidgets import QWebEngineView     from PyQt5.QtWebChannel import QWebChannel     from PyQt5.QtCore import Q...*
- **Link:** [View in docs](./widgets_docs.md)

### R

#### `RunScript`

- **Occurrences:** 1
- **Context:** *....html2.WebView = wx.html2.WebView.New(parent)         super().__init__(abstract.Window(self.webview.RunScript, 'window.wx_msg.postMessage.bind(window.wx_msg)'),                          inner_width, inner_heig...*
- **Link:** [View in docs](./widgets_docs.md)

#### `run_last`

- **Occurrences:** 2
- **Context:** *...autosize)         self.width = width         self.height = height      def run_script(self, script, run_last=False):         if run_last:             self.win.final_scripts.append(script)         else:       ...*
- **Link:** [View in docs](./widgets_docs.md)

#### `run_script`

- **Occurrences:** 5
- **Context:** *...                 .replace('</body>\n</html>', '<script>')          super().__init__(abstract.Window(run_script=self.run_script), inner_width, inner_height,                          scale_candles_only, toolbox, ...*
- **Link:** [View in docs](./widgets_docs.md)

### S

#### `StaticLWC`

- **Occurrences:** 3
- **Context:** *...w.load(QUrl.fromLocalFile(abstract.INDEX))       def get_webview(self): return self.webview   class StaticLWC(abstract.AbstractChart):     def __init__(self, width=None, height=None, inner_width=1, inner_heigh...*
- **Link:** [View in docs](./widgets_docs.md)

#### `StreamlitChart`

- **Occurrences:** 2
- **Context:** *...ts:             self._html += '\n' + script         self._load()      def _load(self): pass   class StreamlitChart(StaticLWC):     def __init__(self, width=None, height=None, inner_width=1, inner_height=1, scale_ca...*
- **Link:** [View in docs](./widgets_docs.md)

#### `scale_candles_only`

- **Occurrences:** 10
- **Context:** *...   def __init__(self, parent, inner_width: float = 1.0, inner_height: float = 1.0,                  scale_candles_only: bool = False, toolbox: bool = False):         if wx is None:             raise ModuleNotFoundError...*
- **Link:** [View in docs](./widgets_docs.md)

### U

#### `UserWarning`

- **Occurrences:** 1
- **Context:** *...hon.display import HTML, display     import warnings     warnings.filterwarnings("ignore", category=UserWarning, module="IPython.core.display") except ImportError:     HTML = None   def emit_callback(window, str...*
- **Link:** [View in docs](./widgets_docs.md)

### W

#### `WebView`

- **Occurrences:** 2
- **Context:** *...ror('wx.html2 was not found, and must be installed to use WxChart.')         self.webview: wx.html2.WebView = wx.html2.WebView.New(parent)         super().__init__(abstract.Window(self.webview.RunScript, 'wi...*
- **Link:** [View in docs](./widgets_docs.md)

#### `WxChart`

- **Occurrences:** 2
- **Context:** *...     asyncio.create_task(func(*args)) if asyncio.iscoroutinefunction(func) else func(*args)   class WxChart(abstract.AbstractChart):     def __init__(self, parent, inner_width: float = 1.0, inner_height: flo...*
- **Link:** [View in docs](./widgets_docs.md)

#### `web_channel`

- **Occurrences:** 3
- **Context:** *...k'),                          inner_width, inner_height, scale_candles_only, toolbox)          self.web_channel = QWebChannel()         self.bridge = Bridge(self)         self.web_channel.registerObject('bridge'...*
- **Link:** [View in docs](./widgets_docs.md)

#### `wx_msg`

- **Occurrences:** 3
- **Context:** *....html2.WebView.New(parent)         super().__init__(abstract.Window(self.webview.RunScript, 'window.wx_msg.postMessage.bind(window.wx_msg)'),                          inner_width, inner_height, scale_candle...*
- **Link:** [View in docs](./widgets_docs.md)

---

*Keywords extracted on 2025-11-18T21:53:49.149187*
