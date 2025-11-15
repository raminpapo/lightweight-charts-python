# pane-view.ts Documentation

## File Metadata
- **Path**: `src/drawing/pane-view.ts`
- **Extension**: `.ts`
- **Lines of Code**: 54
- **File Size**: 1559 bytes

## Original Source

```ts
import { Coordinate, ISeriesPrimitivePaneView } from 'lightweight-charts';
import { Drawing } from './drawing';
import { Point } from './data-source';
import { DrawingPaneRenderer } from './pane-renderer';
import { TwoPointDrawing } from './two-point-drawing';


export abstract class DrawingPaneView implements ISeriesPrimitivePaneView {
    _source: Drawing;

    constructor(source: Drawing) {
        this._source = source;
    }

    abstract update(): void;
    abstract renderer(): DrawingPaneRenderer;
}

export interface ViewPoint {
    x: Coordinate | null;
    y: Coordinate | null;
}

export abstract class TwoPointDrawingPaneView extends DrawingPaneView {
    _p1: ViewPoint = { x: null, y: null };
    _p2: ViewPoint = { x: null, y: null };

    _source: TwoPointDrawing;

    constructor(source: TwoPointDrawing) {
        super(source);
        this._source = source;
    }

    update() {
        if (!this._source.p1 || !this._source.p2) return;
        const series = this._source.series;
        const y1 = series.priceToCoordinate(this._source.p1.price);
        const y2 = series.priceToCoordinate(this._source.p2.price);
        const x1 = this._getX(this._source.p1);
        const x2 = this._getX(this._source.p2);
        this._p1 = { x: x1, y: y1 };
        this._p2 = { x: x2, y: y2 };
        if (!x1 || !x2 || !y1 || !y2) return;
    }

    abstract renderer(): DrawingPaneRenderer;

    _getX(p: Point) {
        const timeScale = this._source.chart.timeScale();
        return timeScale.logicalToCoordinate(p.logical);
    }
}

```

## Overview

This file is located at `src/drawing/pane-view.ts` and contains 54 lines of code.

## TypeScript/JavaScript Code Analysis

### Interfaces

- **ViewPoint**: Interface definition

### Classes

- **DrawingPaneView**: Class implementation
- **TwoPointDrawingPaneView**: Class implementation

### Exports

- **ViewPoint**: Exported symbol


## Related Files

This file is part of the repository structure. Related files may be found in the same directory or referenced in the code above.

## Tests

To test this file, refer to the repository's test suite in the `test/` directory.

## Performance & Security Notes

- Always review code for potential security vulnerabilities
- Ensure proper error handling is implemented
- Follow best practices for the language/framework being used
