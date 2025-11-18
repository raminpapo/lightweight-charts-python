# pane-renderer.ts

**File Path:** `src/drawing/pane-renderer.ts`

**File Size:** 2,571 bytes
**Lines of Code:** 65
**Language:** typescript

---

## File Metadata

- **Relative Path:** `src/drawing/pane-renderer.ts`
- **File Type:** .ts
- **Size:** 2,571 bytes
- **Total Lines:** 65
- **Programming Language:** typescript

## Quick Summary

This file is part of the lightweight-charts-python repository.
 It defines 2 class(es).


## Original Source Code

```typescript

import { ISeriesPrimitivePaneRenderer } from "lightweight-charts";
import { ViewPoint } from "./pane-view";
import { DrawingOptions } from "./options";
import { BitmapCoordinatesRenderingScope, CanvasRenderingTarget2D } from "fancy-canvas";

export abstract class DrawingPaneRenderer implements ISeriesPrimitivePaneRenderer {
    _options: DrawingOptions;

    constructor(options: DrawingOptions) {
        this._options = options;
    }

    abstract draw(target: CanvasRenderingTarget2D): void;

}

export abstract class TwoPointDrawingPaneRenderer extends DrawingPaneRenderer {
    _p1: ViewPoint;
    _p2: ViewPoint;
    protected _hovered: boolean;

    constructor(p1: ViewPoint, p2: ViewPoint, options: DrawingOptions, hovered: boolean) {
        super(options);
        this._p1 = p1;
        this._p2 = p2;
        this._hovered = hovered;
    }

    abstract draw(target: CanvasRenderingTarget2D): void;

    _getScaledCoordinates(scope: BitmapCoordinatesRenderingScope) {
        if (this._p1.x === null || this._p1.y === null ||
            this._p2.x === null || this._p2.y === null) return null;
        return {
            x1: Math.round(this._p1.x * scope.horizontalPixelRatio),
            y1: Math.round(this._p1.y * scope.verticalPixelRatio),
            x2: Math.round(this._p2.x * scope.horizontalPixelRatio),
            y2: Math.round(this._p2.y * scope.verticalPixelRatio),
        }
    }

    // _drawTextLabel(scope: BitmapCoordinatesRenderingScope, text: string, x: number, y: number, left: boolean) {
    //  scope.context.font = '24px Arial';
    //  scope.context.beginPath();
    //  const offset = 5 * scope.horizontalPixelRatio;
    //  const textWidth = scope.context.measureText(text);
    //  const leftAdjustment = left ? textWidth.width + offset * 4 : 0;
    //  scope.context.fillStyle = this._options.labelBackgroundColor;
    //  scope.context.roundRect(x + offset - leftAdjustment, y - 24, textWidth.width + offset * 2,  24 + offset, 5);
    //  scope.context.fill();
    //  scope.context.beginPath();
    //  scope.context.fillStyle = this._options.labelTextColor;
    //  scope.context.fillText(text, x + offset * 2 - leftAdjustment, y);
    // }

    _drawEndCircle(scope: BitmapCoordinatesRenderingScope, x: number, y: number) {
        const radius = 9
        scope.context.fillStyle = '#000';
        scope.context.beginPath();
        scope.context.arc(x, y, radius, 0, 2 * Math.PI);
        scope.context.stroke();
        scope.context.fill();
        // scope.context.strokeStyle = this._options.lineColor;
    }
}

```

## High-Level Overview

### Classes (2)

- **`DrawingPaneRenderer`** (line 6)
- **`TwoPointDrawingPaneRenderer`** (line 17)

## Detailed Walkthrough

### Code Structure

This file contains 65 lines of typescript.

#### Classes

##### DrawingPaneRenderer (Line 6)

##### TwoPointDrawingPaneRenderer (Line 17)

## Usage Examples

To use this file in your project:

```javascript
import { ... } from './src/drawing/pane-renderer.ts';
```

## Performance & Security Notes

### Performance

- File size: 2,571 bytes
- Complexity: 0 functions, 2 classes

### Security

- **Recommendation:** Review this file for potential security vulnerabilities
- No obvious security concerns detected (basic scan)

## Related Files

*To be populated during folder indexing phase*

## Testing

Tests for this file may be located in the `test/` directory.

---

*Documentation generated on 2025-11-18T21:53:49.068869*
