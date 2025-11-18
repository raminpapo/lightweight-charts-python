# pane-renderer.ts

**File Path:** `src/trend-line/pane-renderer.ts`

**File Size:** 1,591 bytes
**Lines of Code:** 42
**Language:** typescript

---

## File Metadata

- **Relative Path:** `src/trend-line/pane-renderer.ts`
- **File Type:** .ts
- **Size:** 1,591 bytes
- **Total Lines:** 42
- **Programming Language:** typescript

## Quick Summary

This file is part of the lightweight-charts-python repository.
 It defines 1 class(es).


## Original Source Code

```typescript

import { ViewPoint } from "./pane-view";

import { CanvasRenderingTarget2D } from "fancy-canvas";
import { TwoPointDrawingPaneRenderer } from "../drawing/pane-renderer";
import { DrawingOptions } from "../drawing/options";
import { setLineStyle } from "../helpers/canvas-rendering";

export class TrendLinePaneRenderer extends TwoPointDrawingPaneRenderer {
    constructor(p1: ViewPoint, p2: ViewPoint, options: DrawingOptions, hovered: boolean) {
        super(p1, p2, options, hovered);
    }

    draw(target: CanvasRenderingTarget2D) {
        target.useBitmapCoordinateSpace(scope => {
            if (
                this._p1.x === null ||
                this._p1.y === null ||
                this._p2.x === null ||
                this._p2.y === null
            )
                return;
            const ctx = scope.context;

            const scaled = this._getScaledCoordinates(scope);
            if (!scaled) return;

            ctx.lineWidth = this._options.width;
            ctx.strokeStyle = this._options.lineColor;
            setLineStyle(ctx, this._options.lineStyle);
            ctx.beginPath();
            ctx.moveTo(scaled.x1, scaled.y1);
            ctx.lineTo(scaled.x2, scaled.y2);
            ctx.stroke();
            // this._drawTextLabel(scope, this._text1, x1Scaled, y1Scaled, true);
            // this._drawTextLabel(scope, this._text2, x2Scaled, y2Scaled, false);

            if (!this._hovered) return;
            this._drawEndCircle(scope, scaled.x1, scaled.y1);
            this._drawEndCircle(scope, scaled.x2, scaled.y2);
        });
    }
}

```

## High-Level Overview

### Classes (1)

- **`TrendLinePaneRenderer`** (line 8)

## Detailed Walkthrough

### Code Structure

This file contains 42 lines of typescript.

#### Classes

##### TrendLinePaneRenderer (Line 8)

## Usage Examples

To use this file in your project:

```javascript
import { ... } from './src/trend-line/pane-renderer.ts';
```

## Performance & Security Notes

### Performance

- File size: 1,591 bytes
- Complexity: 0 functions, 1 classes

### Security

- **Recommendation:** Review this file for potential security vulnerabilities
- No obvious security concerns detected (basic scan)

## Related Files

*To be populated during folder indexing phase*

## Testing

Tests for this file may be located in the `test/` directory.

---

*Documentation generated on 2025-11-18T21:53:49.095320*
