# Keywords: drawings.py

**Source File:** `lightweight_charts/drawings.py`
**Total Keywords:** 34

---

## Keyword Index (A-Z)

### A

#### `as_enum`

- **Occurrences:** 7
- **Context:** *...g import Union, Optional  from lightweight_charts.util import js_json  from .util import NUM, Pane, as_enum, LINE_STYLE, TIME, snake_to_camel  def make_js_point(chart, time, price):     formatted_time = char...*
- **Link:** [View in docs](./drawings_docs.md)

#### `axis_label_visible`

- **Occurrences:** 1
- **Context:** *...')   class HorizontalLine(Drawing):     def __init__(self, chart, price, color, width, style, text, axis_label_visible, func):         super().__init__(chart, func)         self.price = price         self.run_script(f'...*
- **Link:** [View in docs](./drawings_docs.md)

### B

#### `Box`

- **Occurrences:** 2
- **Context:** *... else 'null'}         )         {chart.id}.series.attachPrimitive({self.id})         ''')     class Box(TwoPointDrawing):     def __init__(self,         chart,         start_time: TIME,         start_val...*
- **Link:** [View in docs](./drawings_docs.md)

### D

#### `DatetimeIndex`

- **Occurrences:** 1
- **Context:** *... 0}}         }})         ''')         if end_time is None:             if isinstance(start_time, pd.DatetimeIndex):                 data = [{'time': time.timestamp(), 'value': 1} for time in start_time]           ...*
- **Link:** [View in docs](./drawings_docs.md)

#### `Drawing`

- **Occurrences:** 5
- **Context:** *...timeToCoordinate({formatted_time})                     ),         "price": {price}     }}'''  class Drawing(Pane):     def __init__(self, chart, func=None):         super().__init__(chart.win)         self.c...*
- **Link:** [View in docs](./drawings_docs.md)

#### `drawing_type`

- **Occurrences:** 2
- **Context:** *...: {width},         }})''')  class TwoPointDrawing(Drawing):     def __init__(         self,         drawing_type,         chart,         start_time: TIME,         start_value: NUM,         end_time: TIME,        ...*
- **Link:** [View in docs](./drawings_docs.md)

### E

#### `end_time`

- **Occurrences:** 11
- **Context:** *...f,         drawing_type,         chart,         start_time: TIME,         start_value: NUM,         end_time: TIME,         end_value: NUM,         round: bool,         options: dict,         func=None     ):...*
- **Link:** [View in docs](./drawings_docs.md)

#### `end_value`

- **Occurrences:** 6
- **Context:** *...         chart,         start_time: TIME,         start_value: NUM,         end_time: TIME,         end_value: NUM,         round: bool,         options: dict,         func=None     ):         super().__init__...*
- **Link:** [View in docs](./drawings_docs.md)

### F

#### `fill_color`

- **Occurrences:** 2
- **Context:** *...      end_time: TIME,         end_value: NUM,         round: bool,         line_color: str,         fill_color: str,         width: int,         style: LINE_STYLE,         func=None):          super().__init__(...*
- **Link:** [View in docs](./drawings_docs.md)

#### `formatted_points`

- **Occurrences:** 4
- **Context:** *...     super().__init__(chart.win)         self.chart = chart      def update(self, *points):         formatted_points = []         for i in range(0, len(points), 2):             formatted_points.append(make_js_point(s...*
- **Link:** [View in docs](./drawings_docs.md)

#### `formatted_time`

- **Occurrences:** 3
- **Context:** *...rt NUM, Pane, as_enum, LINE_STYLE, TIME, snake_to_camel  def make_js_point(chart, time, price):     formatted_time = chart._single_datetime_format(time)     return f'''{{         "time": {formatted_time},         "...*
- **Link:** [View in docs](./drawings_docs.md)

### H

#### `HorizontalLine`

- **Occurrences:** 2
- **Context:** *...             }}         )         {chart.id}.series.attachPrimitive({self.id})         ''')   class HorizontalLine(Drawing):     def __init__(self, chart, price, color, width, style, text, axis_label_visible, func)...*
- **Link:** [View in docs](./drawings_docs.md)

### J

#### `js_json`

- **Occurrences:** 1
- **Context:** *...t json import pandas as pd  from typing import Union, Optional  from lightweight_charts.util import js_json  from .util import NUM, Pane, as_enum, LINE_STYLE, TIME, snake_to_camel  def make_js_point(chart, t...*
- **Link:** [View in docs](./drawings_docs.md)

### L

#### `LINE_STYLE`

- **Occurrences:** 10
- **Context:** *...Union, Optional  from lightweight_charts.util import js_json  from .util import NUM, Pane, as_enum, LINE_STYLE, TIME, snake_to_camel  def make_js_point(chart, time, price):     formatted_time = chart._single_da...*
- **Link:** [View in docs](./drawings_docs.md)

#### `lightweight_charts`

- **Occurrences:** 1
- **Context:** *...import asyncio import json import pandas as pd  from typing import Union, Optional  from lightweight_charts.util import js_json  from .util import NUM, Pane, as_enum, LINE_STYLE, TIME, snake_to_camel  def ma...*
- **Link:** [View in docs](./drawings_docs.md)

#### `line_color`

- **Occurrences:** 4
- **Context:** *...     start_value: NUM,         end_time: TIME,         end_value: NUM,         round: bool,         line_color: str,         fill_color: str,         width: int,         style: LINE_STYLE,         func=None):  ...*
- **Link:** [View in docs](./drawings_docs.md)

### M

#### `make_js_point`

- **Occurrences:** 4
- **Context:** *...ts.util import js_json  from .util import NUM, Pane, as_enum, LINE_STYLE, TIME, snake_to_camel  def make_js_point(chart, time, price):     formatted_time = chart._single_datetime_format(time)     return f'''{{    ...*
- **Link:** [View in docs](./drawings_docs.md)

### N

#### `NUM`

- **Occurrences:** 8
- **Context:** *... from typing import Union, Optional  from lightweight_charts.util import js_json  from .util import NUM, Pane, as_enum, LINE_STYLE, TIME, snake_to_camel  def make_js_point(chart, time, price):     format...*
- **Link:** [View in docs](./drawings_docs.md)

### O

#### `options_string`

- **Occurrences:** 2
- **Context:** *...l,         options: dict,         func=None     ):         super().__init__(chart, func)            options_string = '\n'.join(f'{key}: {val},' for key, val in options.items())          self.run_script(f'''        ...*
- **Link:** [View in docs](./drawings_docs.md)

### R

#### `RayLine`

- **Occurrences:** 2
- **Context:** *...color, style, width)         self.run_script(f'{self.id}.applyOptions({{text: `{text}`}})')   class RayLine(Drawing):     def __init__(self,         chart,         start_time: TIME,         value: NUM,      ...*
- **Link:** [View in docs](./drawings_docs.md)

#### `run_script`

- **Occurrences:** 18
- **Context:** *...          formatted_points.append(make_js_point(self.chart, points[i], points[i + 1]))         self.run_script(f'{self.id}.updatePoints({", ".join(formatted_points)})')         print(f'{self.id}.updatePoints({"...*
- **Link:** [View in docs](./drawings_docs.md)

### S

#### `SeriesCommon`

- **Occurrences:** 1
- **Context:** *...   func         )  # TODO reimplement/fix class VerticalSpan(Pane):     def __init__(self, series: 'SeriesCommon', start_time: Union[TIME, tuple, list], end_time: Optional[TIME] = None,                  color: st...*
- **Link:** [View in docs](./drawings_docs.md)

#### `snake_to_camel`

- **Occurrences:** 1
- **Context:** *...rom lightweight_charts.util import js_json  from .util import NUM, Pane, as_enum, LINE_STYLE, TIME, snake_to_camel  def make_js_point(chart, time, price):     formatted_time = chart._single_datetime_format(time)   ...*
- **Link:** [View in docs](./drawings_docs.md)

#### `start_time`

- **Occurrences:** 15
- **Context:** *...PointDrawing(Drawing):     def __init__(         self,         drawing_type,         chart,         start_time: TIME,         start_value: NUM,         end_time: TIME,         end_value: NUM,         round: boo...*
- **Link:** [View in docs](./drawings_docs.md)

#### `start_value`

- **Occurrences:** 6
- **Context:** *... def __init__(         self,         drawing_type,         chart,         start_time: TIME,         start_value: NUM,         end_time: TIME,         end_value: NUM,         round: bool,         options: dict,  ...*
- **Link:** [View in docs](./drawings_docs.md)

### T

#### `TIME`

- **Occurrences:** 11
- **Context:** *...nal  from lightweight_charts.util import js_json  from .util import NUM, Pane, as_enum, LINE_STYLE, TIME, snake_to_camel  def make_js_point(chart, time, price):     formatted_time = chart._single_datetime...*
- **Link:** [View in docs](./drawings_docs.md)

#### `TODO`

- **Occurrences:** 1
- **Context:** *...               "lineStyle": as_enum(style, LINE_STYLE)             },             func         )  # TODO reimplement/fix class VerticalSpan(Pane):     def __init__(self, series: 'SeriesCommon', start_time...*
- **Link:** [View in docs](./drawings_docs.md)

#### `TrendLine`

- **Occurrences:** 2
- **Context:** *...          "lineStyle": as_enum(style, LINE_STYLE)             },             func         )   class TrendLine(TwoPointDrawing):     def __init__(self,         chart,         start_time: TIME,         start_val...*
- **Link:** [View in docs](./drawings_docs.md)

#### `TwoPointDrawing`

- **Occurrences:** 3
- **Context:** *...        lineStyle: {as_enum(style, LINE_STYLE)},             width: {width},         }})''')  class TwoPointDrawing(Drawing):     def __init__(         self,         drawing_type,         chart,         start_time: ...*
- **Link:** [View in docs](./drawings_docs.md)

#### `to_datetime`

- **Occurrences:** 2
- **Context:** *...._chart = series._chart         super().__init__(self._chart.win)         start_time, end_time = pd.to_datetime(start_time), pd.to_datetime(end_time)         self.run_script(f'''         {self.id} = {self._chart...*
- **Link:** [View in docs](./drawings_docs.md)

### V

#### `VerticalLine`

- **Occurrences:** 2
- **Context:** *...olor, style, width)         self.run_script(f'{self.id}.applyOptions({{text: `{text}`}})')    class VerticalLine(Drawing):     def __init__(self, chart, time, color, width, style, text, func=None):         super(...*
- **Link:** [View in docs](./drawings_docs.md)

#### `VerticalSpan`

- **Occurrences:** 1
- **Context:** *... as_enum(style, LINE_STYLE)             },             func         )  # TODO reimplement/fix class VerticalSpan(Pane):     def __init__(self, series: 'SeriesCommon', start_time: Union[TIME, tuple, list], end_tim...*
- **Link:** [View in docs](./drawings_docs.md)

#### `vertical_line`

- **Occurrences:** 1
- **Context:** *...  color: '{color}',                 priceFormat: {{type: 'volume'}},                 priceScaleId: 'vertical_line',                 lastValueVisible: false,                 priceLineVisible: false,         }})    ...*
- **Link:** [View in docs](./drawings_docs.md)

### W

#### `wrapper_async`

- **Occurrences:** 2
- **Context:** *... def wrapper(p):             self.price = float(p)             func(chart, self)          async def wrapper_async(p):             self.price = float(p)             await func(chart, self)          self.win.handler...*
- **Link:** [View in docs](./drawings_docs.md)

---

*Keywords extracted on 2025-11-18T21:53:49.254793*
