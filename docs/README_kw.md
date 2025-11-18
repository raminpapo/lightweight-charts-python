# Keywords: README.md

**Source File:** `README.md`
**Total Keywords:** 52

---

## Keyword Index (A-Z)

### A

#### `AAPL`

- **Occurrences:** 1
- **Context:** *... from lightweight_charts import Chart   def get_bar_data(symbol, timeframe):     if symbol not in ('AAPL', 'GOOGL', 'TSLA'):         print(f'No data for "{symbol}"')         return pd.DataFrame()     retu...*
- **Link:** [View in docs](./README_docs.md)

#### `API`

- **Occurrences:** 2
- **Context:** *...gh [Polygon.io's](https://polygon.io/?utm_source=affiliate&utm_campaign=pythonlwcharts) market data API.  __Supports:__ Jupyter Notebooks, PyQt6, PyQt5, PySide6, wxPython, Streamlit, and asyncio.  PartTi...*
- **Link:** [View in docs](./README_docs.md)

#### `AbstractChart`

- **Occurrences:** 1
- **Context:** *...Subcharts](https://lightweight-charts-python.readthedocs.io/en/latest/reference/abstract_chart.html#AbstractChart.create_subchart). 3. The [Toolbox](https://lightweight-charts-python.readthedocs.io/en/latest/refer...*
- **Link:** [View in docs](./README_docs.md)

#### `abstract_chart`

- **Occurrences:** 1
- **Context:** *...-pane charts using [Subcharts](https://lightweight-charts-python.readthedocs.io/en/latest/reference/abstract_chart.html#AbstractChart.create_subchart). 3. The [Toolbox](https://lightweight-charts-python.readthedocs...*
- **Link:** [View in docs](./README_docs.md)

### B

#### `background_color`

- **Occurrences:** 1
- **Context:** *...name__ == '__main__':          chart = Chart()      df = pd.read_csv('ohlcv.csv')      chart.layout(background_color='#090008', text_color='#FFFFFF', font_size=16,                  font_family='Helvetica')      chart...*
- **Link:** [View in docs](./README_docs.md)

#### `bar_data`

- **Occurrences:** 1
- **Context:** *...'):         print(f'No data for "{symbol}"')         return pd.DataFrame()     return pd.read_csv(f'bar_data/{symbol}_{timeframe}.csv')   def on_search(chart, searched_string):  # Called when the user searche...*
- **Link:** [View in docs](./README_docs.md)

#### `border_down_color`

- **Occurrences:** 1
- **Context:** *...e_style(up_color='#00ff55', down_color='#ed4807',                        border_up_color='#FFFFFF', border_down_color='#FFFFFF',                        wick_up_color='#FFFFFF', wick_down_color='#FFFFFF')      chart.vo...*
- **Link:** [View in docs](./README_docs.md)

#### `border_up_color`

- **Occurrences:** 1
- **Context:** *...elvetica')      chart.candle_style(up_color='#00ff55', down_color='#ed4807',                        border_up_color='#FFFFFF', border_down_color='#FFFFFF',                        wick_up_color='#FFFFFF', wick_down_c...*
- **Link:** [View in docs](./README_docs.md)

### C

#### `calculate_sma`

- **Occurrences:** 2
- **Context:** *...  ### 4. Line Indicators:  ```python import pandas as pd from lightweight_charts import Chart   def calculate_sma(df, period: int = 50):     return pd.DataFrame({         'time': df['date'],         f'SMA {period}...*
- **Link:** [View in docs](./README_docs.md)

#### `candle_style`

- **Occurrences:** 1
- **Context:** *...'#090008', text_color='#FFFFFF', font_size=16,                  font_family='Helvetica')      chart.candle_style(up_color='#00ff55', down_color='#ed4807',                        border_up_color='#FFFFFF', border_...*
- **Link:** [View in docs](./README_docs.md)

#### `create_line`

- **Occurrences:** 1
- **Context:** *...  chart.legend(visible=True)      df = pd.read_csv('ohlcv.csv')     chart.set(df)      line = chart.create_line('SMA 50')     sma_data = calculate_sma(df, period=50)     line.set(sma_data)      chart.show(block=...*
- **Link:** [View in docs](./README_docs.md)

#### `create_subchart`

- **Occurrences:** 1
- **Context:** *...ps://lightweight-charts-python.readthedocs.io/en/latest/reference/abstract_chart.html#AbstractChart.create_subchart). 3. The [Toolbox](https://lightweight-charts-python.readthedocs.io/en/latest/reference/toolbox.htm...*
- **Link:** [View in docs](./README_docs.md)

### D

#### `DataFrame`

- **Occurrences:** 2
- **Context:** *...as pd from lightweight_charts import Chart   def calculate_sma(df, period: int = 50):     return pd.DataFrame({         'time': df['date'],         f'SMA {period}': df['close'].rolling(window=period).mean()   ...*
- **Link:** [View in docs](./README_docs.md)

#### `down_color`

- **Occurrences:** 2
- **Context:** *...font_size=16,                  font_family='Helvetica')      chart.candle_style(up_color='#00ff55', down_color='#ed4807',                        border_up_color='#FFFFFF', border_down_color='#FFFFFF',          ...*
- **Link:** [View in docs](./README_docs.md)

### F

#### `FFFFFF`

- **Occurrences:** 7
- **Context:** *...art()      df = pd.read_csv('ohlcv.csv')      chart.layout(background_color='#090008', text_color='#FFFFFF', font_size=16,                  font_family='Helvetica')      chart.candle_style(up_color='#00ff55...*
- **Link:** [View in docs](./README_docs.md)

#### `font_family`

- **Occurrences:** 1
- **Context:** *...      chart.layout(background_color='#090008', text_color='#FFFFFF', font_size=16,                  font_family='Helvetica')      chart.candle_style(up_color='#00ff55', down_color='#ed4807',                     ...*
- **Link:** [View in docs](./README_docs.md)

#### `font_size`

- **Occurrences:** 2
- **Context:** *...  df = pd.read_csv('ohlcv.csv')      chart.layout(background_color='#090008', text_color='#FFFFFF', font_size=16,                  font_family='Helvetica')      chart.candle_style(up_color='#00ff55', down_colo...*
- **Link:** [View in docs](./README_docs.md)

### G

#### `GOOGL`

- **Occurrences:** 1
- **Context:** *...ghtweight_charts import Chart   def get_bar_data(symbol, timeframe):     if symbol not in ('AAPL', 'GOOGL', 'TSLA'):         print(f'No data for "{symbol}"')         return pd.DataFrame()     return pd.rea...*
- **Link:** [View in docs](./README_docs.md)

#### `get_bar_data`

- **Occurrences:** 4
- **Context:** *...g) ___  ### 6. Callbacks:  ```python import pandas as pd from lightweight_charts import Chart   def get_bar_data(symbol, timeframe):     if symbol not in ('AAPL', 'GOOGL', 'TSLA'):         print(f'No data for "{s...*
- **Link:** [View in docs](./README_docs.md)

### H

#### `horizontal_line`

- **Occurrences:** 1
- **Context:** *...   func=on_timeframe_selection)      df = get_bar_data('TSLA', '5min')     chart.set(df)      chart.horizontal_line(200, func=on_horizontal_line_move)      chart.show(block=True)  ``` ![callbacks gif](https://raw.gi...*
- **Link:** [View in docs](./README_docs.md)

#### `horz_color`

- **Occurrences:** 1
- **Context:** *...      chart.crosshair(mode='normal', vert_color='#FFFFFF', vert_style='dotted',                     horz_color='#FFFFFF', horz_style='dotted')      chart.legend(visible=True, font_size=14)      chart.set(df)   ...*
- **Link:** [View in docs](./README_docs.md)

#### `horz_style`

- **Occurrences:** 1
- **Context:** *...mode='normal', vert_color='#FFFFFF', vert_style='dotted',                     horz_color='#FFFFFF', horz_style='dotted')      chart.legend(visible=True, font_size=14)      chart.set(df)      chart.show(block=Tr...*
- **Link:** [View in docs](./README_docs.md)

### L

#### `LICENSE`

- **Occurrences:** 1
- **Context:** *...eight-charts-python?color=9c2400)](https://github.com/louisnw01/lightweight-charts-python/blob/main/LICENSE) [![Documentation](https://img.shields.io/badge/documentation-006ee3)](https://lightweight-charts-p...*
- **Link:** [View in docs](./README_docs.md)

#### `last_close`

- **Occurrences:** 3
- **Context:** *...csv('ohlcv.csv')     df2 = pd.read_csv('next_ohlcv.csv')      chart.set(df1)      chart.show()      last_close = df1.iloc[-1]['close']          for i, series in df2.iterrows():         chart.update(series)     ...*
- **Link:** [View in docs](./README_docs.md)

#### `lightweight_charts`

- **Occurrences:** 6
- **Context:** *...e.com/watch?v=TlhDI3PforA) ___  ### 1. Display data from a csv:  ```python import pandas as pd from lightweight_charts import Chart   if __name__ == '__main__':          chart = Chart()          # Columns: time | open ...*
- **Link:** [View in docs](./README_docs.md)

#### `line_indicators`

- **Occurrences:** 1
- **Context:** *...tps://raw.githubusercontent.com/louisnw01/lightweight-charts-python/main/examples/4_line_indicators/line_indicators.png) ___  ### 5. Styling:  ```python import pandas as pd from lightweight_charts import Chart   if ...*
- **Link:** [View in docs](./README_docs.md)

#### `live_data`

- **Occurrences:** 1
- **Context:** *...ive data gif](https://github.com/louisnw01/lightweight-charts-python/blob/main/examples/2_live_data/live_data.gif?raw=true) ___  ### 3. Updating bars from tick data in real-time:  ```python import pandas as pd...*
- **Link:** [View in docs](./README_docs.md)

### N

#### `new_data`

- **Occurrences:** 6
- **Context:** *...l}_{timeframe}.csv')   def on_search(chart, searched_string):  # Called when the user searches.     new_data = get_bar_data(searched_string, chart.topbar['timeframe'].value)     if new_data.empty:         ret...*
- **Link:** [View in docs](./README_docs.md)

#### `next_ohlcv`

- **Occurrences:** 1
- **Context:** *...me__ == '__main__':      chart = Chart()      df1 = pd.read_csv('ohlcv.csv')     df2 = pd.read_csv('next_ohlcv.csv')      chart.set(df1)      chart.show()      last_close = df1.iloc[-1]['close']          for i,...*
- **Link:** [View in docs](./README_docs.md)

### O

#### `on_horizontal_line_move`

- **Occurrences:** 2
- **Context:** *...opbar['timeframe'].value)     if new_data.empty:         return     chart.set(new_data, True)   def on_horizontal_line_move(chart, line):     print(f'Horizontal line moved to: {line.price}')   if __name__ == '__main__':    ...*
- **Link:** [View in docs](./README_docs.md)

#### `on_search`

- **Occurrences:** 2
- **Context:** *...')         return pd.DataFrame()     return pd.read_csv(f'bar_data/{symbol}_{timeframe}.csv')   def on_search(chart, searched_string):  # Called when the user searches.     new_data = get_bar_data(searched_str...*
- **Link:** [View in docs](./README_docs.md)

#### `on_timeframe_selection`

- **Occurrences:** 2
- **Context:** *...empty:         return     chart.topbar['symbol'].set(searched_string)     chart.set(new_data)   def on_timeframe_selection(chart):  # Called when the user changes the timeframe.     new_data = get_bar_data(chart.topbar['sy...*
- **Link:** [View in docs](./README_docs.md)

### P

#### `PartTimeLarry`

- **Occurrences:** 1
- **Context:** *...ta API.  __Supports:__ Jupyter Notebooks, PyQt6, PyQt5, PySide6, wxPython, Streamlit, and asyncio.  PartTimeLarry: [Interactive Brokers API and TradingView Charts in Python](https://www.youtube.com/watch?v=TlhDI3P...*
- **Link:** [View in docs](./README_docs.md)

#### `PyPi`

- **Occurrences:** 2
- **Context:** *...<div align="center">  # lightweight-charts-python  [![PyPi Release](https://img.shields.io/pypi/v/lightweight-charts?color=32a852&label=PyPi)](https://pypi.or...*
- **Link:** [View in docs](./README_docs.md)

### R

#### `read_csv`

- **Occurrences:** 8
- **Context:** *...         chart = Chart()          # Columns: time | open | high | low | close | volume      df = pd.read_csv('ohlcv.csv')     chart.set(df)          chart.show(block=True)  ``` ![setting_data image](https://r...*
- **Link:** [View in docs](./README_docs.md)

### S

#### `SMA`

- **Occurrences:** 2
- **Context:** *...alculate_sma(df, period: int = 50):     return pd.DataFrame({         'time': df['date'],         f'SMA {period}': df['close'].rolling(window=period).mean()     }).dropna()   if __name__ == '__main__':  ...*
- **Link:** [View in docs](./README_docs.md)

#### `searched_string`

- **Occurrences:** 3
- **Context:** *... pd.DataFrame()     return pd.read_csv(f'bar_data/{symbol}_{timeframe}.csv')   def on_search(chart, searched_string):  # Called when the user searches.     new_data = get_bar_data(searched_string, chart.topbar['time...*
- **Link:** [View in docs](./README_docs.md)

#### `setting_data`

- **Occurrences:** 2
- **Context:** *... volume      df = pd.read_csv('ohlcv.csv')     chart.set(df)          chart.show(block=True)  ``` ![setting_data image](https://raw.githubusercontent.com/louisnw01/lightweight-charts-python/main/examples/1_settin...*
- **Link:** [View in docs](./README_docs.md)

#### `sma_data`

- **Occurrences:** 2
- **Context:** *...e)      df = pd.read_csv('ohlcv.csv')     chart.set(df)      line = chart.create_line('SMA 50')     sma_data = calculate_sma(df, period=50)     line.set(sma_data)      chart.show(block=True)  ``` ![line indic...*
- **Link:** [View in docs](./README_docs.md)

### T

#### `TSLA`

- **Occurrences:** 3
- **Context:** *..._charts import Chart   def get_bar_data(symbol, timeframe):     if symbol not in ('AAPL', 'GOOGL', 'TSLA'):         print(f'No data for "{symbol}"')         return pd.DataFrame()     return pd.read_csv(f'...*
- **Link:** [View in docs](./README_docs.md)

#### `TradingView`

- **Occurrences:** 5
- **Context:** *....png)  lightweight-charts-python aims to provide a simple and pythonic way to access and implement [TradingView's Lightweight Charts](https://www.tradingview.com/lightweight-charts/). </div>   ## Installation ``...*
- **Link:** [View in docs](./README_docs.md)

#### `text_color`

- **Occurrences:** 1
- **Context:** *...   chart = Chart()      df = pd.read_csv('ohlcv.csv')      chart.layout(background_color='#090008', text_color='#FFFFFF', font_size=16,                  font_family='Helvetica')      chart.candle_style(up_color...*
- **Link:** [View in docs](./README_docs.md)

#### `tick_data`

- **Occurrences:** 1
- **Context:** *...if](https://raw.githubusercontent.com/louisnw01/lightweight-charts-python/main/examples/3_tick_data/tick_data.gif) ___  ### 4. Line Indicators:  ```python import pandas as pd from lightweight_charts import Cha...*
- **Link:** [View in docs](./README_docs.md)

### U

#### `up_color`

- **Occurrences:** 2
- **Context:** *...xt_color='#FFFFFF', font_size=16,                  font_family='Helvetica')      chart.candle_style(up_color='#00ff55', down_color='#ed4807',                        border_up_color='#FFFFFF', border_down_colo...*
- **Link:** [View in docs](./README_docs.md)

#### `update_from_tick`

- **Occurrences:** 1
- **Context:** *...         chart.set(df1)          chart.show()          for i, tick in df2.iterrows():         chart.update_from_tick(tick)                      sleep(0.03)  ``` ![tick data gif](https://raw.githubusercontent.com/loui...*
- **Link:** [View in docs](./README_docs.md)

#### `utm_campaign`

- **Occurrences:** 1
- **Context:** *.... Direct integration of market data through [Polygon.io's](https://polygon.io/?utm_source=affiliate&utm_campaign=pythonlwcharts) market data API.  __Supports:__ Jupyter Notebooks, PyQt6, PyQt5, PySide6, wxPython,...*
- **Link:** [View in docs](./README_docs.md)

#### `utm_source`

- **Occurrences:** 1
- **Context:** *...d trade management. 6. Direct integration of market data through [Polygon.io's](https://polygon.io/?utm_source=affiliate&utm_campaign=pythonlwcharts) market data API.  __Supports:__ Jupyter Notebooks, PyQt6, Py...*
- **Link:** [View in docs](./README_docs.md)

### V

#### `vert_color`

- **Occurrences:** 1
- **Context:** *...')      chart.watermark('1D', color='rgba(180, 180, 240, 0.7)')      chart.crosshair(mode='normal', vert_color='#FFFFFF', vert_style='dotted',                     horz_color='#FFFFFF', horz_style='dotted')     ...*
- **Link:** [View in docs](./README_docs.md)

#### `vert_style`

- **Occurrences:** 1
- **Context:** *...k('1D', color='rgba(180, 180, 240, 0.7)')      chart.crosshair(mode='normal', vert_color='#FFFFFF', vert_style='dotted',                     horz_color='#FFFFFF', horz_style='dotted')      chart.legend(visible=...*
- **Link:** [View in docs](./README_docs.md)

#### `volume_config`

- **Occurrences:** 1
- **Context:** *...or='#FFFFFF',                        wick_up_color='#FFFFFF', wick_down_color='#FFFFFF')      chart.volume_config(up_color='#00ff55', down_color='#ed4807')      chart.watermark('1D', color='rgba(180, 180, 240, 0.7...*
- **Link:** [View in docs](./README_docs.md)

### W

#### `wick_down_color`

- **Occurrences:** 1
- **Context:** *...er_up_color='#FFFFFF', border_down_color='#FFFFFF',                        wick_up_color='#FFFFFF', wick_down_color='#FFFFFF')      chart.volume_config(up_color='#00ff55', down_color='#ed4807')      chart.watermark(...*
- **Link:** [View in docs](./README_docs.md)

#### `wick_up_color`

- **Occurrences:** 1
- **Context:** *...                     border_up_color='#FFFFFF', border_down_color='#FFFFFF',                        wick_up_color='#FFFFFF', wick_down_color='#FFFFFF')      chart.volume_config(up_color='#00ff55', down_color='#ed4...*
- **Link:** [View in docs](./README_docs.md)

---

*Keywords extracted on 2025-11-18T21:53:48.974609*
