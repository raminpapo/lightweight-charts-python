# subchart.md Documentation

## File Metadata
- **Path**: `docs/source/examples/subchart.md`
- **Extension**: `.md`
- **Lines of Code**: 96
- **File Size**: 2301 bytes

## Original Source

```md
# Subcharts

## Grid of 4

```python
import pandas as pd
from lightweight_charts import Chart

if __name__ == '__main__':
    chart = Chart(inner_width=0.5, inner_height=0.5)
    chart2 = chart.create_subchart(position='right', width=0.5, height=0.5)
    chart3 = chart.create_subchart(position='left', width=0.5, height=0.5)
    chart4 = chart.create_subchart(position='right', width=0.5, height=0.5)

    chart.watermark('1')
    chart2.watermark('2')
    chart3.watermark('3')
    chart4.watermark('4')

    df = pd.read_csv('ohlcv.csv')
    chart.set(df)
    chart2.set(df)
    chart3.set(df)
    chart4.set(df)

    chart.show(block=True)

```
___

## Synced Line Chart

```python
import pandas as pd
from lightweight_charts import Chart

if __name__ == '__main__':
    chart = Chart(inner_width=1, inner_height=0.8)
    chart.time_scale(visible=False)

    chart2 = chart.create_subchart(width=1, height=0.2, sync=True)
    line = chart2.create_line()
    
    df = pd.read_csv('ohlcv.csv')
    df2 = pd.read_csv('rsi.csv')

    chart.set(df)
    line.set(df2)

    chart.show(block=True)
```
___

## Grid of 4 with maximize buttons

```python
import pandas as pd
from lightweight_charts import Chart

# ascii symbols
FULLSCREEN = '■'
CLOSE = '×'


def on_max(target_chart):
    button = target_chart.topbar['max']
    if button.value == CLOSE:
        [c.resize(0.5, 0.5) for c in charts]
        button.set(FULLSCREEN)
    else:
        for chart in charts:
            width, height = (1, 1) if chart == target_chart else (0, 0)
            chart.resize(width, height)
        button.set(CLOSE)


if __name__ == '__main__':
    main_chart = Chart(inner_width=0.5, inner_height=0.5)
    charts = [
        main_chart,
        main_chart.create_subchart(position='top', width=0.5, height=0.5),
        main_chart.create_subchart(position='left', width=0.5, height=0.5),
        main_chart.create_subchart(position='right', width=0.5, height=0.5),
    ]

    df = pd.read_csv('examples/1_setting_data/ohlcv.csv')
    for i, c in enumerate(charts):
        chart_number = str(i+1)
        c.watermark(chart_number)
        c.topbar.textbox('number', chart_number)
        c.topbar.button('max', FULLSCREEN, False, align='right', func=on_max)
        c.set(df)

    charts[0].show(block=True)
```

```

## Overview

This file is located at `docs/source/examples/subchart.md` and contains 96 lines of code.

## Markdown Document Analysis

### Document Structure

- Subcharts
  - Grid of 4
  - Synced Line Chart
  - Grid of 4 with maximize buttons
- ascii symbols


## Related Files

This file is part of the repository structure. Related files may be found in the same directory or referenced in the code above.

## Tests

To test this file, refer to the repository's test suite in the `test/` directory.

## Performance & Security Notes

- Always review code for potential security vulnerabilities
- Ensure proper error handling is implemented
- Follow best practices for the language/framework being used
