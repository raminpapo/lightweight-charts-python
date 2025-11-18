# Keywords: abstract.py

**Source File:** `lightweight_charts/abstract.py`
**Total Keywords:** 156

---

## Keyword Index (A-Z)

### A

#### `AbstractChart`

- **Occurrences:** 6
- **Context:** *...: bool = False,         sync_crosshairs_only: bool = False,         toolbox: bool = False     ) -> 'AbstractChart':         subchart = AbstractChart(             self,             width,             height,       ...*
- **Link:** [View in docs](./abstract_docs.md)

#### `AttributeError`

- **Occurrences:** 1
- **Context:** *...s JavaScript within the Webview.         """         if self.script_func is None:             raise AttributeError("script_func has not been set")         if self.loaded:             if self.bulk_run.enabled:      ...*
- **Link:** [View in docs](./abstract_docs.md)

#### `active_background_color`

- **Occurrences:** 1
- **Context:** *...  hover_background_color: str = '#3c434c',         click_background_color: str = '#50565E',         active_background_color: str = 'rgba(0, 122, 255, 0.7)',         muted_background_color: str = 'rgba(0, 122, 255, 0.3)',   ...*
- **Link:** [View in docs](./abstract_docs.md)

#### `active_color`

- **Occurrences:** 1
- **Context:** *...(0, 122, 255, 0.3)',         border_color: str = '#3C434C',         color: str = '#d8d9db',         active_color: str = '#ececed'     ):         self.run_script(f'Lib.Handler.setRootStyles({js_json(locals())});')...*
- **Link:** [View in docs](./abstract_docs.md)

#### `add_script`

- **Occurrences:** 1
- **Context:** *...n set")         if self.loaded:             if self.bulk_run.enabled:                 self.bulk_run.add_script(script)             else:                 self.script_func(script)         elif run_last:          ...*
- **Link:** [View in docs](./abstract_docs.md)

#### `align_labels`

- **Occurrences:** 2
- **Context:** *...bool = True,         mode: PRICE_SCALE_MODE = 'normal',         invert_scale: bool = False,         align_labels: bool = True,         scale_margin_top: float = 0.2,         scale_margin_bottom: float = 0.2,     ...*
- **Link:** [View in docs](./abstract_docs.md)

#### `arrow_up`

- **Occurrences:** 1
- **Context:** *...tional[datetime] = None, position: MARKER_POSITION = 'below',                shape: MARKER_SHAPE = 'arrow_up', color: str = '#2196F3', text: str = ''                ) -> str:         """         Creates a new...*
- **Link:** [View in docs](./abstract_docs.md)

#### `as_enum`

- **Occurrences:** 8
- **Context:** *...VerticalSpan from .topbar import TopBar from .util import (     BulkRunScript, Pane, Events, IDGen, as_enum, jbool, js_json, TIME, NUM, FLOAT,     LINE_STYLE, MARKER_POSITION, MARKER_SHAPE, CROSSHAIR_MODE,  ...*
- **Link:** [View in docs](./abstract_docs.md)

#### `auto_scale`

- **Occurrences:** 2
- **Context:** *...ies['volume']         self.update(bar, _from_tick=True)      def price_scale(         self,         auto_scale: bool = True,         mode: PRICE_SCALE_MODE = 'normal',         invert_scale: bool = False,       ...*
- **Link:** [View in docs](./abstract_docs.md)

#### `axis_label_visible`

- **Occurrences:** 2
- **Context:** *...2, 146, 202)', width: int = 2,                         style: LINE_STYLE = 'solid', text: str = '', axis_label_visible: bool = True,                         func: Optional[Callable] = None                         ) -> ...*
- **Link:** [View in docs](./abstract_docs.md)

### B

#### `BulkRunScript`

- **Occurrences:** 2
- **Context:** *...ine, TwoPointDrawing, VerticalLine, VerticalSpan from .topbar import TopBar from .util import (     BulkRunScript, Pane, Events, IDGen, as_enum, jbool, js_json, TIME, NUM, FLOAT,     LINE_STYLE, MARKER_POSITION, M...*
- **Link:** [View in docs](./abstract_docs.md)

#### `background_color`

- **Occurrences:** 6
- **Context:** *... Optional[tuple] = None,         position: FLOAT = 'left',         draggable: bool = False,         background_color: str = '#121417',         border_color: str = 'rgb(70, 70, 70)',         border_width: int = 1,    ...*
- **Link:** [View in docs](./abstract_docs.md)

#### `border_color`

- **Occurrences:** 7
- **Context:** *...FLOAT = 'left',         draggable: bool = False,         background_color: str = '#121417',         border_color: str = 'rgb(70, 70, 70)',         border_width: int = 1,         heading_text_colors: Optional[tupl...*
- **Link:** [View in docs](./abstract_docs.md)

#### `border_down_color`

- **Occurrences:** 4
- **Context:** *...     wick_visible: bool = True, border_visible: bool = True, border_up_color: str = '',             border_down_color: str = '', wick_up_color: str = '', wick_down_color: str = ''):         """         Candle styling ...*
- **Link:** [View in docs](./abstract_docs.md)

#### `border_up_color`

- **Occurrences:** 4
- **Context:** *...tr = 'rgba(200, 97, 100, 100)',             wick_visible: bool = True, border_visible: bool = True, border_up_color: str = '',             border_down_color: str = '', wick_up_color: str = '', wick_down_color: str =...*
- **Link:** [View in docs](./abstract_docs.md)

#### `border_visible`

- **Occurrences:** 4
- **Context:** *...ol = True,         scale_margin_top: float = 0.2,         scale_margin_bottom: float = 0.2,         border_visible: bool = False,         border_color: Optional[str] = None,         text_color: Optional[str] = None...*
- **Link:** [View in docs](./abstract_docs.md)

#### `border_width`

- **Occurrences:** 2
- **Context:** *...,         background_color: str = '#121417',         border_color: str = 'rgb(70, 70, 70)',         border_width: int = 1,         heading_text_colors: Optional[tuple] = None,         heading_background_colors: O...*
- **Link:** [View in docs](./abstract_docs.md)

#### `bulk_run`

- **Occurrences:** 3
- **Context:** *...lf.script_func = script_func         self.scripts = []         self.final_scripts = []         self.bulk_run = BulkRunScript(script_func)          if run_script:             self.run_script = run_script      ...*
- **Link:** [View in docs](./abstract_docs.md)

### C

#### `CROSSHAIR_MODE`

- **Occurrences:** 3
- **Context:** *...s, IDGen, as_enum, jbool, js_json, TIME, NUM, FLOAT,     LINE_STYLE, MARKER_POSITION, MARKER_SHAPE, CROSSHAIR_MODE,     PRICE_SCALE_MODE, marker_position, marker_shape, js_data, )  current_dir = os.path.dirname(os....*
- **Link:** [View in docs](./abstract_docs.md)

#### `Candlestick`

- **Occurrences:** 3
- **Context:** *...   scaleMargins: {{top: {scale_margin_top}, bottom: {scale_margin_bottom}}}         }})''')   class Candlestick(SeriesCommon):     def __init__(self, chart: 'AbstractChart'):         super().__init__(chart)     ...*
- **Link:** [View in docs](./abstract_docs.md)

#### `candle_data`

- **Occurrences:** 7
- **Context:** *...or = 'rgba(83,141,131,0.8)'         self._volume_down_color = 'rgba(200,127,130,0.8)'          self.candle_data = pd.DataFrame()          # self.run_script(f'{self.id}.makeCandlestickSeries()')      def set(self...*
- **Link:** [View in docs](./abstract_docs.md)

#### `candle_style`

- **Occurrences:** 1
- **Context:** *... {jbool(ticks_visible)},                 minimumWidth: {minimum_width}             }})''')      def candle_style(             self, up_color: str = 'rgba(39, 157, 130, 100)', down_color: str = 'rgba(200, 97, 100,...*
- **Link:** [View in docs](./abstract_docs.md)

#### `clear_markers`

- **Occurrences:** 1
- **Context:** *...     text: str = ''     ) -> VerticalLine:         return VerticalLine(*locals().values())      def clear_markers(self):         """         Clears the markers displayed on the data.\n         """         self.mar...*
- **Link:** [View in docs](./abstract_docs.md)

#### `click_background_color`

- **Occurrences:** 1
- **Context:** *...        background_color: str = '#0c0d0f',         hover_background_color: str = '#3c434c',         click_background_color: str = '#50565E',         active_background_color: str = 'rgba(0, 122, 255, 0.7)',         muted_ba...*
- **Link:** [View in docs](./abstract_docs.md)

#### `color_based_on_candle`

- **Occurrences:** 2
- **Context:** *...b(191, 195, 203)', font_size: int = 11, font_family: str = 'Monaco',                text: str = '', color_based_on_candle: bool = False):         """         Configures the legend of the chart.         """         l_id = ...*
- **Link:** [View in docs](./abstract_docs.md)

#### `common_interval`

- **Occurrences:** 3
- **Context:** *...es.is_datetime64_any_dtype(df['time']):             df['time'] = pd.to_datetime(df['time'])         common_interval = df['time'].diff().value_counts()         if common_interval.empty:             return         sel...*
- **Link:** [View in docs](./abstract_docs.md)

#### `create_histogram`

- **Occurrences:** 1
- **Context:** *...or, style, width, price_line, price_label, price_scale_id))         return self._lines[-1]      def create_histogram(             self, name: str = '', color: str = 'rgba(214, 237, 255, 0.6)',             price_line:...*
- **Link:** [View in docs](./abstract_docs.md)

#### `create_line`

- **Occurrences:** 1
- **Context:** *...viewport.         """         self.run_script(f'{self.id}.chart.timeScale().fitContent()')      def create_line(             self, name: str = '', color: str = 'rgba(214, 237, 255, 0.6)',             style: LINE...*
- **Link:** [View in docs](./abstract_docs.md)

#### `create_subchart`

- **Occurrences:** 3
- **Context:** *...func: Optional[Callable] = None     ) -> 'Table':         return Table(*locals().values())      def create_subchart(         self,         position: FLOAT = 'left',         width: float = 0.5,         height: float ...*
- **Link:** [View in docs](./abstract_docs.md)

#### `create_table`

- **Occurrences:** 3
- **Context:** *...r):         self.run_script(f'_~_~RETURN~_~_{script}')         return self._return_q.get()      def create_table(         self,         width: NUM,         height: NUM,         headings: tuple,         widths: Op...*
- **Link:** [View in docs](./abstract_docs.md)

#### `crosshair_marker`

- **Occurrences:** 2
- **Context:** *... def __init__(self, chart, name, color, style, width, price_line, price_label, price_scale_id=None, crosshair_marker=True):          super().__init__(chart, name)         self.color = color          self.run_script(f...*
- **Link:** [View in docs](./abstract_docs.md)

#### `cumulative_volume`

- **Occurrences:** 3
- **Context:** *...elf.id}.volumeSeries.update({js_data(volume)})')      def update_from_tick(self, series: pd.Series, cumulative_volume: bool = False):         """         Updates the data from a tick.\n         :param series: labels: ...*
- **Link:** [View in docs](./abstract_docs.md)

#### `current_dir`

- **Occurrences:** 2
- **Context:** *...ION, MARKER_SHAPE, CROSSHAIR_MODE,     PRICE_SCALE_MODE, marker_position, marker_shape, js_data, )  current_dir = os.path.dirname(os.path.abspath(__file__)) INDEX = os.path.join(current_dir, 'js', 'index.html') ...*
- **Link:** [View in docs](./abstract_docs.md)

### D

#### `DataFrame`

- **Occurrences:** 8
- **Context:** *...      self.name = name         self.num_decimals = 2         self.offset = 0         self.data = pd.DataFrame()         self.markers = {}      def _set_interval(self, df: pd.DataFrame):         if not pd.api.t...*
- **Link:** [View in docs](./abstract_docs.md)

#### `down_color`

- **Occurrences:** 7
- **Context:** *...        }})''')      def candle_style(             self, up_color: str = 'rgba(39, 157, 130, 100)', down_color: str = 'rgba(200, 97, 100, 100)',             wick_visible: bool = True, border_visible: bool = Tru...*
- **Link:** [View in docs](./abstract_docs.md)

### E

#### `end_time`

- **Occurrences:** 16
- **Context:** *...unc)      def trend_line(         self,         start_time: TIME,         start_value: NUM,         end_time: TIME,         end_value: NUM,         round: bool = False,         line_color: str = '#1E80F0',   ...*
- **Link:** [View in docs](./abstract_docs.md)

#### `end_value`

- **Occurrences:** 4
- **Context:** *...(         self,         start_time: TIME,         start_value: NUM,         end_time: TIME,         end_value: NUM,         round: bool = False,         line_color: str = '#1E80F0',         width: int = 2,    ...*
- **Link:** [View in docs](./abstract_docs.md)

#### `entire_text_only`

- **Occurrences:** 2
- **Context:** *...alse,         border_color: Optional[str] = None,         text_color: Optional[str] = None,         entire_text_only: bool = False,         visible: bool = True,         ticks_visible: bool = False,         minimum_w...*
- **Link:** [View in docs](./abstract_docs.md)

#### `exclude_lowercase`

- **Occurrences:** 10
- **Context:** *...elf.offset = value             break      @staticmethod     def _format_labels(data, labels, index, exclude_lowercase):         def rename(la, mapper):             return [mapper[key] if key in mapper else key for key...*
- **Link:** [View in docs](./abstract_docs.md)

### F

#### `FLOAT`

- **Occurrences:** 6
- **Context:** *...Bar from .util import (     BulkRunScript, Pane, Events, IDGen, as_enum, jbool, js_json, TIME, NUM, FLOAT,     LINE_STYLE, MARKER_POSITION, MARKER_SHAPE, CROSSHAIR_MODE,     PRICE_SCALE_MODE, marker_positi...*
- **Link:** [View in docs](./abstract_docs.md)

#### `fill_color`

- **Occurrences:** 1
- **Context:** *... TIME,         end_value: NUM,         round: bool = False,         color: str = '#1E80F0',         fill_color: str = 'rgba(255, 255, 255, 0.2)',         width: int = 2,         style: LINE_STYLE = 'solid',    ...*
- **Link:** [View in docs](./abstract_docs.md)

#### `final_scripts`

- **Occurrences:** 3
- **Context:** *...  self.loaded = False         self.script_func = script_func         self.scripts = []         self.final_scripts = []         self.bulk_run = BulkRunScript(script_func)          if run_script:             self.ru...*
- **Link:** [View in docs](./abstract_docs.md)

#### `font_family`

- **Occurrences:** 5
- **Context:** *... str = '#000000', text_color: Optional[str] = None,                font_size: Optional[int] = None, font_family: Optional[str] = None):         """         Global layout options for the chart.         """       ...*
- **Link:** [View in docs](./abstract_docs.md)

#### `font_size`

- **Occurrences:** 6
- **Context:** *...ef layout(self, background_color: str = '#000000', text_color: Optional[str] = None,                font_size: Optional[int] = None, font_family: Optional[str] = None):         """         Global layout option...*
- **Link:** [View in docs](./abstract_docs.md)

#### `format_cols`

- **Occurrences:** 3
- **Context:** *...elf._interval)+self.offset         return arg      def set(self, df: Optional[pd.DataFrame] = None, format_cols: bool = True):         if df is None or df.empty:             self.run_script(f'{self.id}.series.se...*
- **Link:** [View in docs](./abstract_docs.md)

#### `formatted_time`

- **Occurrences:** 2
- **Context:** *...with the marker.         :return: The id of the marker placed.         """         try:             formatted_time = self._last_bar['time'] if not time else self._single_datetime_format(time)         except TypeErr...*
- **Link:** [View in docs](./abstract_docs.md)

### H

#### `Histogram`

- **Occurrences:** 4
- **Context:** *...d}.series)             delete {self.id}legendItem             delete {self.id}         ''')   class Histogram(SeriesCommon):     def __init__(self, chart, name, color, price_line, price_label, scale_margin_top...*
- **Link:** [View in docs](./abstract_docs.md)

#### `HorizontalLine`

- **Occurrences:** 3
- **Context:** *...port pandas as pd  from .table import Table from .toolbox import ToolBox from .drawings import Box, HorizontalLine, RayLine, TrendLine, TwoPointDrawing, VerticalLine, VerticalSpan from .topbar import TopBar from .u...*
- **Link:** [View in docs](./abstract_docs.md)

#### `heading_background_colors`

- **Occurrences:** 2
- **Context:** *..., 70)',         border_width: int = 1,         heading_text_colors: Optional[tuple] = None,         heading_background_colors: Optional[tuple] = None,         return_clicked_cells: bool = False,         func: Optional[Callabl...*
- **Link:** [View in docs](./abstract_docs.md)

#### `heading_text_colors`

- **Occurrences:** 2
- **Context:** *... = '#121417',         border_color: str = 'rgb(70, 70, 70)',         border_width: int = 1,         heading_text_colors: Optional[tuple] = None,         heading_background_colors: Optional[tuple] = None,         return_...*
- **Link:** [View in docs](./abstract_docs.md)

#### `hide_data`

- **Occurrences:** 1
- **Context:** *...: {precision}, minMove: {min_move}}}         }})''')         self.num_decimals = precision      def hide_data(self):         self._toggle_data(False)      def show_data(self):         self._toggle_data(True)  ...*
- **Link:** [View in docs](./abstract_docs.md)

#### `horizontal_line`

- **Occurrences:** 1
- **Context:** *...given id.\n         """         self.markers.pop(marker_id)         self._update_markers()      def horizontal_line(self, price: NUM, color: str = 'rgb(122, 146, 202)', width: int = 2,                         style:...*
- **Link:** [View in docs](./abstract_docs.md)

#### `horz_color`

- **Occurrences:** 3
- **Context:** *...r: str = 'rgb(46, 46, 46)',         horz_visible: bool = True,         horz_width: int = 1,         horz_color: Optional[str] = None,         horz_style: LINE_STYLE = 'large_dashed',         horz_label_backgrou...*
- **Link:** [View in docs](./abstract_docs.md)

#### `horz_enabled`

- **Occurrences:** 2
- **Context:** *...ly}",' if font_family else ''}             }}}})""")      def grid(self, vert_enabled: bool = True, horz_enabled: bool = True,              color: str = 'rgba(29, 30, 38, 5)', style: LINE_STYLE = 'solid'):       ...*
- **Link:** [View in docs](./abstract_docs.md)

#### `horz_label_background_color`

- **Occurrences:** 2
- **Context:** *...         horz_color: Optional[str] = None,         horz_style: LINE_STYLE = 'large_dashed',         horz_label_background_color: str = 'rgb(55, 55, 55)'     ):         """         Crosshair formatting for its vertical and horiz...*
- **Link:** [View in docs](./abstract_docs.md)

#### `horz_style`

- **Occurrences:** 2
- **Context:** *...isible: bool = True,         horz_width: int = 1,         horz_color: Optional[str] = None,         horz_style: LINE_STYLE = 'large_dashed',         horz_label_background_color: str = 'rgb(55, 55, 55)'     ):  ...*
- **Link:** [View in docs](./abstract_docs.md)

#### `horz_visible`

- **Occurrences:** 2
- **Context:** *... LINE_STYLE = 'large_dashed',         vert_label_background_color: str = 'rgb(46, 46, 46)',         horz_visible: bool = True,         horz_width: int = 1,         horz_color: Optional[str] = None,         horz_s...*
- **Link:** [View in docs](./abstract_docs.md)

#### `horz_width`

- **Occurrences:** 2
- **Context:** *...   vert_label_background_color: str = 'rgb(46, 46, 46)',         horz_visible: bool = True,         horz_width: int = 1,         horz_color: Optional[str] = None,         horz_style: LINE_STYLE = 'large_dashed'...*
- **Link:** [View in docs](./abstract_docs.md)

#### `hover_background_color`

- **Occurrences:** 1
- **Context:** *...   return subchart      def style(         self,         background_color: str = '#0c0d0f',         hover_background_color: str = '#3c434c',         click_background_color: str = '#50565E',         active_background_color:...*
- **Link:** [View in docs](./abstract_docs.md)

### I

#### `INDEX`

- **Occurrences:** 1
- **Context:** *...marker_position, marker_shape, js_data, )  current_dir = os.path.dirname(os.path.abspath(__file__)) INDEX = os.path.join(current_dir, 'js', 'index.html')   class Window:     _id_gen = IDGen()     handlers ...*
- **Link:** [View in docs](./abstract_docs.md)

#### `ignore_index`

- **Occurrences:** 2
- **Context:** *...ata.index[-1]] = self._last_bar             self.data = pd.concat([self.data, series.to_frame().T], ignore_index=True)         self._last_bar = series         self.run_script(f'{self.id}.series.update({js_data(se...*
- **Link:** [View in docs](./abstract_docs.md)

#### `initial_script`

- **Occurrences:** 3
- **Context:** *...d_get('document.readyState == "complete"'):                 continue    # scary, but works          initial_script = ''         self.scripts.extend(self.final_scripts)         for script in self.scripts:           ...*
- **Link:** [View in docs](./abstract_docs.md)

#### `invert_scale`

- **Occurrences:** 2
- **Context:** *...(         self,         auto_scale: bool = True,         mode: PRICE_SCALE_MODE = 'normal',         invert_scale: bool = False,         align_labels: bool = True,         scale_margin_top: float = 0.2,         sc...*
- **Link:** [View in docs](./abstract_docs.md)

### J

#### `JavaScript`

- **Occurrences:** 1
- **Context:** *...cript(self, script: str, run_last: bool = False):         """         For advanced users; evaluates JavaScript within the Webview.         """         if self.script_func is None:             raise AttributeErr...*
- **Link:** [View in docs](./abstract_docs.md)

#### `js_api_code`

- **Occurrences:** 3
- **Context:** *...dlers = {}      def __init__(         self,         script_func: Optional[Callable] = None,         js_api_code: Optional[str] = None,         run_script: Optional[Callable] = None     ):         self.loaded = F...*
- **Link:** [View in docs](./abstract_docs.md)

#### `js_data`

- **Occurrences:** 7
- **Context:** *...MARKER_POSITION, MARKER_SHAPE, CROSSHAIR_MODE,     PRICE_SCALE_MODE, marker_position, marker_shape, js_data, )  current_dir = os.path.dirname(os.path.abspath(__file__)) INDEX = os.path.join(current_dir, 'js'...*
- **Link:** [View in docs](./abstract_docs.md)

#### `js_json`

- **Occurrences:** 5
- **Context:** *...m .topbar import TopBar from .util import (     BulkRunScript, Pane, Events, IDGen, as_enum, jbool, js_json, TIME, NUM, FLOAT,     LINE_STYLE, MARKER_POSITION, MARKER_SHAPE, CROSSHAIR_MODE,     PRICE_SCALE_M...*
- **Link:** [View in docs](./abstract_docs.md)

### K

#### `keep_drawings`

- **Occurrences:** 3
- **Context:** *..._script(f'{self.id}.makeCandlestickSeries()')      def set(self, df: Optional[pd.DataFrame] = None, keep_drawings=False):         """         Sets the initial data for the chart.\n         :param df: columns: date...*
- **Link:** [View in docs](./abstract_docs.md)

#### `key_code`

- **Occurrences:** 2
- **Context:** *...in keys:             key = str(key)             if key.isalnum() and len(key) == 1:                 key_code = f'Digit{key}' if key.isdigit() else f'Key{key.upper()}'                 key_condition = f'event.c...*
- **Link:** [View in docs](./abstract_docs.md)

#### `key_condition`

- **Occurrences:** 4
- **Context:** *...                 key_code = f'Digit{key}' if key.isdigit() else f'Key{key.upper()}'                 key_condition = f'event.code === "{key_code}"'             else:                 key_condition = f'event.key === ...*
- **Link:** [View in docs](./abstract_docs.md)

### L

#### `LINE_STYLE`

- **Occurrences:** 15
- **Context:** *...til import (     BulkRunScript, Pane, Events, IDGen, as_enum, jbool, js_json, TIME, NUM, FLOAT,     LINE_STYLE, MARKER_POSITION, MARKER_SHAPE, CROSSHAIR_MODE,     PRICE_SCALE_MODE, marker_position, marker_shape...*
- **Link:** [View in docs](./abstract_docs.md)

#### `Line`

- **Occurrences:** 5
- **Context:** *..._time) if end_time else None         return VerticalSpan(self, start_time, end_time, color)   class Line(SeriesCommon):     def __init__(self, chart, name, color, style, width, price_line, price_label, pr...*
- **Link:** [View in docs](./abstract_docs.md)

#### `l_id`

- **Occurrences:** 15
- **Context:** *..._candle: bool = False):         """         Configures the legend of the chart.         """         l_id = f'{self.id}.legend'         if not visible:             self.run_script(f'''             {l_id}.d...*
- **Link:** [View in docs](./abstract_docs.md)

#### `label_visible`

- **Occurrences:** 2
- **Context:** *...n         """         self.markers.clear()         self._update_markers()      def price_line(self, label_visible: bool = True, line_visible: bool = True, title: str = ''):         self.run_script(f'''         {se...*
- **Link:** [View in docs](./abstract_docs.md)

#### `large_dashed`

- **Occurrences:** 2
- **Context:** *...   vert_width: int = 1,         vert_color: Optional[str] = None,         vert_style: LINE_STYLE = 'large_dashed',         vert_label_background_color: str = 'rgb(46, 46, 46)',         horz_visible: bool = True, ...*
- **Link:** [View in docs](./abstract_docs.md)

#### `lightweight_charts`

- **Occurrences:** 1
- **Context:** *...idth = width         self._height = height         self.events: Events = Events(self)          from lightweight_charts.polygon import PolygonAPI         self.polygon: PolygonAPI = PolygonAPI(self)          self.run_scr...*
- **Link:** [View in docs](./abstract_docs.md)

#### `line_color`

- **Occurrences:** 1
- **Context:** *...rt_value: NUM,         end_time: TIME,         end_value: NUM,         round: bool = False,         line_color: str = '#1E80F0',         width: int = 2,         style: LINE_STYLE = 'solid',     ) -> TwoPointDra...*
- **Link:** [View in docs](./abstract_docs.md)

#### `line_visible`

- **Occurrences:** 2
- **Context:** *...arkers.clear()         self._update_markers()      def price_line(self, label_visible: bool = True, line_visible: bool = True, title: str = ''):         self.run_script(f'''         {self.id}.series.applyOptions(...*
- **Link:** [View in docs](./abstract_docs.md)

### M

#### `MARKER_POSITION`

- **Occurrences:** 2
- **Context:** *...     BulkRunScript, Pane, Events, IDGen, as_enum, jbool, js_json, TIME, NUM, FLOAT,     LINE_STYLE, MARKER_POSITION, MARKER_SHAPE, CROSSHAIR_MODE,     PRICE_SCALE_MODE, marker_position, marker_shape, js_data, )  cur...*
- **Link:** [View in docs](./abstract_docs.md)

#### `MARKER_SHAPE`

- **Occurrences:** 2
- **Context:** *...t, Pane, Events, IDGen, as_enum, jbool, js_json, TIME, NUM, FLOAT,     LINE_STYLE, MARKER_POSITION, MARKER_SHAPE, CROSSHAIR_MODE,     PRICE_SCALE_MODE, marker_position, marker_shape, js_data, )  current_dir = os....*
- **Link:** [View in docs](./abstract_docs.md)

#### `marker_id`

- **Occurrences:** 8
- **Context:** *...        markers = markers.copy()         marker_ids = []         for marker in markers:             marker_id = self.win._id_gen.generate()             self.markers[marker_id] = {                 "time": self....*
- **Link:** [View in docs](./abstract_docs.md)

#### `marker_ids`

- **Occurrences:** 3
- **Context:** *...      ]         :return: a list of marker ids.         """         markers = markers.copy()         marker_ids = []         for marker in markers:             marker_id = self.win._id_gen.generate()            ...*
- **Link:** [View in docs](./abstract_docs.md)

#### `marker_list`

- **Occurrences:** 1
- **Context:** *...self.run_script(f'{self.id}.series.setMarkers({json.dumps(list(self.markers.values()))})')      def marker_list(self, markers: list):         """         Creates multiple markers.\n         :param markers: The l...*
- **Link:** [View in docs](./abstract_docs.md)

#### `marker_position`

- **Occurrences:** 3
- **Context:** *...E, NUM, FLOAT,     LINE_STYLE, MARKER_POSITION, MARKER_SHAPE, CROSSHAIR_MODE,     PRICE_SCALE_MODE, marker_position, marker_shape, js_data, )  current_dir = os.path.dirname(os.path.abspath(__file__)) INDEX = os.path...*
- **Link:** [View in docs](./abstract_docs.md)

#### `marker_shape`

- **Occurrences:** 3
- **Context:** *...  LINE_STYLE, MARKER_POSITION, MARKER_SHAPE, CROSSHAIR_MODE,     PRICE_SCALE_MODE, marker_position, marker_shape, js_data, )  current_dir = os.path.dirname(os.path.abspath(__file__)) INDEX = os.path.join(current_...*
- **Link:** [View in docs](./abstract_docs.md)

#### `min_bar_spacing`

- **Occurrences:** 1
- **Context:** *...f._height}         {self.id}.reSize()         ''')      def time_scale(self, right_offset: int = 0, min_bar_spacing: float = 0.5,                    visible: bool = True, time_visible: bool = True, seconds_visible: ...*
- **Link:** [View in docs](./abstract_docs.md)

#### `min_move`

- **Occurrences:** 2
- **Context:** *...recision and minMove.\n         :param precision: The number of decimal places.         """         min_move = 1 / (10**precision)         self.run_script(f'''         {self.id}.series.applyOptions({{        ...*
- **Link:** [View in docs](./abstract_docs.md)

#### `minimum_width`

- **Occurrences:** 2
- **Context:** *...text_only: bool = False,         visible: bool = True,         ticks_visible: bool = False,         minimum_width: int = 0     ):         self.run_script(f'''             {self.id}.series.priceScale().applyOptions...*
- **Link:** [View in docs](./abstract_docs.md)

#### `modifier_key`

- **Occurrences:** 5
- **Context:** *...ript(f"{self.id}.spinner.style.display = '{'block' if visible else 'none'}'")      def hotkey(self, modifier_key: Literal['ctrl', 'alt', 'shift', 'meta', None],                keys: Union[str, tuple, int], func: ...*
- **Link:** [View in docs](./abstract_docs.md)

#### `muted_background_color`

- **Occurrences:** 1
- **Context:** *...nd_color: str = '#50565E',         active_background_color: str = 'rgba(0, 122, 255, 0.7)',         muted_background_color: str = 'rgba(0, 122, 255, 0.3)',         border_color: str = '#3C434C',         color: str = '#d8d9...*
- **Link:** [View in docs](./abstract_docs.md)

### N

#### `NUM`

- **Occurrences:** 11
- **Context:** *...t TopBar from .util import (     BulkRunScript, Pane, Events, IDGen, as_enum, jbool, js_json, TIME, NUM, FLOAT,     LINE_STYLE, MARKER_POSITION, MARKER_SHAPE, CROSSHAIR_MODE,     PRICE_SCALE_MODE, marker...*
- **Link:** [View in docs](./abstract_docs.md)

#### `NameError`

- **Occurrences:** 1
- **Context:** *...owercase=self.name)         if self.name:             if self.name not in df:                 raise NameError(f'No column named "{self.name}".')             df = df.rename(columns={self.name: 'value'})        ...*
- **Link:** [View in docs](./abstract_docs.md)

#### `new_bar`

- **Occurrences:** 1
- **Context:** *...d.concat([self.candle_data, series.to_frame().T], ignore_index=True)             self._chart.events.new_bar._emit(self)          self._last_bar = series         self.run_script(f'{self.id}.series.update({js_...*
- **Link:** [View in docs](./abstract_docs.md)

#### `num_decimals`

- **Occurrences:** 2
- **Context:** *...             self._interval = 1         self._last_bar = None         self.name = name         self.num_decimals = 2         self.offset = 0         self.data = pd.DataFrame()         self.markers = {}      def _...*
- **Link:** [View in docs](./abstract_docs.md)

### O

#### `on_js_load`

- **Occurrences:** 1
- **Context:** *...   if js_api_code:             self.run_script(f'window.callbackFunction = {js_api_code}')      def on_js_load(self):         if self.loaded:             return         self.loaded = True          if hasattr(se...*
- **Link:** [View in docs](./abstract_docs.md)

### P

#### `PRICE_SCALE_MODE`

- **Occurrences:** 3
- **Context:** *...bool, js_json, TIME, NUM, FLOAT,     LINE_STYLE, MARKER_POSITION, MARKER_SHAPE, CROSSHAIR_MODE,     PRICE_SCALE_MODE, marker_position, marker_shape, js_data, )  current_dir = os.path.dirname(os.path.abspath(__file__)...*
- **Link:** [View in docs](./abstract_docs.md)

#### `price_label`

- **Occurrences:** 8
- **Context:** *...r)   class Line(SeriesCommon):     def __init__(self, chart, name, color, style, width, price_line, price_label, price_scale_id=None, crosshair_marker=True):          super().__init__(chart, name)         self.c...*
- **Link:** [View in docs](./abstract_docs.md)

#### `price_line`

- **Occurrences:** 9
- **Context:** *...yed on the data.\n         """         self.markers.clear()         self._update_markers()      def price_line(self, label_visible: bool = True, line_visible: bool = True, title: str = ''):         self.run_scr...*
- **Link:** [View in docs](./abstract_docs.md)

#### `price_scale`

- **Occurrences:** 1
- **Context:** *...                bar['volume'] = series['volume']         self.update(bar, _from_tick=True)      def price_scale(         self,         auto_scale: bool = True,         mode: PRICE_SCALE_MODE = 'normal',         ...*
- **Link:** [View in docs](./abstract_docs.md)

#### `price_scale_id`

- **Occurrences:** 5
- **Context:** *...ne(SeriesCommon):     def __init__(self, chart, name, color, style, width, price_line, price_label, price_scale_id=None, crosshair_marker=True):          super().__init__(chart, name)         self.color = color    ...*
- **Link:** [View in docs](./abstract_docs.md)

### R

#### `RETURN`

- **Occurrences:** 1
- **Context:** *...cripts.append(script)      def run_script_and_get(self, script: str):         self.run_script(f'_~_~RETURN~_~_{script}')         return self._return_q.get()      def create_table(         self,         widt...*
- **Link:** [View in docs](./abstract_docs.md)

#### `RayLine`

- **Occurrences:** 3
- **Context:** *...d  from .table import Table from .toolbox import ToolBox from .drawings import Box, HorizontalLine, RayLine, TrendLine, TwoPointDrawing, VerticalLine, VerticalSpan from .topbar import TopBar from .util impor...*
- **Link:** [View in docs](./abstract_docs.md)

#### `ray_line`

- **Occurrences:** 1
- **Context:** *...le: LINE_STYLE = 'solid',     ) -> TwoPointDrawing:         return Box(*locals().values())      def ray_line(         self,         start_time: TIME,         value: NUM,         round: bool = False,         c...*
- **Link:** [View in docs](./abstract_docs.md)

#### `remove_marker`

- **Occurrences:** 1
- **Context:** *...           "text": text,         }         self._update_markers()         return marker_id      def remove_marker(self, marker_id: str):         """         Removes the marker with the given id.\n         """     ...*
- **Link:** [View in docs](./abstract_docs.md)

#### `return_clicked_cells`

- **Occurrences:** 2
- **Context:** *..._colors: Optional[tuple] = None,         heading_background_colors: Optional[tuple] = None,         return_clicked_cells: bool = False,         func: Optional[Callable] = None     ) -> 'Table':         return Table(*loca...*
- **Link:** [View in docs](./abstract_docs.md)

#### `right_offset`

- **Occurrences:** 1
- **Context:** *...id}.scale.height = {self._height}         {self.id}.reSize()         ''')      def time_scale(self, right_offset: int = 0, min_bar_spacing: float = 0.5,                    visible: bool = True, time_visible: bool...*
- **Link:** [View in docs](./abstract_docs.md)

#### `run_last`

- **Occurrences:** 3
- **Context:** *...pt += f'\n{script}'         self.script_func(initial_script)      def run_script(self, script: str, run_last: bool = False):         """         For advanced users; evaluates JavaScript within the Webview.   ...*
- **Link:** [View in docs](./abstract_docs.md)

#### `run_script`

- **Occurrences:** 48
- **Context:** *...         script_func: Optional[Callable] = None,         js_api_code: Optional[str] = None,         run_script: Optional[Callable] = None     ):         self.loaded = False         self.script_func = script_fun...*
- **Link:** [View in docs](./abstract_docs.md)

#### `run_script_and_get`

- **Occurrences:** 3
- **Context:** *...eturn         self.loaded = True          if hasattr(self, '_return_q'):             while not self.run_script_and_get('document.readyState == "complete"'):                 continue    # scary, but works          initi...*
- **Link:** [View in docs](./abstract_docs.md)

### S

#### `SeriesCommon`

- **Occurrences:** 4
- **Context:** *...#ececed'     ):         self.run_script(f'Lib.Handler.setRootStyles({js_json(locals())});')   class SeriesCommon(Pane):     def __init__(self, chart: 'AbstractChart', name: str = ''):         super().__init__(cha...*
- **Link:** [View in docs](./abstract_docs.md)

#### `scale_candles_only`

- **Occurrences:** 5
- **Context:** *...    width: float = 0.5,         height: float = 0.5,         sync_id: Optional[str] = None,         scale_candles_only: bool = False,         sync_crosshairs_only: bool = False,         toolbox: bool = False     ) -> '...*
- **Link:** [View in docs](./abstract_docs.md)

#### `scale_margin_bottom`

- **Occurrences:** 10
- **Context:** *...eriesCommon):     def __init__(self, chart, name, color, price_line, price_label, scale_margin_top, scale_margin_bottom):         super().__init__(chart, name)         self.color = color         self.run_script(f'''    ...*
- **Link:** [View in docs](./abstract_docs.md)

#### `scale_margin_top`

- **Occurrences:** 10
- **Context:** *... class Histogram(SeriesCommon):     def __init__(self, chart, name, color, price_line, price_label, scale_margin_top, scale_margin_bottom):         super().__init__(chart, name)         self.color = color         sel...*
- **Link:** [View in docs](./abstract_docs.md)

#### `script_func`

- **Occurrences:** 8
- **Context:** *...')   class Window:     _id_gen = IDGen()     handlers = {}      def __init__(         self,         script_func: Optional[Callable] = None,         js_api_code: Optional[str] = None,         run_script: Optional...*
- **Link:** [View in docs](./abstract_docs.md)

#### `seconds_visible`

- **Occurrences:** 1
- **Context:** *..., min_bar_spacing: float = 0.5,                    visible: bool = True, time_visible: bool = True, seconds_visible: bool = False,                    border_visible: bool = True, border_color: Optional[str] = None):...*
- **Link:** [View in docs](./abstract_docs.md)

#### `serial_data`

- **Occurrences:** 2
- **Context:** *... visible.         :return: a bytes object containing a screenshot of the chart.         """         serial_data = self.win.run_script_and_get(f'{self.id}.chart.takeScreenshot().toDataURL()')         return b64de...*
- **Link:** [View in docs](./abstract_docs.md)

#### `set_visible_range`

- **Occurrences:** 1
- **Context:** *..."""         Returns all lines for the chart.         """         return self._lines.copy()      def set_visible_range(self, start_time: TIME, end_time: TIME):         self.run_script(f'''         {self.id}.chart.timeS...*
- **Link:** [View in docs](./abstract_docs.md)

#### `show_data`

- **Occurrences:** 1
- **Context:** *...  self.num_decimals = precision      def hide_data(self):         self._toggle_data(False)      def show_data(self):         self._toggle_data(True)      def _toggle_data(self, arg):         self.run_script(f'...*
- **Link:** [View in docs](./abstract_docs.md)

#### `start_time`

- **Occurrences:** 16
- **Context:** *...ce, color, width, style, text, axis_label_visible, func)      def trend_line(         self,         start_time: TIME,         start_value: NUM,         end_time: TIME,         end_value: NUM,         round: boo...*
- **Link:** [View in docs](./abstract_docs.md)

#### `start_value`

- **Occurrences:** 4
- **Context:** *...ext, axis_label_visible, func)      def trend_line(         self,         start_time: TIME,         start_value: NUM,         end_time: TIME,         end_value: NUM,         round: bool = False,         line_col...*
- **Link:** [View in docs](./abstract_docs.md)

#### `sync_crosshairs_only`

- **Occurrences:** 3
- **Context:** *...oat = 0.5,         sync_id: Optional[str] = None,         scale_candles_only: bool = False,         sync_crosshairs_only: bool = False,         toolbox: bool = False     ) -> 'AbstractChart':         subchart = AbstractC...*
- **Link:** [View in docs](./abstract_docs.md)

#### `sync_id`

- **Occurrences:** 3
- **Context:** *...         position: FLOAT = 'left',         width: float = 0.5,         height: float = 0.5,         sync_id: Optional[str] = None,         scale_candles_only: bool = False,         sync_crosshairs_only: bool...*
- **Link:** [View in docs](./abstract_docs.md)

### T

#### `TIME`

- **Occurrences:** 11
- **Context:** *... import TopBar from .util import (     BulkRunScript, Pane, Events, IDGen, as_enum, jbool, js_json, TIME, NUM, FLOAT,     LINE_STYLE, MARKER_POSITION, MARKER_SHAPE, CROSSHAIR_MODE,     PRICE_SCALE_MODE, m...*
- **Link:** [View in docs](./abstract_docs.md)

#### `TODO`

- **Occurrences:** 2
- **Context:** *...width: int = 2,         style: LINE_STYLE = 'solid',         text: str = ''     ) -> RayLine:     # TODO         return RayLine(*locals().values())      def vertical_line(         self,         time: TIME...*
- **Link:** [View in docs](./abstract_docs.md)

#### `ToolBox`

- **Occurrences:** 3
- **Context:** *..., Union, Literal, List, Optional import pandas as pd  from .table import Table from .toolbox import ToolBox from .drawings import Box, HorizontalLine, RayLine, TrendLine, TwoPointDrawing, VerticalLine, Verti...*
- **Link:** [View in docs](./abstract_docs.md)

#### `TopBar`

- **Occurrences:** 3
- **Context:** *...HorizontalLine, RayLine, TrendLine, TwoPointDrawing, VerticalLine, VerticalSpan from .topbar import TopBar from .util import (     BulkRunScript, Pane, Events, IDGen, as_enum, jbool, js_json, TIME, NUM, FLO...*
- **Link:** [View in docs](./abstract_docs.md)

#### `TrendLine`

- **Occurrences:** 2
- **Context:** *...table import Table from .toolbox import ToolBox from .drawings import Box, HorizontalLine, RayLine, TrendLine, TwoPointDrawing, VerticalLine, VerticalSpan from .topbar import TopBar from .util import (     Bul...*
- **Link:** [View in docs](./abstract_docs.md)

#### `TwoPointDrawing`

- **Occurrences:** 3
- **Context:** *...t Table from .toolbox import ToolBox from .drawings import Box, HorizontalLine, RayLine, TrendLine, TwoPointDrawing, VerticalLine, VerticalSpan from .topbar import TopBar from .util import (     BulkRunScript, Pane,...*
- **Link:** [View in docs](./abstract_docs.md)

#### `TypeError`

- **Occurrences:** 2
- **Context:** *...ed_time = self._last_bar['time'] if not time else self._single_datetime_format(time)         except TypeError:             raise TypeError('Chart marker created before data was set.')         marker_id = self....*
- **Link:** [View in docs](./abstract_docs.md)

#### `text_color`

- **Occurrences:** 6
- **Context:** *...at = 0.2,         border_visible: bool = False,         border_color: Optional[str] = None,         text_color: Optional[str] = None,         entire_text_only: bool = False,         visible: bool = True,       ...*
- **Link:** [View in docs](./abstract_docs.md)

#### `ticks_visible`

- **Occurrences:** 2
- **Context:** *...Optional[str] = None,         entire_text_only: bool = False,         visible: bool = True,         ticks_visible: bool = False,         minimum_width: int = 0     ):         self.run_script(f'''             {self...*
- **Link:** [View in docs](./abstract_docs.md)

#### `time_scale`

- **Occurrences:** 1
- **Context:** *...h}         {self.id}.scale.height = {self._height}         {self.id}.reSize()         ''')      def time_scale(self, right_offset: int = 0, min_bar_spacing: float = 0.5,                    visible: bool = True,...*
- **Link:** [View in docs](./abstract_docs.md)

#### `time_visible`

- **Occurrences:** 1
- **Context:** *...self, right_offset: int = 0, min_bar_spacing: float = 0.5,                    visible: bool = True, time_visible: bool = True, seconds_visible: bool = False,                    border_visible: bool = True, border...*
- **Link:** [View in docs](./abstract_docs.md)

#### `to_datetime`

- **Occurrences:** 9
- **Context:** *...rame):         if not pd.api.types.is_datetime64_any_dtype(df['time']):             df['time'] = pd.to_datetime(df['time'])         common_interval = df['time'].diff().value_counts()         if common_interval.e...*
- **Link:** [View in docs](./abstract_docs.md)

#### `to_frame`

- **Occurrences:** 2
- **Context:** *...data.loc[self.data.index[-1]] = self._last_bar             self.data = pd.concat([self.data, series.to_frame().T], ignore_index=True)         self._last_bar = series         self.run_script(f'{self.id}.series...*
- **Link:** [View in docs](./abstract_docs.md)

#### `total_seconds`

- **Occurrences:** 2
- **Context:** *...     if common_interval.empty:             return         self._interval = common_interval.index[0].total_seconds()          units = [             pd.Timedelta(microseconds=df['time'].dt.microsecond.value_counts()...*
- **Link:** [View in docs](./abstract_docs.md)

#### `trend_line`

- **Occurrences:** 1
- **Context:** *...   return HorizontalLine(self, price, color, width, style, text, axis_label_visible, func)      def trend_line(         self,         start_time: TIME,         start_value: NUM,         end_time: TIME,         ...*
- **Link:** [View in docs](./abstract_docs.md)

### U

#### `up_color`

- **Occurrences:** 7
- **Context:** *...         minimumWidth: {minimum_width}             }})''')      def candle_style(             self, up_color: str = 'rgba(39, 157, 130, 100)', down_color: str = 'rgba(200, 97, 100, 100)',             wick_vis...*
- **Link:** [View in docs](./abstract_docs.md)

#### `update_from_tick`

- **Occurrences:** 1
- **Context:** *...me_down_color         self.run_script(f'{self.id}.volumeSeries.update({js_data(volume)})')      def update_from_tick(self, series: pd.Series, cumulative_volume: bool = False):         """         Updates the data fro...*
- **Link:** [View in docs](./abstract_docs.md)

### V

#### `ValueError`

- **Occurrences:** 2
- **Context:** *...type(arg):             try:                 arg = pd.to_datetime(arg, unit='ms')             except ValueError:                 arg = pd.to_datetime(arg)         arg = self._interval * (arg.timestamp() // self....*
- **Link:** [View in docs](./abstract_docs.md)

#### `VerticalLine`

- **Occurrences:** 3
- **Context:** *...lbox import ToolBox from .drawings import Box, HorizontalLine, RayLine, TrendLine, TwoPointDrawing, VerticalLine, VerticalSpan from .topbar import TopBar from .util import (     BulkRunScript, Pane, Events, IDGen...*
- **Link:** [View in docs](./abstract_docs.md)

#### `VerticalSpan`

- **Occurrences:** 2
- **Context:** *...olBox from .drawings import Box, HorizontalLine, RayLine, TrendLine, TwoPointDrawing, VerticalLine, VerticalSpan from .topbar import TopBar from .util import (     BulkRunScript, Pane, Events, IDGen, as_enum, jbo...*
- **Link:** [View in docs](./abstract_docs.md)

#### `value_counts`

- **Occurrences:** 6
- **Context:** *...]):             df['time'] = pd.to_datetime(df['time'])         common_interval = df['time'].diff().value_counts()         if common_interval.empty:             return         self._interval = common_interval.ind...*
- **Link:** [View in docs](./abstract_docs.md)

#### `vert_color`

- **Occurrences:** 3
- **Context:** *... CROSSHAIR_MODE = 'normal',         vert_visible: bool = True,         vert_width: int = 1,         vert_color: Optional[str] = None,         vert_style: LINE_STYLE = 'large_dashed',         vert_label_backgrou...*
- **Link:** [View in docs](./abstract_docs.md)

#### `vert_enabled`

- **Occurrences:** 2
- **Context:** *... {f'fontFamily: "{font_family}",' if font_family else ''}             }}}})""")      def grid(self, vert_enabled: bool = True, horz_enabled: bool = True,              color: str = 'rgba(29, 30, 38, 5)', style: LI...*
- **Link:** [View in docs](./abstract_docs.md)

#### `vert_label_background_color`

- **Occurrences:** 2
- **Context:** *...         vert_color: Optional[str] = None,         vert_style: LINE_STYLE = 'large_dashed',         vert_label_background_color: str = 'rgb(46, 46, 46)',         horz_visible: bool = True,         horz_width: int = 1,         h...*
- **Link:** [View in docs](./abstract_docs.md)

#### `vert_style`

- **Occurrences:** 2
- **Context:** *...isible: bool = True,         vert_width: int = 1,         vert_color: Optional[str] = None,         vert_style: LINE_STYLE = 'large_dashed',         vert_label_background_color: str = 'rgb(46, 46, 46)',        ...*
- **Link:** [View in docs](./abstract_docs.md)

#### `vert_visible`

- **Occurrences:** 2
- **Context:** *...         }})""")      def crosshair(         self,         mode: CROSSHAIR_MODE = 'normal',         vert_visible: bool = True,         vert_width: int = 1,         vert_color: Optional[str] = None,         vert_s...*
- **Link:** [View in docs](./abstract_docs.md)

#### `vert_width`

- **Occurrences:** 2
- **Context:** *...(         self,         mode: CROSSHAIR_MODE = 'normal',         vert_visible: bool = True,         vert_width: int = 1,         vert_color: Optional[str] = None,         vert_style: LINE_STYLE = 'large_dashed'...*
- **Link:** [View in docs](./abstract_docs.md)

#### `vertical_line`

- **Occurrences:** 1
- **Context:** *...    text: str = ''     ) -> RayLine:     # TODO         return RayLine(*locals().values())      def vertical_line(         self,         time: TIME,         color: str = '#1E80F0',         width: int = 2,         ...*
- **Link:** [View in docs](./abstract_docs.md)

#### `vertical_span`

- **Occurrences:** 1
- **Context:** *... in {self.id}) {self.id}.volumeSeries.applyOptions({{visible: {jbool(arg)}}})         ''')      def vertical_span(         self,         start_time: Union[TIME, tuple, list],         end_time: Optional[TIME] = Non...*
- **Link:** [View in docs](./abstract_docs.md)

#### `volume_config`

- **Occurrences:** 1
- **Context:** *... down_color         self.run_script(f"{self.id}.series.applyOptions({js_json(locals())})")      def volume_config(self, scale_margin_top: float = 0.8, scale_margin_bottom: float = 0.0,                       up_col...*
- **Link:** [View in docs](./abstract_docs.md)

### W

#### `Window`

- **Occurrences:** 2
- **Context:** *...th.dirname(os.path.abspath(__file__)) INDEX = os.path.join(current_dir, 'js', 'index.html')   class Window:     _id_gen = IDGen()     handlers = {}      def __init__(         self,         script_func: Opti...*
- **Link:** [View in docs](./abstract_docs.md)

#### `wick_down_color`

- **Occurrences:** 4
- **Context:** *... True, border_up_color: str = '',             border_down_color: str = '', wick_up_color: str = '', wick_down_color: str = ''):         """         Candle styling for each of its parts.\n         If only `up_color` ...*
- **Link:** [View in docs](./abstract_docs.md)

#### `wick_up_color`

- **Occurrences:** 4
- **Context:** *...e, border_visible: bool = True, border_up_color: str = '',             border_down_color: str = '', wick_up_color: str = '', wick_down_color: str = ''):         """         Candle styling for each of its parts.\n ...*
- **Link:** [View in docs](./abstract_docs.md)

#### `wick_visible`

- **Occurrences:** 1
- **Context:** *...up_color: str = 'rgba(39, 157, 130, 100)', down_color: str = 'rgba(200, 97, 100, 100)',             wick_visible: bool = True, border_visible: bool = True, border_up_color: str = '',             border_down_color...*
- **Link:** [View in docs](./abstract_docs.md)

---

*Keywords extracted on 2025-11-18T21:53:49.229147*
