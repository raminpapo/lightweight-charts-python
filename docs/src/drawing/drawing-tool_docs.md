# drawing-tool.ts

**File Path:** `src/drawing/drawing-tool.ts`

**File Size:** 3,777 bytes
**Lines of Code:** 122
**Language:** typescript

---

## File Metadata

- **Relative Path:** `src/drawing/drawing-tool.ts`
- **File Type:** .ts
- **Size:** 3,777 bytes
- **Total Lines:** 122
- **Programming Language:** typescript

## Quick Summary

This file is part of the lightweight-charts-python repository.
 It defines 1 class(es).


## Original Source Code

```typescript

import {
    IChartApi,
    ISeriesApi,
    Logical,
    MouseEventParams,
    SeriesType,
} from 'lightweight-charts';
import { Drawing } from './drawing';
import { HorizontalLine } from '../horizontal-line/horizontal-line';


export class DrawingTool {
    private _chart: IChartApi;
    private _series: ISeriesApi<SeriesType>;
    private _finishDrawingCallback: Function | null = null;

    private _drawings: Drawing[] = [];
    private _activeDrawing: Drawing | null = null;
    private _isDrawing: boolean = false;
    private _drawingType: (new (...args: any[]) => Drawing) | null = null;

    constructor(chart: IChartApi, series: ISeriesApi<SeriesType>, finishDrawingCallback: Function | null = null) {
        this._chart = chart;
        this._series = series;
        this._finishDrawingCallback = finishDrawingCallback;

        this._chart.subscribeClick(this._clickHandler);
        this._chart.subscribeCrosshairMove(this._moveHandler);
    }

    private _clickHandler = (param: MouseEventParams) => this._onClick(param);
    private _moveHandler = (param: MouseEventParams) => this._onMouseMove(param);

    beginDrawing(DrawingType: new (...args: any[]) => Drawing) {
        this._drawingType = DrawingType;
        this._isDrawing = true;
    }

    stopDrawing() {
        this._isDrawing = false;
        this._activeDrawing = null;
    }

    get drawings() {
        return this._drawings;
    }

    addNewDrawing(drawing: Drawing) {
        this._series.attachPrimitive(drawing);
        this._drawings.push(drawing);
    }

    delete(d: Drawing | null) {
        if (d == null) return;
        const idx = this._drawings.indexOf(d);
        if (idx == -1) return;
        this._drawings.splice(idx, 1)
        d.detach();
    }

    clearDrawings() {
        for (const d of this._drawings) d.detach();
        this._drawings = [];
    }

    repositionOnTime() {
        for (const drawing of this.drawings) {
            const newPoints = []
            for (const point of drawing.points) {
                if (!point) {
                    newPoints.push(point);
                    continue;
                }
                const logical = point.time ? this._chart.timeScale()
                    .coordinateToLogical(
                        this._chart.timeScale().timeToCoordinate(point.time) || 0
                    ) : point.logical;
                newPoints.push({
                    time: point.time,
                    logical: logical as Logical,
                    price: point.price,
                })
            }
            drawing.updatePoints(...newPoints);
        }
    }

    private _onClick(param: MouseEventParams) {
        if (!this._isDrawing) return;

        const point = Drawing._eventToPoint(param, this._series);
        if (!point) return;

        if (this._activeDrawing == null) {
            if (this._drawingType == null) return;

            this._activeDrawing = new this._drawingType(point, point);
            this._series.attachPrimitive(this._activeDrawing);
            if (this._drawingType == HorizontalLine) this._onClick(param);
        }
        else {
            this._drawings.push(this._activeDrawing);
            this.stopDrawing();

            if (!this._finishDrawingCallback) return;
            this._finishDrawingCallback();
        }
    }

    private _onMouseMove(param: MouseEventParams) {
        if (!param) return;

        for (const t of this._drawings) t._handleHoverInteraction(param);

        if (!this._isDrawing || !this._activeDrawing) return;

        const point = Drawing._eventToPoint(param, this._series);
        if (!point) return;
        this._activeDrawing.updatePoints(null, point);
        // this._activeDrawing.setSecondPoint(point);
    }
}

```

## High-Level Overview

### Classes (1)

- **`DrawingTool`** (line 12)

## Detailed Walkthrough

### Code Structure

This file contains 122 lines of typescript.

#### Classes

##### DrawingTool (Line 12)

## Usage Examples

To use this file in your project:

```javascript
import { ... } from './src/drawing/drawing-tool.ts';
```

## Performance & Security Notes

### Performance

- File size: 3,777 bytes
- Complexity: 0 functions, 1 classes

### Security

- **Recommendation:** Review this file for potential security vulnerabilities
- No obvious security concerns detected (basic scan)

## Related Files

*To be populated during folder indexing phase*

## Testing

Tests for this file may be located in the `test/` directory.

---

*Documentation generated on 2025-11-18T21:53:49.079980*
