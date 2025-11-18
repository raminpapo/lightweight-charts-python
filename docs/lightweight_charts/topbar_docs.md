# topbar.py

**File Path:** `lightweight_charts/topbar.py`

**File Size:** 4,660 bytes
**Lines of Code:** 129
**Language:** python

---

## File Metadata

- **Relative Path:** `lightweight_charts/topbar.py`
- **File Type:** .py
- **Size:** 4,660 bytes
- **Total Lines:** 129
- **Programming Language:** python

## Quick Summary

This file is part of the lightweight-charts-python repository.
 It defines 6 class(es).


## Original Source Code

```python

import asyncio
from typing import Dict, Literal

from .util import jbool, Pane


ALIGN = Literal['left', 'right']


class Widget(Pane):
    def __init__(self, topbar, value, func: callable = None, convert_boolean=False):
        super().__init__(topbar.win)
        self.value = value

        def wrapper(v):
            if convert_boolean:
                self.value = False if v == 'false' else True
            else:
                self.value = v
            func(topbar._chart)

        async def async_wrapper(v):
            self.value = v
            await func(topbar._chart)

        self.win.handlers[self.id] = async_wrapper if asyncio.iscoroutinefunction(func) else wrapper


class TextWidget(Widget):
    def __init__(self, topbar, initial_text, align, func):
        super().__init__(topbar, value=initial_text, func=func)

        callback_name = f'"{self.id}"' if func else ''

        self.run_script(f'{self.id} = {topbar.id}.makeTextBoxWidget("{initial_text}", "{align}", {callback_name})')

    def set(self, string):
        self.value = string
        self.run_script(f'{self.id}.innerText = "{string}"')


class SwitcherWidget(Widget):
    def __init__(self, topbar, options, default, align, func):
        super().__init__(topbar, value=default, func=func)
        self.options = list(options)
        self.run_script(f'{self.id} = {topbar.id}.makeSwitcher({self.options}, "{default}", "{self.id}", "{align}")')

    def set(self, option):
        if option not in self.options:
            raise ValueError(f"option '{option}' does not exist within {self.options}.")
        self.run_script(f'{self.id}.onItemClicked("{option}")')
        self.value = option


class MenuWidget(Widget):
    def __init__(self, topbar, options, default, separator, align, func):
        super().__init__(topbar, value=default, func=func)
        self.options = list(options)
        self.run_script(f'''
        {self.id} = {topbar.id}.makeMenu({list(options)}, "{default}", {jbool(separator)}, "{self.id}", "{align}")
        ''')

    # TODO this will probably need to be fixed
    def set(self, option):
        if option not in self.options:
            raise ValueError(f"Option {option} not in menu options ({self.options})")
        self.value = option
        self.run_script(f'''
            {self.id}._clickHandler("{option}")
        ''')
        # self.win.handlers[self.id](option)

    def update_items(self, *items: str):
        self.options = list(items)
        self.run_script(f'{self.id}.updateMenuItems({self.options})')


class ButtonWidget(Widget):
    def __init__(self, topbar, button, separator, align, toggle, func):
        super().__init__(topbar, value=False, func=func, convert_boolean=toggle)
        self.run_script(
            f'{self.id} = {topbar.id}.makeButton("{button}", "{self.id}", {jbool(separator)}, true, "{align}", {jbool(toggle)})')

    def set(self, string):
        # self.value = string
        self.run_script(f'{self.id}.elem.innerText = "{string}"')


class TopBar(Pane):
    def __init__(self, chart):
        super().__init__(chart.win)
        self._chart = chart
        self._widgets: Dict[str, Widget] = {}
        self._created = False

    def _create(self):
        if self._created:
            return
        self._created = True
        self.run_script(f'{self.id} = {self._chart.id}.createTopBar()')

    def __getitem__(self, item):
        if widget := self._widgets.get(item):
            return widget
        raise KeyError(f'Topbar widget "{item}" not found.')

    def get(self, widget_name):
        return self._widgets.get(widget_name)

    def switcher(self, name, options: tuple, default: str = None,
                 align: ALIGN = 'left', func: callable = None):
        self._create()
        self._widgets[name] = SwitcherWidget(self, options, default if default else options[0], align, func)

    def menu(self, name, options: tuple, default: str = None, separator: bool = True,
             align: ALIGN = 'left', func: callable = None):
        self._create()
        self._widgets[name] = MenuWidget(self, options, default if default else options[0], separator, align, func)

    def textbox(self, name: str, initial_text: str = '',
                align: ALIGN = 'left', func: callable = None):
        self._create()
        self._widgets[name] = TextWidget(self, initial_text, align, func)

    def button(self, name, button_text: str, separator: bool = True,
               align: ALIGN = 'left', toggle: bool = False, func: callable = None):
        self._create()
        self._widgets[name] = ButtonWidget(self, button_text, separator, align, toggle, func)


```

## High-Level Overview

### Classes (6)

- **`Widget`** (line 10)
- **`TextWidget`** (line 29)
- **`SwitcherWidget`** (line 42)
- **`MenuWidget`** (line 55)
- **`ButtonWidget`** (line 78)
- **`TopBar`** (line 89)

### Imports (3)

- `import asyncio`
- `from typing import Dict, Literal`
- `from .util import jbool, Pane`

## Detailed Walkthrough

### Code Structure

This file contains 129 lines of python.

#### Classes

##### Widget (Line 10)

```python
    def __init__(self, topbar, value, func: callable = None, convert_boolean=False):
        super().__init__(topbar.win)
        self.value = value
```

##### TextWidget (Line 29)

```python
    def __init__(self, topbar, initial_text, align, func):
        super().__init__(topbar, value=initial_text, func=func)
```

##### SwitcherWidget (Line 42)

```python
    def __init__(self, topbar, options, default, align, func):
        super().__init__(topbar, value=default, func=func)
        self.options = list(options)
        self.run_script(f'{self.id} = {topbar.id}.makeSwitcher({self.options}, "{default}", "{self.id}", "{align}")')
```

##### MenuWidget (Line 55)

```python
    def __init__(self, topbar, options, default, separator, align, func):
        super().__init__(topbar, value=default, func=func)
        self.options = list(options)
        self.run_script(f'''
        {self.id} = {topbar.id}.makeMenu({list(options)}, "{default}", {jbool(separator)}, "{self.id}", "{align}")
        ''')
```

##### ButtonWidget (Line 78)

```python
    def __init__(self, topbar, button, separator, align, toggle, func):
        super().__init__(topbar, value=False, func=func, convert_boolean=toggle)
        self.run_script(
            f'{self.id} = {topbar.id}.makeButton("{button}", "{self.id}", {jbool(separator)}, true, "{align}", {jbool(toggle)})')
```

##### TopBar (Line 89)

```python
    def __init__(self, chart):
        super().__init__(chart.win)
        self._chart = chart
        self._widgets: Dict[str, Widget] = {}
        self._created = False
```

## Usage Examples

To use this file in your project:

```python
from lightweight_charts.topbar import *
```

## Performance & Security Notes

### Performance

- File size: 4,660 bytes
- Complexity: 0 functions, 6 classes

### Security

- **Recommendation:** Review this file for potential security vulnerabilities
- No obvious security concerns detected (basic scan)

## Related Files

*To be populated during folder indexing phase*

## Testing

Tests for this file may be located in the `test/` directory.

---

*Documentation generated on 2025-11-18T21:53:49.140244*
