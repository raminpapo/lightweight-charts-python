# two-point-drawing.ts Documentation

## File Metadata
- **Path**: `src/drawing/two-point-drawing.ts`
- **Extension**: `.ts`
- **Lines of Code**: 39
- **File Size**: 904 bytes

## Original Source

```ts
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

## Overview

This file is located at `src/drawing/two-point-drawing.ts` and contains 39 lines of code.

## TypeScript/JavaScript Code Analysis

### Classes

- **TwoPointDrawing**: Class implementation


## Related Files

This file is part of the repository structure. Related files may be found in the same directory or referenced in the code above.

## Tests

To test this file, refer to the repository's test suite in the `test/` directory.

## Performance & Security Notes

- Always review code for potential security vulnerabilities
- Ensure proper error handling is implemented
- Follow best practices for the language/framework being used
