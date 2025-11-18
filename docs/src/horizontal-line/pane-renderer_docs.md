# pane-renderer.ts

**File Path:** `src/horizontal-line/pane-renderer.ts`

**File Size:** 1,213 bytes
**Lines of Code:** 35
**Language:** typescript

---

## File Metadata

- **Relative Path:** `src/horizontal-line/pane-renderer.ts`
- **File Type:** .ts
- **Size:** 1,213 bytes
- **Total Lines:** 35
- **Programming Language:** typescript

## Quick Summary

This file is part of the lightweight-charts-python repository.
 It defines 1 class(es).


## Original Source Code

```typescript

import { CanvasRenderingTarget2D } from "fancy-canvas";
import { DrawingOptions } from "../drawing/options";
import { DrawingPaneRenderer } from "../drawing/pane-renderer";
import { ViewPoint } from "../drawing/pane-view";
import { setLineStyle } from "../helpers/canvas-rendering";

export class HorizontalLinePaneRenderer extends DrawingPaneRenderer {
    _point: ViewPoint = {x: null, y: null};

    constructor(point: ViewPoint, options: DrawingOptions) {
        super(options);
        this._point = point;
    }

    draw(target: CanvasRenderingTarget2D) {
        target.useBitmapCoordinateSpace(scope => {
            if (this._point.y == null) return;
            const ctx = scope.context;

            const scaledY = Math.round(this._point.y * scope.verticalPixelRatio);
            const scaledX = this._point.x ? this._point.x * scope.horizontalPixelRatio : 0;

            ctx.lineWidth = this._options.width;
            ctx.strokeStyle = this._options.lineColor;
            setLineStyle(ctx, this._options.lineStyle);
            ctx.beginPath();

            ctx.moveTo(scaledX, scaledY);
            ctx.lineTo(scope.bitmapSize.width, scaledY);

            ctx.stroke();
        });
    }

}

```

## High-Level Overview

### Classes (1)

- **`HorizontalLinePaneRenderer`** (line 7)

## Detailed Walkthrough

### Code Structure

This file contains 35 lines of typescript.

#### Classes

##### HorizontalLinePaneRenderer (Line 7)

## Usage Examples

To use this file in your project:

```javascript
import { ... } from './src/horizontal-line/pane-renderer.ts';
```

## Performance & Security Notes

### Performance

- File size: 1,213 bytes
- Complexity: 0 functions, 1 classes

### Security

- **Recommendation:** Review this file for potential security vulnerabilities
- No obvious security concerns detected (basic scan)

## Related Files

*To be populated during folder indexing phase*

## Testing

Tests for this file may be located in the `test/` directory.

---

*Documentation generated on 2025-11-18T21:53:49.034771*
