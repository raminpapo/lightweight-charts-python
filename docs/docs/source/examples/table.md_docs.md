# table.md Documentation

## File Metadata
- **Path**: `docs/source/examples/table.md`
- **Extension**: `.md`
- **Lines of Code**: 39
- **File Size**: 1104 bytes

## Original Source

```md
# Table

```python
import pandas as pd
from lightweight_charts import Chart

def on_row_click(row):
    row['PL'] = round(row['PL']+1, 2)
    row.background_color('PL', 'green' if row['PL'] > 0 else 'red')

    table.footer[1] = row['Ticker']

if __name__ == '__main__':
    chart = Chart(width=1000, inner_width=0.7, inner_height=1)
    subchart = chart.create_subchart(width=0.3, height=0.5)
    df = pd.read_csv('ohlcv.csv')
    chart.set(df)
    subchart.set(df)

    table = chart.create_table(width=0.3, height=0.2,
                  headings=('Ticker', 'Quantity', 'Status', '%', 'PL'),
                  widths=(0.2, 0.1, 0.2, 0.2, 0.3),
                  alignments=('center', 'center', 'right', 'right', 'right'),
                  position='left', func=on_row_click)

    table.format('PL', f'£ {table.VALUE}')
    table.format('%', f'{table.VALUE} %')

    table.new_row('SPY', 3, 'Submitted', 0, 0)
    table.new_row('AMD', 1, 'Filled', 25.5, 105.24)
    table.new_row('NVDA', 2, 'Filled', -0.5, -8.24)

    table.footer(2)
    table.footer[0] = 'Selected:'

    chart.show(block=True)

```

```

## Overview

This file is located at `docs/source/examples/table.md` and contains 39 lines of code.

## Markdown Document Analysis

### Document Structure

- Table


## Related Files

This file is part of the repository structure. Related files may be found in the same directory or referenced in the code above.

## Tests

To test this file, refer to the repository's test suite in the `test/` directory.

## Performance & Security Notes

- Always review code for potential security vulnerabilities
- Ensure proper error handling is implemented
- Follow best practices for the language/framework being used
