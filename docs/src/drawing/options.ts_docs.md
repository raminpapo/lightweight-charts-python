# options.ts Documentation

## File Metadata
- **Path**: `src/drawing/options.ts`
- **Extension**: `.ts`
- **Lines of Code**: 15
- **File Size**: 277 bytes

## Original Source

```ts
import { LineStyle } from "lightweight-charts";


export interface DrawingOptions {
    lineColor: string;
    lineStyle: LineStyle
    width: number;
}

export const defaultOptions: DrawingOptions = {
    lineColor: '#1E80F0',
    lineStyle: LineStyle.Solid,
    width: 4,
};

```

## Overview

This file is located at `src/drawing/options.ts` and contains 15 lines of code.

## TypeScript/JavaScript Code Analysis

### Interfaces

- **DrawingOptions**: Interface definition

### Exports

- **DrawingOptions**: Exported symbol
- **defaultOptions**: Exported symbol


## Related Files

This file is part of the repository structure. Related files may be found in the same directory or referenced in the code above.

## Tests

To test this file, refer to the repository's test suite in the `test/` directory.

## Performance & Security Notes

- Always review code for potential security vulnerabilities
- Ensure proper error handling is implemented
- Follow best practices for the language/framework being used
