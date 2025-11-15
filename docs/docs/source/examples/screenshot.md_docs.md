# screenshot.md Documentation

## File Metadata
- **Path**: `docs/source/examples/screenshot.md`
- **Extension**: `.md`
- **Lines of Code**: 28
- **File Size**: 624 bytes

## Original Source

```md
# Screenshot & Save


```python
import pandas as pd
from lightweight_charts import Chart


if __name__ == '__main__':
    chart = Chart()
    df = pd.read_csv('ohlcv.csv')
    chart.set(df)
    chart.show()
    
    img = chart.screenshot()
    with open('screenshot.png', 'wb') as f:
        f.write(img)
```

```{important}
The `screenshot` command can only be executed after the chart window is open. Therefore, either `block` must equal `False`, the screenshot should be triggered with a callback, or `async_show` should be used. 
```

```{important}
This example can only be used with the standard `Chart` object.
```


```

## Overview

This file is located at `docs/source/examples/screenshot.md` and contains 28 lines of code.

## Markdown Document Analysis

### Document Structure

- Screenshot & Save


## Related Files

This file is part of the repository structure. Related files may be found in the same directory or referenced in the code above.

## Tests

To test this file, refer to the repository's test suite in the `test/` directory.

## Performance & Security Notes

- Always review code for potential security vulnerabilities
- Ensure proper error handling is implemented
- Follow best practices for the language/framework being used
