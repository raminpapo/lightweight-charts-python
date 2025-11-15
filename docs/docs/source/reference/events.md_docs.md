# events.md Documentation

## File Metadata
- **Path**: `docs/source/reference/events.md`
- **Extension**: `.md`
- **Lines of Code**: 34
- **File Size**: 841 bytes

## Original Source

```md
# `Events`

````{py:class} AbstractChart.Events
The chart events class, accessed through `chart.events`

Events allow asynchronous and synchronous callbacks to be passed back into python.

Chart events can be subscribed to using: `chart.events.<name> += <callable>`

```{py:method} search -> (chart: Chart, string: str)
Fires upon searching. Searchbox will be automatically created.

```

```{py:method} new_bar -> (chart: Chart)
Fires when a new candlestick is added to the chart.

```

```{py:method} range_change -> (chart: Chart, bars_before: NUM, bars_after: NUM)
Fires when the range (visibleLogicalRange) changes.

```

```{py:method} click -> (chart: Chart, time: NUM, price: NUM)
Fires when the mouse is clicked, returning the time and price of the clicked location.

```

````

Tutorial: [Topbar & Events](../tutorials/events.md)


```

## Overview

This file is located at `docs/source/reference/events.md` and contains 34 lines of code.

## Markdown Document Analysis

### Document Structure

- `Events`


## Related Files

This file is part of the repository structure. Related files may be found in the same directory or referenced in the code above.

## Tests

To test this file, refer to the repository's test suite in the `test/` directory.

## Performance & Security Notes

- Always review code for potential security vulnerabilities
- Ensure proper error handling is implemented
- Follow best practices for the language/framework being used
