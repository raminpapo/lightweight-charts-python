# topbar.py Documentation

## File Metadata
- **Path**: `lightweight_charts/topbar.py`
- **Extension**: `.py`
- **Lines of Code**: 129
- **File Size**: 4660 bytes

## Original Source

```py
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

## Overview

This file is located at `lightweight_charts/topbar.py` and contains 129 lines of code.

## Python Code Analysis

### Classes

- **Widget**: Class defined in this file
- **TextWidget**: Class defined in this file
- **SwitcherWidget**: Class defined in this file
- **MenuWidget**: Class defined in this file
- **ButtonWidget**: Class defined in this file
- **TopBar**: Class defined in this file

### Functions

- **__init__**(self, topbar, value, func: callable = None, convert_boolean=False): Function implementation
- **wrapper**(v): Function implementation
- **async_wrapper**(v): Function implementation
- **__init__**(self, topbar, initial_text, align, func): Function implementation
- **set**(self, string): Function implementation
- **__init__**(self, topbar, options, default, align, func): Function implementation
- **set**(self, option): Function implementation
- **__init__**(self, topbar, options, default, separator, align, func): Function implementation
- **set**(self, option): Function implementation
- **update_items**(self, *items: str): Function implementation
- **__init__**(self, topbar, button, separator, align, toggle, func): Function implementation
- **set**(self, string): Function implementation
- **__init__**(self, chart): Function implementation
- **_create**(self): Function implementation
- **__getitem__**(self, item): Function implementation
- **get**(self, widget_name): Function implementation
- **switcher**(self, name, options: tuple, default: str = None,
                 align: ALIGN = 'left', func: callable = None): Function implementation
- **menu**(self, name, options: tuple, default: str = None, separator: bool = True,
             align: ALIGN = 'left', func: callable = None): Function implementation
- **textbox**(self, name: str, initial_text: str = '',
                align: ALIGN = 'left', func: callable = None): Function implementation
- **button**(self, name, button_text: str, separator: bool = True,
               align: ALIGN = 'left', toggle: bool = False, func: callable = None): Function implementation

### Dependencies

- asyncio
- Dict, Literal
- jbool, Pane


## Related Files

This file is part of the repository structure. Related files may be found in the same directory or referenced in the code above.

## Tests

To test this file, refer to the repository's test suite in the `test/` directory.

## Performance & Security Notes

- Always review code for potential security vulnerabilities
- Ensure proper error handling is implemented
- Follow best practices for the language/framework being used
