# drawings.py

**File Path:** `lightweight_charts/drawings.py`

**File Size:** 8,430 bytes
**Lines of Code:** 281
**Language:** python

---

## File Metadata

- **Relative Path:** `lightweight_charts/drawings.py`
- **File Type:** .py
- **Size:** 8,430 bytes
- **Total Lines:** 281
- **Programming Language:** python

## Quick Summary

This file is part of the lightweight-charts-python repository.
 It defines 8 class(es).
 It contains 1 function(s).


## Original Source Code

```python

import asyncio
import json
import pandas as pd

from typing import Union, Optional

from lightweight_charts.util import js_json

from .util import NUM, Pane, as_enum, LINE_STYLE, TIME, snake_to_camel

def make_js_point(chart, time, price):
    formatted_time = chart._single_datetime_format(time)
    return f'''{{
        "time": {formatted_time},
        "logical": {chart.id}.chart.timeScale()
                    .coordinateToLogical(
                        {chart.id}.chart.timeScale()
                        .timeToCoordinate({formatted_time})
                    ),
        "price": {price}
    }}'''

class Drawing(Pane):
    def __init__(self, chart, func=None):
        super().__init__(chart.win)
        self.chart = chart

    def update(self, *points):
        formatted_points = []
        for i in range(0, len(points), 2):
            formatted_points.append(make_js_point(self.chart, points[i], points[i + 1]))
        self.run_script(f'{self.id}.updatePoints({", ".join(formatted_points)})')
        print(f'{self.id}.updatePoints({", ".join(formatted_points)})')

    def delete(self):
        """
        Irreversibly deletes the drawing.
        """
        self.run_script(f'{self.id}.detach()')

    def options(self, color='#1E80F0', style='solid', width=4):
        self.run_script(f'''{self.id}.applyOptions({{
            lineColor: '{color}',
            lineStyle: {as_enum(style, LINE_STYLE)},
            width: {width},
        }})''')

class TwoPointDrawing(Drawing):
    def __init__(
        self,
        drawing_type,
        chart,
        start_time: TIME,
        start_value: NUM,
        end_time: TIME,
        end_value: NUM,
        round: bool,
        options: dict,
        func=None
    ):
        super().__init__(chart, func)



        options_string = '\n'.join(f'{key}: {val},' for key, val in options.items())

        self.run_script(f'''
        {self.id} = new Lib.{drawing_type}(
            {make_js_point(self.chart, start_time, start_value)},
            {make_js_point(self.chart, end_time, end_value)},
            {{
                {options_string}
            }}
        )
        {chart.id}.series.attachPrimitive({self.id})
        ''')


class HorizontalLine(Drawing):
    def __init__(self, chart, price, color, width, style, text, axis_label_visible, func):
        super().__init__(chart, func)
        self.price = price
        self.run_script(f'''

        {self.id} = new Lib.HorizontalLine(
            {{price: {price}}},
            {{
                lineColor: '{color}',
                lineStyle: {as_enum(style, LINE_STYLE)},
                width: {width},
                text: `{text}`,
            }},
            callbackName={f"'{self.id}'" if func else 'null'}
        )
        {chart.id}.series.attachPrimitive({self.id})
        ''')
        if not func:
            return

        def wrapper(p):
            self.price = float(p)
            func(chart, self)

        async def wrapper_async(p):
            self.price = float(p)
            await func(chart, self)

        self.win.handlers[self.id] = wrapper_async if asyncio.iscoroutinefunction(func) else wrapper
        self.run_script(f'{chart.id}.toolBox?.addNewDrawing({self.id})')

    def update(self, price: float):
        """
        Moves the horizontal line to the given price.
        """
        self.run_script(f'{self.id}.updatePoints({{price: {price}}})')
        # self.run_script(f'{self.id}.updatePrice({price})')
        self.price = price

    def options(self, color='#1E80F0', style='solid', width=4, text=''):
        super().options(color, style, width)
        self.run_script(f'{self.id}.applyOptions({{text: `{text}`}})')



class VerticalLine(Drawing):
    def __init__(self, chart, time, color, width, style, text, func=None):
        super().__init__(chart, func)
        self.time = time
        self.run_script(f'''

        {self.id} = new Lib.VerticalLine(
            {{time: {self.chart._single_datetime_format(time)}}},
            {{
                lineColor: '{color}',
                lineStyle: {as_enum(style, LINE_STYLE)},
                width: {width},
                text: `{text}`,
            }},
            callbackName={f"'{self.id}'" if func else 'null'}
        )
        {chart.id}.series.attachPrimitive({self.id})
        ''')

    def update(self, time: TIME):
        self.run_script(f'{self.id}.updatePoints({{time: {time}}})')
        # self.run_script(f'{self.id}.updatePrice({price})')
        self.price = price

    def options(self, color='#1E80F0', style='solid', width=4, text=''):
        super().options(color, style, width)
        self.run_script(f'{self.id}.applyOptions({{text: `{text}`}})')


class RayLine(Drawing):
    def __init__(self,
        chart,
        start_time: TIME,
        value: NUM,
        round: bool = False,
        color: str = '#1E80F0',
        width: int = 2,
        style: LINE_STYLE = 'solid',
        text: str = '',
        func = None,
    ):
        super().__init__(chart, func)
        self.run_script(f'''
        {self.id} = new Lib.RayLine(
            {{time: {self.chart._single_datetime_format(start_time)}, price: {value}}},
            {{
                lineColor: '{color}',
                lineStyle: {as_enum(style, LINE_STYLE)},
                width: {width},
                text: `{text}`,
            }},
            callbackName={f"'{self.id}'" if func else 'null'}
        )
        {chart.id}.series.attachPrimitive({self.id})
        ''')




class Box(TwoPointDrawing):
    def __init__(self,
        chart,
        start_time: TIME,
        start_value: NUM,
        end_time: TIME,
        end_value: NUM,
        round: bool,
        line_color: str,
        fill_color: str,
        width: int,
        style: LINE_STYLE,
        func=None):

        super().__init__(
            "Box",
            chart,
            start_time,
            start_value,
            end_time,
            end_value,
            round,
            {
                "lineColor": f'"{line_color}"',
                "fillColor": f'"{fill_color}"',
                "width": width,
                "lineStyle": as_enum(style, LINE_STYLE)
            },
            func
        )


class TrendLine(TwoPointDrawing):
    def __init__(self,
        chart,
        start_time: TIME,
        start_value: NUM,
        end_time: TIME,
        end_value: NUM,
        round: bool,
        line_color: str,
        width: int,
        style: LINE_STYLE,
        func=None):

        super().__init__(
            "TrendLine",
            chart,
            start_time,
            start_value,
            end_time,
            end_value,
            round,
            {
                "lineColor": f'"{line_color}"',
                "width": width,
                "lineStyle": as_enum(style, LINE_STYLE)
            },
            func
        )

# TODO reimplement/fix
class VerticalSpan(Pane):
    def __init__(self, series: 'SeriesCommon', start_time: Union[TIME, tuple, list], end_time: Optional[TIME] = None,
                 color: str = 'rgba(252, 219, 3, 0.2)'):
        self._chart = series._chart
        super().__init__(self._chart.win)
        start_time, end_time = pd.to_datetime(start_time), pd.to_datetime(end_time)
        self.run_script(f'''
        {self.id} = {self._chart.id}.chart.addHistogramSeries({{
                color: '{color}',
                priceFormat: {{type: 'volume'}},
                priceScaleId: 'vertical_line',
                lastValueVisible: false,
                priceLineVisible: false,
        }})
        {self.id}.priceScale('').applyOptions({{
            scaleMargins: {{top: 0, bottom: 0}}
        }})
        ''')
        if end_time is None:
            if isinstance(start_time, pd.DatetimeIndex):
                data = [{'time': time.timestamp(), 'value': 1} for time in start_time]
            else:
                data = [{'time': start_time.timestamp(), 'value': 1}]
            self.run_script(f'{self.id}.setData({data})')
        else:
            self.run_script(f'''
            {self.id}.setData(calculateTrendLine(
            {start_time.timestamp()}, 1, {end_time.timestamp()}, 1, {series.id}))
            ''')

    def delete(self):
        """
        Irreversibly deletes the vertical span.
        """
        self.run_script(f'{self._chart.id}.chart.removeSeries({self.id})')


```

## High-Level Overview

### Classes (8)

- **`Drawing`** (line 23)
- **`TwoPointDrawing`** (line 48)
- **`HorizontalLine`** (line 79)
- **`VerticalLine`** (line 125)
- **`RayLine`** (line 154)
- **`Box`** (line 184)
- **`TrendLine`** (line 216)
- **`VerticalSpan`** (line 246)

### Functions (1)

- **`make_js_point(chart, time, price)`** (line 11)

### Imports (6)

- `import asyncio`
- `import json`
- `import pandas as pd`
- `from typing import Union, Optional`
- `from lightweight_charts.util import js_json`
- `from .util import NUM, Pane, as_enum, LINE_STYLE, TIME, snake_to_camel`

## Detailed Walkthrough

### Code Structure

This file contains 281 lines of python.

#### Classes

##### Drawing (Line 23)

```python
    def __init__(self, chart, func=None):
        super().__init__(chart.win)
        self.chart = chart
```

##### TwoPointDrawing (Line 48)

```python
    def __init__(
        self,
        drawing_type,
        chart,
        start_time: TIME,
        start_value: NUM,
        end_time: TIME,
        end_value: NUM,
        round: bool,
        options: dict,
        func=None
    ):
        super().__init__(chart, func)
```

##### HorizontalLine (Line 79)

```python
    def __init__(self, chart, price, color, width, style, text, axis_label_visible, func):
        super().__init__(chart, func)
        self.price = price
        self.run_script(f'''
```

##### VerticalLine (Line 125)

```python
    def __init__(self, chart, time, color, width, style, text, func=None):
        super().__init__(chart, func)
        self.time = time
        self.run_script(f'''
```

##### RayLine (Line 154)

```python
    def __init__(self,
        chart,
        start_time: TIME,
        value: NUM,
        round: bool = False,
        color: str = '#1E80F0',
        width: int = 2,
        style: LINE_STYLE = 'solid',
        text: str = '',
        func = None,
    ):
        super().__init__(chart, func)
        self.run_script(f'''
        {self.id} = new Lib.RayLine(
            {{time: {self.chart._single_datetime_format(start_time)}, price: {value}}},
            {{
                lineColor: '{color}
```

##### Box (Line 184)

```python
    def __init__(self,
        chart,
        start_time: TIME,
        start_value: NUM,
        end_time: TIME,
        end_value: NUM,
        round: bool,
        line_color: str,
        fill_color: str,
        width: int,
        style: LINE_STYLE,
        func=None):
```

##### TrendLine (Line 216)

```python
    def __init__(self,
        chart,
        start_time: TIME,
        start_value: NUM,
        end_time: TIME,
        end_value: NUM,
        round: bool,
        line_color: str,
        width: int,
        style: LINE_STYLE,
        func=None):
```

##### VerticalSpan (Line 246)

```python
    def __init__(self, series: 'SeriesCommon', start_time: Union[TIME, tuple, list], end_time: Optional[TIME] = None,
                 color: str = 'rgba(252, 219, 3, 0.2)'):
        self._chart = series._chart
        super().__init__(self._chart.win)
        start_time, end_time = pd.to_datetime(start_time), pd.to_datetime(end_time)
        self.run_script(f'''
        {self.id} = {self._chart.id}.chart.addHistogramSeries({{
                color: '{color}',
                priceFormat: {{type
```


#### Functions

##### make_js_point (Line 11)

**Parameters:** `chart, time, price`

## Usage Examples

To use this file in your project:

```python
from lightweight_charts.drawings import *
```

## Performance & Security Notes

### Performance

- File size: 8,430 bytes
- Complexity: 1 functions, 8 classes

### Security

- **Recommendation:** Review this file for potential security vulnerabilities
- No obvious security concerns detected (basic scan)

## Related Files

*To be populated during folder indexing phase*

## Testing

Tests for this file may be located in the `test/` directory.

---

*Documentation generated on 2025-11-18T21:53:49.250786*
