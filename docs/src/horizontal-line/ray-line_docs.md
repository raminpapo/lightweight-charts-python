# ray-line.ts

**File Path:** `src/horizontal-line/ray-line.ts`

**File Size:** 1,158 bytes
**Lines of Code:** 35
**Language:** typescript

---

## File Metadata

- **Relative Path:** `src/horizontal-line/ray-line.ts`
- **File Type:** .ts
- **Size:** 1,158 bytes
- **Total Lines:** 35
- **Programming Language:** typescript

## Quick Summary

This file is part of the lightweight-charts-python repository.
 It defines 1 class(es).


## Original Source Code

```typescript

import {
    DeepPartial,
    MouseEventParams
} from "lightweight-charts";
import { DiffPoint, Point } from "../drawing/data-source";
import { DrawingOptions } from "../drawing/options";
import { HorizontalLine } from "./horizontal-line";

export class RayLine extends HorizontalLine {
    _type = 'RayLine';

    constructor(point: Point, options: DeepPartial<DrawingOptions>) {
        super({...point}, options);
        this._point.time = point.time;
    }

    public updatePoints(...points: (Point | null)[]) {
        for (const p of points) if (p) this._point = p;
        this.requestUpdate();
    }

    _onDrag(diff: DiffPoint) {
        this._addDiffToPoint(this._point, diff.logical, diff.price);
        this.requestUpdate();
    }

    _mouseIsOverDrawing(param: MouseEventParams, tolerance = 4) {
        if (!param.point) return false;
        const y = this.series.priceToCoordinate(this._point.price);

        const x = this._point.time ? this.chart.timeScale().timeToCoordinate(this._point.time) : null;
        if (!y || !x) return false;
        return (Math.abs(y-param.point.y) < tolerance && param.point.x > x - tolerance);
    }
}

```

## High-Level Overview

### Classes (1)

- **`RayLine`** (line 9)

## Detailed Walkthrough

### Code Structure

This file contains 35 lines of typescript.

#### Classes

##### RayLine (Line 9)

## Usage Examples

To use this file in your project:

```javascript
import { ... } from './src/horizontal-line/ray-line.ts';
```

## Performance & Security Notes

### Performance

- File size: 1,158 bytes
- Complexity: 0 functions, 1 classes

### Security

- **Recommendation:** Review this file for potential security vulnerabilities
- No obvious security concerns detected (basic scan)

## Related Files

*To be populated during folder indexing phase*

## Testing

Tests for this file may be located in the `test/` directory.

---

*Documentation generated on 2025-11-18T21:53:49.032953*
