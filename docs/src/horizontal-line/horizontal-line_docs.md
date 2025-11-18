# horizontal-line.ts

**File Path:** `src/horizontal-line/horizontal-line.ts`

**File Size:** 3,330 bytes
**Lines of Code:** 99
**Language:** typescript

---

## File Metadata

- **Relative Path:** `src/horizontal-line/horizontal-line.ts`
- **File Type:** .ts
- **Size:** 3,330 bytes
- **Total Lines:** 99
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
import { Point } from "../drawing/data-source";
import { Drawing, InteractionState } from "../drawing/drawing";
import { DrawingOptions } from "../drawing/options";
import { HorizontalLinePaneView } from "./pane-view";
import { GlobalParams } from "../general/global-params";
import { HorizontalLineAxisView } from "./axis-view";


declare const window: GlobalParams;

export class HorizontalLine extends Drawing {
    _type = 'HorizontalLine';
    _paneViews: HorizontalLinePaneView[];
    _point: Point;
    private _callbackName: string | null;
    _priceAxisViews: HorizontalLineAxisView[];

    protected _startDragPoint: Point | null = null;

    constructor(point: Point, options: DeepPartial<DrawingOptions>, callbackName=null) {
        super(options)
        this._point = point;
        this._point.time = null;    // time is null for horizontal lines
        this._paneViews = [new HorizontalLinePaneView(this)];
        this._priceAxisViews = [new HorizontalLineAxisView(this)];

        this._callbackName = callbackName;
    }

    public get points() {
        return [this._point];
    }

    public updatePoints(...points: (Point | null)[]) {
        for (const p of points) if (p) this._point.price = p.price;
        this.requestUpdate();
    }

    updateAllViews() {
        this._paneViews.forEach((pw) => pw.update());
        this._priceAxisViews.forEach((tw) => tw.update());
    }

    priceAxisViews() {
        return this._priceAxisViews;
    }

    _moveToState(state: InteractionState) {
        switch(state) {
            case InteractionState.NONE:
                document.body.style.cursor = "default";
                this._unsubscribe("mousedown", this._handleMouseDownInteraction);
                break;

            case InteractionState.HOVERING:
                document.body.style.cursor = "pointer";
                this._unsubscribe("mouseup", this._childHandleMouseUpInteraction);
                this._subscribe("mousedown", this._handleMouseDownInteraction)
                this.chart.applyOptions({handleScroll: true});
                break;

            case InteractionState.DRAGGING:
                document.body.style.cursor = "grabbing";
                this._subscribe("mouseup", this._childHandleMouseUpInteraction);
                this.chart.applyOptions({handleScroll: false});
                break;
        }
        this._state = state;
    }

    _onDrag(diff: any) {
        this._addDiffToPoint(this._point, 0, diff.price);
        this.requestUpdate();
    }

    _mouseIsOverDrawing(param: MouseEventParams, tolerance = 4) {
        if (!param.point) return false;
        const y = this.series.priceToCoordinate(this._point.price);
        if (!y) return false;
        return (Math.abs(y-param.point.y) < tolerance);
    }

    protected _onMouseDown() {
        this._startDragPoint = null;
        const hoverPoint = this._latestHoverPoint;
        if (!hoverPoint) return;
        return this._moveToState(InteractionState.DRAGGING);
    }

    protected _childHandleMouseUpInteraction = () => {
        this._handleMouseUpInteraction();
        if (!this._callbackName) return;
        window.callbackFunction(`${this._callbackName}_~_${this._point.price.toFixed(8)}`);
    }
}

```

## High-Level Overview

### Classes (1)

- **`HorizontalLine`** (line 15)

## Detailed Walkthrough

### Code Structure

This file contains 99 lines of typescript.

#### Classes

##### HorizontalLine (Line 15)

```typescript
                document.body.style.cursor = "default";
                this._unsubscribe("mousedown", this._handleMouseDownInteraction);
                break;
```

## Usage Examples

To use this file in your project:

```javascript
import { ... } from './src/horizontal-line/horizontal-line.ts';
```

## Performance & Security Notes

### Performance

- File size: 3,330 bytes
- Complexity: 0 functions, 1 classes

### Security

- **Recommendation:** Review this file for potential security vulnerabilities
- No obvious security concerns detected (basic scan)

## Related Files

*To be populated during folder indexing phase*

## Testing

Tests for this file may be located in the `test/` directory.

---

*Documentation generated on 2025-11-18T21:53:49.038262*
