# options.ts

**File Path:** `src/drawing/options.ts`

**File Size:** 277 bytes
**Lines of Code:** 15
**Language:** typescript

---

## File Metadata

- **Relative Path:** `src/drawing/options.ts`
- **File Type:** .ts
- **Size:** 277 bytes
- **Total Lines:** 15
- **Programming Language:** typescript

## Quick Summary

This file is part of the lightweight-charts-python repository.


## Original Source Code

```typescript

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

## High-Level Overview

## Detailed Walkthrough

### Code Structure

This file contains 15 lines of typescript.
## Usage Examples

To use this file in your project:

```javascript
import { ... } from './src/drawing/options.ts';
```

## Performance & Security Notes

### Performance

- File size: 277 bytes
- Complexity: 0 functions, 0 classes

### Security

- **Recommendation:** Review this file for potential security vulnerabilities
- No obvious security concerns detected (basic scan)

## Related Files

*To be populated during folder indexing phase*

## Testing

Tests for this file may be located in the `test/` directory.

---

*Documentation generated on 2025-11-18T21:53:49.065980*
