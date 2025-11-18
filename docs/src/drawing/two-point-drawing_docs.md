# two-point-drawing.ts

**File Path:** `src/drawing/two-point-drawing.ts`

**File Size:** 904 bytes
**Lines of Code:** 39
**Language:** typescript

---

## File Metadata

- **Relative Path:** `src/drawing/two-point-drawing.ts`
- **File Type:** .ts
- **Size:** 904 bytes
- **Total Lines:** 39
- **Programming Language:** typescript

## Quick Summary

This file is part of the lightweight-charts-python repository.
 It defines 1 class(es).


## Original Source Code

```typescript

import { Point } from './data-source';
import { DrawingOptions, defaultOptions } from './options';
import { Drawing } from './drawing';
import { TwoPointDrawingPaneView } from './pane-view';


export abstract class TwoPointDrawing extends Drawing {
    _paneViews: TwoPointDrawingPaneView[] = [];

    protected _hovered: boolean = false;

    constructor(
        p1: Point,
        p2: Point,
        options?: Partial<DrawingOptions>
    ) {
        super()
        this.points.push(p1);
        this.points.push(p2);
        this._options = {
            ...defaultOptions,
            ...options,
        };
    }

    setFirstPoint(point: Point) {
        this.updatePoints(point);
    }

    setSecondPoint(point: Point) {
        this.updatePoints(null, point);
    }

    get p1() { return this.points[0]; }
    get p2() { return this.points[1]; }

    get hovered() { return this._hovered; }
}


```

## High-Level Overview

### Classes (1)

- **`TwoPointDrawing`** (line 7)

## Detailed Walkthrough

### Code Structure

This file contains 39 lines of typescript.

#### Classes

##### TwoPointDrawing (Line 7)

## Usage Examples

To use this file in your project:

```javascript
import { ... } from './src/drawing/two-point-drawing.ts';
```

## Performance & Security Notes

### Performance

- File size: 904 bytes
- Complexity: 0 functions, 1 classes

### Security

- **Recommendation:** Review this file for potential security vulnerabilities
- No obvious security concerns detected (basic scan)

## Related Files

*To be populated during folder indexing phase*

## Testing

Tests for this file may be located in the `test/` directory.

---

*Documentation generated on 2025-11-18T21:53:49.071073*
