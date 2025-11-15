# global-params.ts Documentation

## File Metadata
- **Path**: `src/general/global-params.ts`
- **Extension**: `.ts`
- **Lines of Code**: 63
- **File Size**: 1707 bytes

## Original Source

```ts
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

## Overview

This file is located at `src/general/global-params.ts` and contains 63 lines of code.

## TypeScript/JavaScript Code Analysis

### Interfaces

- **GlobalParams**: Interface definition
- **paneStyle**: Interface definition
- **SeriesHandler**: Interface definition

### Functions

- **globalParamInit**: Function implementation

### Exports

- **GlobalParams**: Exported symbol
- **paneStyleDefault**: Exported symbol
- **globalParamInit**: Exported symbol
- **setCursor**: Exported symbol
- **SeriesHandler**: Exported symbol


## Related Files

This file is part of the repository structure. Related files may be found in the same directory or referenced in the code above.

## Tests

To test this file, refer to the repository's test suite in the `test/` directory.

## Performance & Security Notes

- Always review code for potential security vulnerabilities
- Ensure proper error handling is implemented
- Follow best practices for the language/framework being used
