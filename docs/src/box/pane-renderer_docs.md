# pane-renderer.ts

**File Path:** `src/box/pane-renderer.ts`

**File Size:** 1,612 bytes
**Lines of Code:** 44
**Language:** typescript

---

## File Metadata

- **Relative Path:** `src/box/pane-renderer.ts`
- **File Type:** .ts
- **Size:** 1,612 bytes
- **Total Lines:** 44
- **Programming Language:** typescript

## Quick Summary

This file is part of the lightweight-charts-python repository.
 It defines 1 class(es).


## Original Source Code

```typescript

import { ViewPoint } from "../drawing/pane-view";
import { CanvasRenderingTarget2D } from "fancy-canvas";
import { TwoPointDrawingPaneRenderer } from "../drawing/pane-renderer";
import { BoxOptions } from "./box";
import { setLineStyle } from "../helpers/canvas-rendering";

export class BoxPaneRenderer extends TwoPointDrawingPaneRenderer {
    declare _options: BoxOptions;

    constructor(p1: ViewPoint, p2: ViewPoint, options: BoxOptions, showCircles: boolean) {
        super(p1, p2, options, showCircles)
    }

    draw(target: CanvasRenderingTarget2D) {
        target.useBitmapCoordinateSpace(scope => {

            const ctx = scope.context;

            const scaled = this._getScaledCoordinates(scope);

            if (!scaled) return;

            ctx.lineWidth = this._options.width;
            ctx.strokeStyle = this._options.lineColor;
            setLineStyle(ctx, this._options.lineStyle)
            ctx.fillStyle = this._options.fillColor;

            const mainX = Math.min(scaled.x1, scaled.x2);
            const mainY = Math.min(scaled.y1, scaled.y2);
            const width = Math.abs(scaled.x1-scaled.x2);
            const height = Math.abs(scaled.y1-scaled.y2);

            ctx.strokeRect(mainX, mainY, width, height);
            ctx.fillRect(mainX, mainY, width, height);

            if (!this._hovered) return;
            this._drawEndCircle(scope, mainX, mainY);
            this._drawEndCircle(scope, mainX+width, mainY);
            this._drawEndCircle(scope, mainX+width, mainY+height);
            this._drawEndCircle(scope, mainX, mainY+height);

        });
    }
}

```

## High-Level Overview

### Classes (1)

- **`BoxPaneRenderer`** (line 7)

## Detailed Walkthrough

### Code Structure

This file contains 44 lines of typescript.

#### Classes

##### BoxPaneRenderer (Line 7)

## Usage Examples

To use this file in your project:

```javascript
import { ... } from './src/box/pane-renderer.ts';
```

## Performance & Security Notes

### Performance

- File size: 1,612 bytes
- Complexity: 0 functions, 1 classes

### Security

- **Recommendation:** Review this file for potential security vulnerabilities
- No obvious security concerns detected (basic scan)

## Related Files

*To be populated during folder indexing phase*

## Testing

Tests for this file may be located in the `test/` directory.

---

*Documentation generated on 2025-11-18T21:53:49.059404*
