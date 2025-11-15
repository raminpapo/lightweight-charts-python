# axis-view.ts Documentation

## File Metadata
- **Path**: `src/horizontal-line/axis-view.ts`
- **Extension**: `.ts`
- **Lines of Code**: 38
- **File Size**: 1140 bytes

## Original Source

```ts
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

## Overview

This file is located at `src/horizontal-line/axis-view.ts` and contains 38 lines of code.

## TypeScript/JavaScript Code Analysis

### Classes

- **HorizontalLineAxisView**: Class implementation

### Exports

- **HorizontalLineAxisView**: Exported symbol


## Related Files

This file is part of the repository structure. Related files may be found in the same directory or referenced in the code above.

## Tests

To test this file, refer to the repository's test suite in the `test/` directory.

## Performance & Security Notes

- Always review code for potential security vulnerabilities
- Ensure proper error handling is implemented
- Follow best practices for the language/framework being used
