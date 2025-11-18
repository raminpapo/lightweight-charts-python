# Keywords: topbar.py

**Source File:** `lightweight_charts/topbar.py`
**Total Keywords:** 18

---

## Keyword Index (A-Z)

### A

#### `ALIGN`

- **Occurrences:** 5
- **Context:** *...import asyncio from typing import Dict, Literal  from .util import jbool, Pane   ALIGN = Literal['left', 'right']   class Widget(Pane):     def __init__(self, topbar, value, func: callab...*
- **Link:** [View in docs](./topbar_docs.md)

#### `async_wrapper`

- **Occurrences:** 2
- **Context:** *...            else:                 self.value = v             func(topbar._chart)          async def async_wrapper(v):             self.value = v             await func(topbar._chart)          self.win.handlers[sel...*
- **Link:** [View in docs](./topbar_docs.md)

### B

#### `ButtonWidget`

- **Occurrences:** 2
- **Context:** *...options = list(items)         self.run_script(f'{self.id}.updateMenuItems({self.options})')   class ButtonWidget(Widget):     def __init__(self, topbar, button, separator, align, toggle, func):         super().__...*
- **Link:** [View in docs](./topbar_docs.md)

#### `button_text`

- **Occurrences:** 2
- **Context:** *...      self._widgets[name] = TextWidget(self, initial_text, align, func)      def button(self, name, button_text: str, separator: bool = True,                align: ALIGN = 'left', toggle: bool = False, func: cal...*
- **Link:** [View in docs](./topbar_docs.md)

### C

#### `callback_name`

- **Occurrences:** 2
- **Context:** *...nitial_text, align, func):         super().__init__(topbar, value=initial_text, func=func)          callback_name = f'"{self.id}"' if func else ''          self.run_script(f'{self.id} = {topbar.id}.makeTextBoxWidg...*
- **Link:** [View in docs](./topbar_docs.md)

#### `convert_boolean`

- **Occurrences:** 3
- **Context:** *...'left', 'right']   class Widget(Pane):     def __init__(self, topbar, value, func: callable = None, convert_boolean=False):         super().__init__(topbar.win)         self.value = value          def wrapper(v):   ...*
- **Link:** [View in docs](./topbar_docs.md)

### I

#### `initial_text`

- **Occurrences:** 5
- **Context:** *...o.iscoroutinefunction(func) else wrapper   class TextWidget(Widget):     def __init__(self, topbar, initial_text, align, func):         super().__init__(topbar, value=initial_text, func=func)          callback_na...*
- **Link:** [View in docs](./topbar_docs.md)

### K

#### `KeyError`

- **Occurrences:** 1
- **Context:** *...(self, item):         if widget := self._widgets.get(item):             return widget         raise KeyError(f'Topbar widget "{item}" not found.')      def get(self, widget_name):         return self._widgets...*
- **Link:** [View in docs](./topbar_docs.md)

### M

#### `MenuWidget`

- **Occurrences:** 2
- **Context:** *...        self.run_script(f'{self.id}.onItemClicked("{option}")')         self.value = option   class MenuWidget(Widget):     def __init__(self, topbar, options, default, separator, align, func):         super()....*
- **Link:** [View in docs](./topbar_docs.md)

### R

#### `run_script`

- **Occurrences:** 10
- **Context:** *...alue=initial_text, func=func)          callback_name = f'"{self.id}"' if func else ''          self.run_script(f'{self.id} = {topbar.id}.makeTextBoxWidget("{initial_text}", "{align}", {callback_name})')      de...*
- **Link:** [View in docs](./topbar_docs.md)

### S

#### `SwitcherWidget`

- **Occurrences:** 2
- **Context:** *...):         self.value = string         self.run_script(f'{self.id}.innerText = "{string}"')   class SwitcherWidget(Widget):     def __init__(self, topbar, options, default, align, func):         super().__init__(to...*
- **Link:** [View in docs](./topbar_docs.md)

### T

#### `TODO`

- **Occurrences:** 1
- **Context:** *...eMenu({list(options)}, "{default}", {jbool(separator)}, "{self.id}", "{align}")         ''')      # TODO this will probably need to be fixed     def set(self, option):         if option not in self.option...*
- **Link:** [View in docs](./topbar_docs.md)

#### `TextWidget`

- **Occurrences:** 2
- **Context:** *...elf.win.handlers[self.id] = async_wrapper if asyncio.iscoroutinefunction(func) else wrapper   class TextWidget(Widget):     def __init__(self, topbar, initial_text, align, func):         super().__init__(topbar...*
- **Link:** [View in docs](./topbar_docs.md)

#### `TopBar`

- **Occurrences:** 1
- **Context:** *...    # self.value = string         self.run_script(f'{self.id}.elem.innerText = "{string}"')   class TopBar(Pane):     def __init__(self, chart):         super().__init__(chart.win)         self._chart = cha...*
- **Link:** [View in docs](./topbar_docs.md)

### U

#### `update_items`

- **Occurrences:** 1
- **Context:** *...lf.id}._clickHandler("{option}")         ''')         # self.win.handlers[self.id](option)      def update_items(self, *items: str):         self.options = list(items)         self.run_script(f'{self.id}.updateMe...*
- **Link:** [View in docs](./topbar_docs.md)

### V

#### `ValueError`

- **Occurrences:** 2
- **Context:** *..., "{align}")')      def set(self, option):         if option not in self.options:             raise ValueError(f"option '{option}' does not exist within {self.options}.")         self.run_script(f'{self.id}.onI...*
- **Link:** [View in docs](./topbar_docs.md)

### W

#### `Widget`

- **Occurrences:** 6
- **Context:** *...ping import Dict, Literal  from .util import jbool, Pane   ALIGN = Literal['left', 'right']   class Widget(Pane):     def __init__(self, topbar, value, func: callable = None, convert_boolean=False):        ...*
- **Link:** [View in docs](./topbar_docs.md)

#### `widget_name`

- **Occurrences:** 2
- **Context:** *...      return widget         raise KeyError(f'Topbar widget "{item}" not found.')      def get(self, widget_name):         return self._widgets.get(widget_name)      def switcher(self, name, options: tuple, defau...*
- **Link:** [View in docs](./topbar_docs.md)

---

*Keywords extracted on 2025-11-18T21:53:49.142386*
