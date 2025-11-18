# global-params.ts

**File Path:** `src/general/global-params.ts`

**File Size:** 1,707 bytes
**Lines of Code:** 63
**Language:** typescript

---

## File Metadata

- **Relative Path:** `src/general/global-params.ts`
- **File Type:** .ts
- **Size:** 1,707 bytes
- **Total Lines:** 63
- **Programming Language:** typescript

## Quick Summary

This file is part of the lightweight-charts-python repository.
 It contains 2 function(s).


## Original Source Code

```typescript

export interface GlobalParams extends Window {
    pane: paneStyle;    // TODO shouldnt need this cause of css variables
    handlerInFocus: string;
    textBoxFocused: boolean;
    callbackFunction: Function;
    containerDiv: HTMLElement;
    setCursor: Function;
    cursor: string;
}

interface paneStyle {
    backgroundColor: string;
    hoverBackgroundColor: string;
    clickBackgroundColor: string;
    activeBackgroundColor: string;
    mutedBackgroundColor: string;
    borderColor: string;
    color: string;
    activeColor: string;
}

export const paneStyleDefault: paneStyle = {
    backgroundColor: '#0c0d0f',
    hoverBackgroundColor: '#3c434c',
    clickBackgroundColor: '#50565E',
    activeBackgroundColor: 'rgba(0, 122, 255, 0.7)',
    mutedBackgroundColor: 'rgba(0, 122, 255, 0.3)',
    borderColor: '#3C434C',
    color: '#d8d9db',
    activeColor: '#ececed',
}

declare const window: GlobalParams;

export function globalParamInit() {
    window.pane = {
        ...paneStyleDefault,
    }
    window.containerDiv = document.getElementById("container") || document.createElement('div');
    window.setCursor = (type: string | undefined) => {
        if (type) window.cursor = type;
        document.body.style.cursor = window.cursor;
    }
    window.cursor = 'default';
    window.textBoxFocused = false;
}

export const setCursor = (type: string | undefined) => {
    if (type) window.cursor = type;
    document.body.style.cursor = window.cursor;
}


// export interface SeriesHandler {
//     type: string;
//     series: ISeriesApi<SeriesType>;
//     markers: SeriesMarker<"">[],
//     horizontal_lines: HorizontalLine[],
//     name?: string,
//     precision: number,
// }



```

## High-Level Overview

### Functions (2)

- **`globalParamInit()`** (line 35)
- **`setCursor()`** (line 48)

## Detailed Walkthrough

### Code Structure

This file contains 63 lines of typescript.

#### Functions

##### globalParamInit (Line 35)

**Parameters:** ``

##### setCursor (Line 48)

**Parameters:** `None`

## Usage Examples

To use this file in your project:

```javascript
import { ... } from './src/general/global-params.ts';
```

## Performance & Security Notes

### Performance

- File size: 1,707 bytes
- Complexity: 2 functions, 0 classes

### Security

- **Recommendation:** Review this file for potential security vulnerabilities
- No obvious security concerns detected (basic scan)

## Related Files

*To be populated during folder indexing phase*

## Testing

Tests for this file may be located in the `test/` directory.

---

*Documentation generated on 2025-11-18T21:53:49.132092*
