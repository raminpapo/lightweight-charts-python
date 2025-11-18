# trend-line.ts

**File Path:** `src/trend-line/trend-line.ts`

**File Size:** 3,747 bytes
**Lines of Code:** 110
**Language:** typescript

---

## File Metadata

- **Relative Path:** `src/trend-line/trend-line.ts`
- **File Type:** .ts
- **Size:** 3,747 bytes
- **Total Lines:** 110
- **Programming Language:** typescript

## Quick Summary

This file is part of the lightweight-charts-python repository.
 It defines 1 class(es).


## Original Source Code

```typescript

import {
    MouseEventParams,
} from 'lightweight-charts';


import { TrendLinePaneView } from './pane-view';
import { Point } from '../drawing/data-source';
import { InteractionState } from '../drawing/drawing';
import { DrawingOptions } from '../drawing/options';
import { TwoPointDrawing } from '../drawing/two-point-drawing';


export class TrendLine extends TwoPointDrawing {
    _type = "TrendLine"

    constructor(
        p1: Point,
        p2: Point,
        options?: Partial<DrawingOptions>
    ) {
        super(p1, p2, options)
        this._paneViews = [new TrendLinePaneView(this)];
    }

    _moveToState(state: InteractionState) {
        switch(state) {

            case InteractionState.NONE:
                document.body.style.cursor = "default";
                this._hovered = false;
                this.requestUpdate();
                this._unsubscribe("mousedown", this._handleMouseDownInteraction);
                break;

            case InteractionState.HOVERING:
                document.body.style.cursor = "pointer";
                this._hovered = true;
                this.requestUpdate();
                this._subscribe("mousedown", this._handleMouseDownInteraction);
                this._unsubscribe("mouseup", this._handleMouseDownInteraction);
                this.chart.applyOptions({handleScroll: true});
                break;

            case InteractionState.DRAGGINGP1:
            case InteractionState.DRAGGINGP2:
            case InteractionState.DRAGGING:
                document.body.style.cursor = "grabbing";
                this._subscribe("mouseup", this._handleMouseUpInteraction);
                this.chart.applyOptions({handleScroll: false});
                break;
        }
        this._state = state;
    }


     _onDrag(diff: any) {
        if (this._state == InteractionState.DRAGGING || this._state == InteractionState.DRAGGINGP1) {
            this._addDiffToPoint(this.p1, diff.logical, diff.price);
        }
        if (this._state == InteractionState.DRAGGING || this._state == InteractionState.DRAGGINGP2) {
            this._addDiffToPoint(this.p2, diff.logical, diff.price);
        }
    }

    protected _onMouseDown() {
        this._startDragPoint = null;
        const hoverPoint = this._latestHoverPoint;
        if (!hoverPoint) return;
        const p1  = this._paneViews[0]._p1;
        const p2  = this._paneViews[0]._p2;

        if (!p1.x || !p2.x || !p1.y || !p2.y) return this._moveToState(InteractionState.DRAGGING);

        const tolerance = 10;
        if (Math.abs(hoverPoint.x-p1.x) < tolerance && Math.abs(hoverPoint.y-p1.y) < tolerance) {
            this._moveToState(InteractionState.DRAGGINGP1)
        }
        else if (Math.abs(hoverPoint.x-p2.x) < tolerance && Math.abs(hoverPoint.y-p2.y) < tolerance) {
            this._moveToState(InteractionState.DRAGGINGP2)
        }
        else {
            this._moveToState(InteractionState.DRAGGING);
        }
    }

    protected _mouseIsOverDrawing(param: MouseEventParams, tolerance = 4) {

        if (!param.point) return false;;

        const x1 = this._paneViews[0]._p1.x;
        const y1 = this._paneViews[0]._p1.y;
        const x2 = this._paneViews[0]._p2.x;
        const y2 = this._paneViews[0]._p2.y;
        if (!x1 || !x2 || !y1 || !y2 ) return false;

        const mouseX = param.point.x;
        const mouseY = param.point.y;

        if (mouseX <= Math.min(x1, x2) - tolerance ||
            mouseX >= Math.max(x1, x2) + tolerance) {
            return false;
        }

        const distance = Math.abs((y2 - y1) * mouseX - (x2 - x1) * mouseY + x2 * y1 - y2 * x1
        ) / Math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2);

        return distance <= tolerance
    }
}


```

## High-Level Overview

### Classes (1)

- **`TrendLine`** (line 13)

## Detailed Walkthrough

### Code Structure

This file contains 110 lines of typescript.

#### Classes

##### TrendLine (Line 13)

```typescript
                document.body.style.cursor = "default";
                this._hovered = false;
                this.requestUpdate();
                this._unsubscribe("mousedown", this._handleMouseDownInteraction);
                break;
```

## Usage Examples

To use this file in your project:

```javascript
import { ... } from './src/trend-line/trend-line.ts';
```

## Performance & Security Notes

### Performance

- File size: 3,747 bytes
- Complexity: 0 functions, 1 classes

### Security

- **Recommendation:** Review this file for potential security vulnerabilities
- No obvious security concerns detected (basic scan)

## Related Files

*To be populated during folder indexing phase*

## Testing

Tests for this file may be located in the `test/` directory.

---

*Documentation generated on 2025-11-18T21:53:49.098682*
