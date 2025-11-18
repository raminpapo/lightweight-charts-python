# pane-view.ts

**File Path:** `src/drawing/pane-view.ts`

**File Size:** 1,559 bytes
**Lines of Code:** 54
**Language:** typescript

---

## File Metadata

- **Relative Path:** `src/drawing/pane-view.ts`
- **File Type:** .ts
- **Size:** 1,559 bytes
- **Total Lines:** 54
- **Programming Language:** typescript

## Quick Summary

This file is part of the lightweight-charts-python repository.
 It defines 2 class(es).


## Original Source Code

```typescript

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

## High-Level Overview

### Classes (2)

- **`DrawingPaneView`** (line 8)
- **`TwoPointDrawingPaneView`** (line 24)

## Detailed Walkthrough

### Code Structure

This file contains 54 lines of typescript.

#### Classes

##### DrawingPaneView (Line 8)

##### TwoPointDrawingPaneView (Line 24)

## Usage Examples

To use this file in your project:

```javascript
import { ... } from './src/drawing/pane-view.ts';
```

## Performance & Security Notes

### Performance

- File size: 1,559 bytes
- Complexity: 0 functions, 2 classes

### Security

- **Recommendation:** Review this file for potential security vulnerabilities
- No obvious security concerns detected (basic scan)

## Related Files

*To be populated during folder indexing phase*

## Testing

Tests for this file may be located in the `test/` directory.

---

*Documentation generated on 2025-11-18T21:53:49.073145*
