# toolbox.md Documentation

## File Metadata
- **Path**: `docs/source/reference/toolbox.md`
- **Extension**: `.md`
- **Lines of Code**: 63
- **File Size**: 1260 bytes

## Original Source

```md
# `ToolBox`

`````{py:class} ToolBox

The Toolbox allows for trendlines, ray lines and horizontal lines to be drawn and edited directly on the chart.

It can be used within any Chart object, and is enabled by setting the `toolbox` parameter to `True` upon Chart declaration.

The following hotkeys can also be used when the Toolbox is enabled:

| Key Cmd            | Action  |
|---                 |---        |
| `alt T`             |  Trendline |
| `alt H`           |  Horizontal Line |
| `alt R`             |  Ray Line  |
| `⌘ Z` or `ctrl Z`  |  Undo |

Right-clicking on a drawing will open a context menu, allowing for color selection, style selection and deletion.
___



````{py:method} save_drawings_under(widget: Widget)

Saves drawings under a specific `topbar` text widget. For example:

```python
chart.toolbox.save_drawings_under(chart.topbar['symbol'])
```

````
___



```{py:method} load_drawings(tag: str)

Loads and displays drawings stored under the tag given.
```
___



```{py:method} import_drawings(file_path: str)

Imports the drawings stored at the JSON file given in `file_path`.

```
___



```{py:method} export_drawings(file_path: str)

Exports all currently saved drawings to the JSON file given in `file_path`.

```

`````




```

## Overview

This file is located at `docs/source/reference/toolbox.md` and contains 63 lines of code.

## Markdown Document Analysis

### Document Structure

- `ToolBox`


## Related Files

This file is part of the repository structure. Related files may be found in the same directory or referenced in the code above.

## Tests

To test this file, refer to the repository's test suite in the `test/` directory.

## Performance & Security Notes

- Always review code for potential security vulnerabilities
- Ensure proper error handling is implemented
- Follow best practices for the language/framework being used
