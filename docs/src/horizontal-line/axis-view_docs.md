# axis-view.ts

**File Path:** `src/horizontal-line/axis-view.ts`

**File Size:** 1,140 bytes
**Lines of Code:** 38
**Language:** typescript

---

## File Metadata

- **Relative Path:** `src/horizontal-line/axis-view.ts`
- **File Type:** .ts
- **Size:** 1,140 bytes
- **Total Lines:** 38
- **Programming Language:** typescript

## Quick Summary

This file is part of the lightweight-charts-python repository.
 It defines 1 class(es).


## Original Source Code

```typescript

import { Coordinate, ISeriesPrimitiveAxisView, PriceFormatBuiltIn } from 'lightweight-charts';
import { HorizontalLine } from './horizontal-line';

export class HorizontalLineAxisView implements ISeriesPrimitiveAxisView {
    _source: HorizontalLine;
    _y: Coordinate | null = null;
    _price: string | null = null;

    constructor(source: HorizontalLine) {
        this._source = source;
    }
    update() {
        if (!this._source.series || !this._source._point) return;
        this._y = this._source.series.priceToCoordinate(this._source._point.price);
        const priceFormat = this._source.series.options().priceFormat as PriceFormatBuiltIn;
        const precision = priceFormat.precision;
        this._price = this._source._point.price.toFixed(precision).toString();
    }
    visible() {
        return true;
    }
    tickVisible() {
        return true;
    }
    coordinate() {
        return this._y ?? 0;
    }
    text() {
        return this._source._options.text || this._price || '';
    }
    textColor() {
        return 'white';
    }
    backColor() {
        return this._source._options.lineColor;
    }
}


```

## High-Level Overview

### Classes (1)

- **`HorizontalLineAxisView`** (line 4)

## Detailed Walkthrough

### Code Structure

This file contains 38 lines of typescript.

#### Classes

##### HorizontalLineAxisView (Line 4)

## Usage Examples

To use this file in your project:

```javascript
import { ... } from './src/horizontal-line/axis-view.ts';
```

## Performance & Security Notes

### Performance

- File size: 1,140 bytes
- Complexity: 0 functions, 1 classes

### Security

- **Recommendation:** Review this file for potential security vulnerabilities
- No obvious security concerns detected (basic scan)

## Related Files

*To be populated during folder indexing phase*

## Testing

Tests for this file may be located in the `test/` directory.

---

*Documentation generated on 2025-11-18T21:53:49.031070*
