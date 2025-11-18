# Keywords: table.py

**Source File:** `lightweight_charts/table.py`
**Total Keywords:** 23

---

## Keyword Index (A-Z)

### A

#### `async_wrapper`

- **Occurrences:** 2
- **Context:** *...          func(self[rId], cId)             else:                 func(self[rId])          async def async_wrapper(rId, cId=None):             if return_clicked_cells:                 await func(self[rId], cId)    ...*
- **Link:** [View in docs](./table_docs.md)

### B

#### `background_color`

- **Occurrences:** 3
- **Context:** *....id}", "{column}", "{value}")')         return super().__setitem__(column, original_value)      def background_color(self, column, color): self._style('backgroundColor', column, color)      def text_color(self, colum...*
- **Link:** [View in docs](./table_docs.md)

#### `border_color`

- **Occurrences:** 2
- **Context:** *...t',             draggable: bool = False,             background_color: str = '#121417',             border_color: str = 'rgb(70, 70, 70)',             border_width: int = 1,             heading_text_colors: Optio...*
- **Link:** [View in docs](./table_docs.md)

#### `border_width`

- **Occurrences:** 2
- **Context:** *...  background_color: str = '#121417',             border_color: str = 'rgb(70, 70, 70)',             border_width: int = 1,             heading_text_colors: Optional[tuple] = None,             heading_background_c...*
- **Link:** [View in docs](./table_docs.md)

### C

#### `CELL__`

- **Occurrences:** 1
- **Context:** *...Row('{self.id}')")         self._table.pop(self.id)           class Table(Pane, dict):     VALUE = 'CELL__~__VALUE__~__PLACEHOLDER'      def __init__(             self,             window,             width...*
- **Link:** [View in docs](./table_docs.md)

### E

#### `EventListener`

- **Occurrences:** 1
- **Context:** *....display = '{'flex' if visible else 'none'}'         {self.id}._div.{'add' if visible else 'remove'}EventListener('mousedown', {self.id}.onMouseDown)         """) ...*
- **Link:** [View in docs](./table_docs.md)

### F

#### `format_str`

- **Occurrences:** 2
- **Context:** *...f __getitem__(self, item): return super().__getitem__(int(item))      def format(self, column: str, format_str: str): self._formatters[column] = format_str      def resize(self, width: NUM, height: NUM): self.r...*
- **Link:** [View in docs](./table_docs.md)

### H

#### `heading_background_colors`

- **Occurrences:** 3
- **Context:** *...        border_width: int = 1,             heading_text_colors: Optional[tuple] = None,             heading_background_colors: Optional[tuple] = None,             return_clicked_cells: bool = False,             func: Optional...*
- **Link:** [View in docs](./table_docs.md)

#### `heading_text_colors`

- **Occurrences:** 3
- **Context:** *...,             border_color: str = 'rgb(70, 70, 70)',             border_width: int = 1,             heading_text_colors: Optional[tuple] = None,             heading_background_colors: Optional[tuple] = None,            ...*
- **Link:** [View in docs](./table_docs.md)

### I

#### `is_shown`

- **Occurrences:** 2
- **Context:** *....__init__(self, window)         self._formatters = {}         self.headings = headings         self.is_shown = True         def wrapper(rId, cId=None):             if return_clicked_cells:                 fun...*
- **Link:** [View in docs](./table_docs.md)

### N

#### `NUM`

- **Occurrences:** 5
- **Context:** *... asyncio import random from typing import Union, Optional, Callable  from .util import jbool, Pane, NUM   class Section(Pane):     def __init__(self, table, section_type):         super().__init__(table....*
- **Link:** [View in docs](./table_docs.md)

#### `new_row`

- **Occurrences:** 1
- **Context:** *...       self.footer = Section(self, 'footer')         self.header = Section(self, 'header')      def new_row(self, *values, id=None) -> Row:         row_id = random.randint(0, 99_999_999) if not id else id   ...*
- **Link:** [View in docs](./table_docs.md)

#### `number_of_text_boxes`

- **Occurrences:** 2
- **Context:** *...t__(table.win)         self._table = table         self.type = section_type      def __call__(self, number_of_text_boxes: int, func: Optional[Callable] = None):         if func is not None:             self.win.handlers[...*
- **Link:** [View in docs](./table_docs.md)

### O

#### `original_value`

- **Occurrences:** 2
- **Context:** *...         [self.__setitem__(col, val) for col, val in zip(column, value)]             return         original_value = value         if column in self._table._formatters:             value = self._table._formatters[c...*
- **Link:** [View in docs](./table_docs.md)

### R

#### `Row`

- **Occurrences:** 4
- **Context:** *...lue):         self.run_script(f'{self._table.id}.{self.type}[{key}].innerText = "{value}"')   class Row(dict):     def __init__(self, table, id, items):         super().__init__()         self.run_script...*
- **Link:** [View in docs](./table_docs.md)

#### `return_clicked_cells`

- **Occurrences:** 6
- **Context:** *...         self.meta = {}         self.run_script(f'{self._table.id}.newRow("{self.id}", {jbool(table.return_clicked_cells)})')         for key, val in items.items():             self[key] = val      def __setitem__(self, ...*
- **Link:** [View in docs](./table_docs.md)

#### `row_id`

- **Occurrences:** 4
- **Context:** *...     self.header = Section(self, 'header')      def new_row(self, *values, id=None) -> Row:         row_id = random.randint(0, 99_999_999) if not id else id         self[row_id] = Row(self, row_id, {heading...*
- **Link:** [View in docs](./table_docs.md)

#### `run_script`

- **Occurrences:** 13
- **Context:** *...:             self.win.handlers[self.id] = lambda boxId: func(self._table, int(boxId))         self.run_script(f'''         {self._table.id}.makeSection("{self.id}", "{self.type}", {number_of_text_boxes}, {"tru...*
- **Link:** [View in docs](./table_docs.md)

### S

#### `Section`

- **Occurrences:** 3
- **Context:** *...ort random from typing import Union, Optional, Callable  from .util import jbool, Pane, NUM   class Section(Pane):     def __init__(self, table, section_type):         super().__init__(table.win)         sel...*
- **Link:** [View in docs](./table_docs.md)

#### `section_type`

- **Occurrences:** 2
- **Context:** *..., Callable  from .util import jbool, Pane, NUM   class Section(Pane):     def __init__(self, table, section_type):         super().__init__(table.win)         self._table = table         self.type = section_type ...*
- **Link:** [View in docs](./table_docs.md)

### T

#### `Table`

- **Occurrences:** 2
- **Context:** *...script(f"{self._table.id}.deleteRow('{self.id}')")         self._table.pop(self.id)           class Table(Pane, dict):     VALUE = 'CELL__~__VALUE__~__PLACEHOLDER'      def __init__(             self,     ...*
- **Link:** [View in docs](./table_docs.md)

#### `text_color`

- **Occurrences:** 1
- **Context:** *...  def background_color(self, column, color): self._style('backgroundColor', column, color)      def text_color(self, column, color): self._style('textColor', column, color)      def _style(self, style, column, ...*
- **Link:** [View in docs](./table_docs.md)

### V

#### `VALUE`

- **Occurrences:** 2
- **Context:** *...in self._table._formatters:             value = self._table._formatters[column].replace(self._table.VALUE, str(value))         self.run_script(f'{self._table.id}.updateCell("{self.id}", "{column}", "{value...*
- **Link:** [View in docs](./table_docs.md)

---

*Keywords extracted on 2025-11-18T21:53:49.249293*
