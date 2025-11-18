# Keywords: polygon.py

**Source File:** `lightweight_charts/polygon.py`
**Total Keywords:** 64

---

## Keyword Index (A-Z)

### A

#### `API`

- **Occurrences:** 3
- **Context:** *...      func(pd.Series(lasts), *args)   class PolygonAPI:     """     Offers direct access to Polygon API data within all Chart objects.      It is not designed to be initialized by the user, and should be...*
- **Link:** [View in docs](./polygon_docs.md)

#### `AbstractChart`

- **Occurrences:** 1
- **Context:** *...designed to be initialized by the user, and should be utilised     through the `polygon` method of `AbstractChart` (chart.polygon.<method>).     """     _set_on_load = []      def __init__(self, chart):         se...*
- **Link:** [View in docs](./polygon_docs.md)

#### `active_background_color`

- **Occurrences:** 1
- **Context:** *... = end_date         self.limit = limit         self.live = live         self.win.style(             active_background_color='rgba(91, 98, 246, 0.8)',             muted_background_color='rgba(91, 98, 246, 0.5)'         )    ...*
- **Link:** [View in docs](./polygon_docs.md)

#### `api_key`

- **Occurrences:** 9
- **Context:** *...ogging.DEBUG) _log = logging.getLogger('polygon') _log.setLevel(logging.ERROR) _log.addHandler(ch)  api_key = '' _tickers = {} _set_on_load = []  _lasts = {} _ws = {'stocks': None, 'options': None, 'indices'...*
- **Link:** [View in docs](./polygon_docs.md)

#### `async_crypto`

- **Occurrences:** 1
- **Context:** *...f.async_set('forex', f'C:{fiat_pair}', timeframe, start_date, end_date, limit, live)      async def async_crypto(             self, crypto_pair: str, timeframe: str, start_date: str, end_date: str = 'now',       ...*
- **Link:** [View in docs](./polygon_docs.md)

#### `async_forex`

- **Occurrences:** 1
- **Context:** *...lf.async_set('indices', f'I:{symbol}', timeframe, start_date, end_date, limit, live)      async def async_forex(             self, fiat_pair: str, timeframe: str, start_date: str, end_date: str = 'now',         ...*
- **Link:** [View in docs](./polygon_docs.md)

#### `async_get_bar_data`

- **Occurrences:** 2
- **Context:** *...'):         rename['v'] = 'volume'      return df[rename.keys()].rename(columns=rename)   async def async_get_bar_data(ticker: str, timeframe: str, start_date: str, end_date: str, limit: int = 5_000):     loop = asynci...*
- **Link:** [View in docs](./polygon_docs.md)

#### `async_index`

- **Occurrences:** 1
- **Context:** *...lf.async_set('options', f'O:{symbol}', timeframe, start_date, end_date, limit, live)      async def async_index(             self, symbol: str, timeframe: str, start_date: str, end_date: str = 'now',            ...*
- **Link:** [View in docs](./polygon_docs.md)

#### `async_option`

- **Occurrences:** 1
- **Context:** *...await self.async_set('stocks', symbol, timeframe, start_date, end_date, limit, live)      async def async_option(             self, symbol: str, timeframe: str, start_date: str, expiration: str = None,           ...*
- **Link:** [View in docs](./polygon_docs.md)

#### `async_set`

- **Occurrences:** 7
- **Context:** *...elf, *args):         if asyncio.get_event_loop().is_running():             asyncio.create_task(self.async_set(*args))             return True         else:             _set_on_load.append(args)             ret...*
- **Link:** [View in docs](./polygon_docs.md)

#### `async_stock`

- **Occurrences:** 1
- **Context:** *...self.set('crypto', f'X:{crypto_pair}', timeframe, start_date, end_date, limit, live)      async def async_stock(             self, symbol: str, timeframe: str, start_date: str, end_date: str = 'now',            ...*
- **Link:** [View in docs](./polygon_docs.md)

### B

#### `BTC`

- **Occurrences:** 2
- **Context:** *...lays crypto data pulled from Polygon.io.\n         :param crypto_pair: The crypto pair to request. (BTC-USD, ETH-BTC etc.)         :param timeframe:   Timeframe to request (1min, 5min, 2H, 1D, 1W, 2M, et...*
- **Link:** [View in docs](./polygon_docs.md)

### C

#### `CAD`

- **Occurrences:** 1
- **Context:** *...ays forex data pulled from Polygon.io.\n         :param fiat_pair:   The fiat pair to request. (USD-CAD, GBP-JPY etc.)         :param timeframe:   Timeframe to request (1min, 5min, 2H, 1D, 1W, 2M, etc). ...*
- **Link:** [View in docs](./polygon_docs.md)

#### `create_task`

- **Occurrences:** 2
- **Context:** *...icker: str, sec_type: SEC_TYPE, func, args, precision=2):     if not _ws[sec_type]:         asyncio.create_task(_websocket_connect(sec_type))      if sec_type in ('forex', 'crypto'):         key = ticker[ticker....*
- **Link:** [View in docs](./polygon_docs.md)

#### `crypto_pair`

- **Occurrences:** 5
- **Context:** *... f'C:{fiat_pair}', timeframe, start_date, end_date, limit, live)      def crypto(             self, crypto_pair: str, timeframe: str, start_date: str, end_date: str = 'now',             limit: int = 5_000, live:...*
- **Link:** [View in docs](./polygon_docs.md)

### D

#### `DEBUG`

- **Occurrences:** 1
- **Context:** *...r('%(asctime)s | [polygon.io] %(levelname)s: %(message)s', datefmt='%H:%M:%S')) ch.setLevel(logging.DEBUG) _log = logging.getLogger('polygon') _log.setLevel(logging.ERROR) _log.addHandler(ch)  api_key = ''...*
- **Link:** [View in docs](./polygon_docs.md)

#### `DataFrame`

- **Occurrences:** 2
- **Context:** *...it}"     results = _polygon_request(query_url)     if not results:         return None      df = pd.DataFrame(results)     df['t'] = pd.to_datetime(df['t'], unit='ms')      rename = {'o': 'open', 'h': 'high', ...*
- **Link:** [View in docs](./polygon_docs.md)

#### `data_list`

- **Occurrences:** 2
- **Context:** *...send(sec_type, 'auth', api_key)         while 1:             response = await ws.recv()             data_list: List[dict] = json.loads(response)             for i, data in enumerate(data_list):                ...*
- **Link:** [View in docs](./polygon_docs.md)

### E

#### `ERROR`

- **Occurrences:** 2
- **Context:** *...t='%H:%M:%S')) ch.setLevel(logging.DEBUG) _log = logging.getLogger('polygon') _log.setLevel(logging.ERROR) _log.addHandler(ch)  api_key = '' _tickers = {} _set_on_load = []  _lasts = {} _ws = {'stocks': No...*
- **Link:** [View in docs](./polygon_docs.md)

#### `ETH`

- **Occurrences:** 1
- **Context:** *...to data pulled from Polygon.io.\n         :param crypto_pair: The crypto pair to request. (BTC-USD, ETH-BTC etc.)         :param timeframe:   Timeframe to request (1min, 5min, 2H, 1D, 1W, 2M, etc).      ...*
- **Link:** [View in docs](./polygon_docs.md)

#### `end_date`

- **Occurrences:** 41
- **Context:** *...urn         return data['results']   def get_bar_data(ticker: str, timeframe: str, start_date: str, end_date: str, limit: int = 5_000):     end_date = dt.datetime.now().strftime('%Y-%m-%d') if end_date == 'no...*
- **Link:** [View in docs](./polygon_docs.md)

### F

#### `fiat_pair`

- **Occurrences:** 5
- **Context:** *...es', f'I:{symbol}', timeframe, start_date, end_date, limit, live)      def forex(             self, fiat_pair: str, timeframe: str, start_date: str, end_date: str = 'now',             limit: int = 5_000, live:...*
- **Link:** [View in docs](./polygon_docs.md)

### G

#### `GBP`

- **Occurrences:** 1
- **Context:** *...orex data pulled from Polygon.io.\n         :param fiat_pair:   The fiat pair to request. (USD-CAD, GBP-JPY etc.)         :param timeframe:   Timeframe to request (1min, 5min, 2H, 1D, 1W, 2M, etc).      ...*
- **Link:** [View in docs](./polygon_docs.md)

#### `get_bar_data`

- **Occurrences:** 2
- **Context:** *...  _log.error(f'No results for {query_url}')             return         return data['results']   def get_bar_data(ticker: str, timeframe: str, start_date: str, end_date: str, limit: int = 5_000):     end_date = dt...*
- **Link:** [View in docs](./polygon_docs.md)

#### `get_event_loop`

- **Occurrences:** 1
- **Context:** *...ef __init__(self, chart):         self._chart = chart      def set(self, *args):         if asyncio.get_event_loop().is_running():             asyncio.create_task(self.async_set(*args))             return True     ...*
- **Link:** [View in docs](./polygon_docs.md)

#### `get_running_loop`

- **Occurrences:** 1
- **Context:** *...icker: str, timeframe: str, start_date: str, end_date: str, limit: int = 5_000):     loop = asyncio.get_running_loop()     return await loop.run_in_executor(None, get_bar_data, ticker, timeframe, start_date, end_date...*
- **Link:** [View in docs](./polygon_docs.md)

### H

#### `horz_visible`

- **Occurrences:** 2
- **Context:** *...       self.legend(True)         self.grid(False, False)         self.crosshair(vert_visible=False, horz_visible=False)          self.topbar.textbox('symbol')         self.topbar.switcher('timeframe', timeframe_o...*
- **Link:** [View in docs](./polygon_docs.md)

### I

#### `INFO`

- **Occurrences:** 1
- **Context:** *...    Streams informational messages related to Polygon.io.         """         _log.setLevel(logging.INFO) if info else _log.setLevel(logging.ERROR)      @staticmethod     def api_key(key: str):         ""...*
- **Link:** [View in docs](./polygon_docs.md)

#### `ImportError`

- **Occurrences:** 2
- **Context:** *...teral, Union, List import pandas as pd  from .chart import Chart  try:     import websockets except ImportError:     websockets = None  SEC_TYPE = Literal['stocks', 'options', 'indices', 'forex', 'crypto']  ch =...*
- **Link:** [View in docs](./polygon_docs.md)

#### `IndexError`

- **Occurrences:** 1
- **Context:** *...      'M': 'month',     }     try:         multiplier = re.findall(r'\d+', timeframe)[0]     except IndexError:         return 1, spans[timeframe]     timespan = spans[timeframe.replace(multiplier, '')]     ret...*
- **Link:** [View in docs](./polygon_docs.md)

#### `is_running`

- **Occurrences:** 1
- **Context:** *... chart):         self._chart = chart      def set(self, *args):         if asyncio.get_event_loop().is_running():             asyncio.create_task(self.async_set(*args))             return True         else:    ...*
- **Link:** [View in docs](./polygon_docs.md)

### J

#### `JPY`

- **Occurrences:** 1
- **Context:** *... data pulled from Polygon.io.\n         :param fiat_pair:   The fiat pair to request. (USD-CAD, GBP-JPY etc.)         :param timeframe:   Timeframe to request (1min, 5min, 2H, 1D, 1W, 2M, etc).         :...*
- **Link:** [View in docs](./polygon_docs.md)

### K

#### `keep_drawings`

- **Occurrences:** 1
- **Context:** *...ait async_get_bar_data(ticker, timeframe, start_date, end_date, limit)          self._chart.set(df, keep_drawings=_tickers.get(self._chart) == ticker)         _tickers[self._chart] = ticker          if not live:  ...*
- **Link:** [View in docs](./polygon_docs.md)

### L

#### `lightweight_charts`

- **Occurrences:** 1
- **Context:** *...rl += f'&apiKey={api_key}'      request = urllib.request.Request(query_url, headers={'User-Agent': 'lightweight_charts/1.0'})     with urllib.request.urlopen(request) as response:         if response.status != 200:    ...*
- **Link:** [View in docs](./polygon_docs.md)

### M

#### `muted_background_color`

- **Occurrences:** 1
- **Context:** *...e         self.win.style(             active_background_color='rgba(91, 98, 246, 0.8)',             muted_background_color='rgba(91, 98, 246, 0.5)'         )         self.polygon.api_key(api_key)         self.events.search...*
- **Link:** [View in docs](./polygon_docs.md)

### N

#### `num_bars`

- **Occurrences:** 4
- **Context:** *...nc` can also be used.     """     def __init__(             self, api_key: str, live: bool = False, num_bars: int = 200, end_date: str = 'now', limit: int = 5_000,             timeframe_options: tuple = ('1mi...*
- **Link:** [View in docs](./polygon_docs.md)

#### `num_decimals`

- **Occurrences:** 1
- **Context:** *...n True         await subscribe(ticker, sec_type, self._chart.update_from_tick, (True,), self._chart.num_decimals)         return True      def stock(             self, symbol: str, timeframe: str, start_date: str...*
- **Link:** [View in docs](./polygon_docs.md)

### O

#### `on_search`

- **Occurrences:** 2
- **Context:** *..., 98, 246, 0.5)'         )         self.polygon.api_key(api_key)         self.events.search += self.on_search         self.legend(True)         self.grid(False, False)         self.crosshair(vert_visible=False...*
- **Link:** [View in docs](./polygon_docs.md)

#### `on_top`

- **Occurrences:** 2
- **Context:** *...oolbox: bool = True, width: int = 800, height: int = 600, x: int = None, y: int = None,             on_top: bool = False, maximize: bool = False, debug: bool = False,             title: str = '', screen: in...*
- **Link:** [View in docs](./polygon_docs.md)

### P

#### `PolygonAPI`

- **Occurrences:** 1
- **Context:** *...mbol'] = ticker     for func, args in lasts['funcs']:         func(pd.Series(lasts), *args)   class PolygonAPI:     """     Offers direct access to Polygon API data within all Chart objects.      It is not desi...*
- **Link:** [View in docs](./polygon_docs.md)

#### `PolygonChart`

- **Occurrences:** 1
- **Context:** *...PI key to be used with Polygon.io.         """         global api_key         api_key = key   class PolygonChart(Chart):     """     A prebuilt callback chart object allowing for a standalone, plug-and-play     e...*
- **Link:** [View in docs](./polygon_docs.md)

### Q

#### `query_url`

- **Occurrences:** 8
- **Context:** *...(prefix):             return security_type     else:         return 'stocks'   def _polygon_request(query_url):     query_url = 'https://api.polygon.io'+query_url     query_url += f'&apiKey={api_key}'      req...*
- **Link:** [View in docs](./polygon_docs.md)

### R

#### `remaining_bars`

- **Occurrences:** 3
- **Context:** *...tetime.now() if self.end_date == 'now' else dt.datetime.strptime(self.end_date, '%Y-%m-%d')         remaining_bars = self.num_bars         while remaining_bars > 0:             start_date -= delta             if st...*
- **Link:** [View in docs](./polygon_docs.md)

#### `run_in_executor`

- **Occurrences:** 1
- **Context:** *...tr, end_date: str, limit: int = 5_000):     loop = asyncio.get_running_loop()     return await loop.run_in_executor(None, get_bar_data, ticker, timeframe, start_date, end_date, limit)   async def _send(sec_type: SEC...*
- **Link:** [View in docs](./polygon_docs.md)

#### `run_script`

- **Occurrences:** 1
- **Context:** *... self.topbar.switcher('security', security_options, func=self._on_security_selection)          self.run_script(f'''         {self.id}.search.window.style.display = "flex"         {self.id}.search.box.focus()   ...*
- **Link:** [View in docs](./polygon_docs.md)

### S

#### `SEC_TYPE`

- **Occurrences:** 3
- **Context:** *...pd  from .chart import Chart  try:     import websockets except ImportError:     websockets = None  SEC_TYPE = Literal['stocks', 'options', 'indices', 'forex', 'crypto']  ch = logging.StreamHandler() ch.setFo...*
- **Link:** [View in docs](./polygon_docs.md)

#### `StreamHandler`

- **Occurrences:** 1
- **Context:** *...sockets = None  SEC_TYPE = Literal['stocks', 'options', 'indices', 'forex', 'crypto']  ch = logging.StreamHandler() ch.setFormatter(logging.Formatter('%(asctime)s | [polygon.io] %(levelname)s: %(message)s', datefm...*
- **Link:** [View in docs](./polygon_docs.md)

#### `searched_string`

- **Occurrences:** 3
- **Context:** *... self.crosshair() if success else None         return success      async def on_search(self, chart, searched_string):         chart.topbar['symbol'].set(searched_string if await self._polygon(searched_string) else '...*
- **Link:** [View in docs](./polygon_docs.md)

#### `sec_type`

- **Occurrences:** 27
- **Context:** *...n_in_executor(None, get_bar_data, ticker, timeframe, start_date, end_date, limit)   async def _send(sec_type: SEC_TYPE, action: str, params: str):     ws = _ws[sec_type]     while ws is None:         await as...*
- **Link:** [View in docs](./polygon_docs.md)

#### `security_options`

- **Occurrences:** 2
- **Context:** *...nt = 5_000,             timeframe_options: tuple = ('1min', '5min', '30min', 'D', 'W'),             security_options: tuple = ('Stock', 'Option', 'Index', 'Forex', 'Crypto'),             toolbox: bool = True, width: ...*
- **Link:** [View in docs](./polygon_docs.md)

#### `security_type`

- **Occurrences:** 2
- **Context:** *... timespan   def _get_sec_type(ticker):     if '/' in ticker:         return 'forex'     for prefix, security_type in zip(('O:', 'I:', 'C:', 'X:'), ('options', 'indices', 'forex', 'crypto')):         if ticker.star...*
- **Link:** [View in docs](./polygon_docs.md)

#### `short_delta`

- **Occurrences:** 2
- **Context:** *...ame(self.topbar['timeframe'].value)         delta = dt.timedelta(**{span + 's': int(mult)})         short_delta = (delta < dt.timedelta(days=7))         start_date = dt.datetime.now() if self.end_date == 'now' e...*
- **Link:** [View in docs](./polygon_docs.md)

#### `show_async`

- **Occurrences:** 1
- **Context:** *...t window.      If using the standard `show` method, the `block` parameter must be set to True.     `show_async` can also be used.     """     def __init__(             self, api_key: str, live: bool = False, nu...*
- **Link:** [View in docs](./polygon_docs.md)

#### `start_date`

- **Occurrences:** 39
- **Context:** *...)             return         return data['results']   def get_bar_data(ticker: str, timeframe: str, start_date: str, end_date: str, limit: int = 5_000):     end_date = dt.datetime.now().strftime('%Y-%m-%d') if ...*
- **Link:** [View in docs](./polygon_docs.md)

### T

#### `ticker_key`

- **Occurrences:** 2
- **Context:** *...ImportError('The "websockets" library was not found, and must be installed to pull live data.')     ticker_key = {         'stocks': 'sym',         'options': 'sym',         'indices': 'T',         'forex': 'p'...*
- **Link:** [View in docs](./polygon_docs.md)

#### `timeframe_options`

- **Occurrences:** 2
- **Context:** *...tr, live: bool = False, num_bars: int = 200, end_date: str = 'now', limit: int = 5_000,             timeframe_options: tuple = ('1min', '5min', '30min', 'D', 'W'),             security_options: tuple = ('Stock', 'Opti...*
- **Link:** [View in docs](./polygon_docs.md)

#### `to_datetime`

- **Occurrences:** 3
- **Context:** *...query_url)     if not results:         return None      df = pd.DataFrame(results)     df['t'] = pd.to_datetime(df['t'], unit='ms')      rename = {'o': 'open', 'h': 'high', 'l': 'low', 'c': 'close', 't': 'time'}...*
- **Link:** [View in docs](./polygon_docs.md)

### U

#### `USD`

- **Occurrences:** 2
- **Context:** *...isplays forex data pulled from Polygon.io.\n         :param fiat_pair:   The fiat pair to request. (USD-CAD, GBP-JPY etc.)         :param timeframe:   Timeframe to request (1min, 5min, 2H, 1D, 1W, 2M, et...*
- **Link:** [View in docs](./polygon_docs.md)

#### `update_from_tick`

- **Occurrences:** 2
- **Context:** *...,                         start_date, end_date, limit, live):         await unsubscribe(self._chart.update_from_tick)          df = await async_get_bar_data(ticker, timeframe, start_date, end_date, limit)          se...*
- **Link:** [View in docs](./polygon_docs.md)

### V

#### `vert_visible`

- **Occurrences:** 2
- **Context:** *... += self.on_search         self.legend(True)         self.grid(False, False)         self.crosshair(vert_visible=False, horz_visible=False)          self.topbar.textbox('symbol')         self.topbar.switcher('tim...*
- **Link:** [View in docs](./polygon_docs.md)

### Y

#### `YYYY`

- **Occurrences:** 11
- **Context:** *...e to request (1min, 5min, 2H, 1D, 1W, 2M, etc).         :param start_date:  Start date of the data (YYYY-MM-DD).         :param end_date:    End date of the data (YYYY-MM-DD). If left blank, this will be ...*
- **Link:** [View in docs](./polygon_docs.md)

### _

#### `_convert_timeframe`

- **Occurrences:** 3
- **Context:** *...Q', 'A'),     'indices': ('V', None),     'forex': ('C', 'CA'),     'crypto': ('XQ', 'XA'), }   def _convert_timeframe(timeframe):     spans = {         'min': 'minute',         'H': 'hour',         'D': 'day',        ...*
- **Link:** [View in docs](./polygon_docs.md)

#### `_get_sec_type`

- **Occurrences:** 3
- **Context:** *...rame]     timespan = spans[timeframe.replace(multiplier, '')]     return multiplier, timespan   def _get_sec_type(ticker):     if '/' in ticker:         return 'forex'     for prefix, security_type in zip(('O:', '...*
- **Link:** [View in docs](./polygon_docs.md)

#### `_polygon_request`

- **Occurrences:** 2
- **Context:** *...ticker.startswith(prefix):             return security_type     else:         return 'stocks'   def _polygon_request(query_url):     query_url = 'https://api.polygon.io'+query_url     query_url += f'&apiKey={api_key}...*
- **Link:** [View in docs](./polygon_docs.md)

---

*Keywords extracted on 2025-11-18T21:53:49.272743*
