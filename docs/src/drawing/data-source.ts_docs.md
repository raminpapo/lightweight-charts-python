# data-source.ts Documentation

## File Metadata
- **Path**: `src/drawing/data-source.ts`
- **Extension**: `.ts`
- **Lines of Code**: 16
- **File Size**: 225 bytes

## Original Source

```ts
import {
    Logical,
    Time,
} from 'lightweight-charts';

export interface Point {
    time: Time | null;
    logical: Logical;
    price: number;
}

export interface DiffPoint {
    logical: number;
    price: number;
}

```

## Overview

This file is located at `src/drawing/data-source.ts` and contains 16 lines of code.

## TypeScript/JavaScript Code Analysis

### Interfaces

- **Point**: Interface definition
- **DiffPoint**: Interface definition

### Exports

- **Point**: Exported symbol
- **DiffPoint**: Exported symbol


## Related Files

This file is part of the repository structure. Related files may be found in the same directory or referenced in the code above.

## Tests

To test this file, refer to the repository's test suite in the `test/` directory.

## Performance & Security Notes

- Always review code for potential security vulnerabilities
- Ensure proper error handling is implemented
- Follow best practices for the language/framework being used
