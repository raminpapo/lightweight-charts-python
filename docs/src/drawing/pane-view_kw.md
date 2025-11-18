# Keywords: pane-view.ts

**Source File:** `src/drawing/pane-view.ts`
**Total Keywords:** 5

---

## Keyword Index (A-Z)

### D

#### `DrawingPaneRenderer`

- **Occurrences:** 3
- **Context:** *...eight-charts'; import { Drawing } from './drawing'; import { Point } from './data-source'; import { DrawingPaneRenderer } from './pane-renderer'; import { TwoPointDrawing } from './two-point-drawing';   export abstract ...*
- **Link:** [View in docs](./pane-view_docs.md)

#### `DrawingPaneView`

- **Occurrences:** 2
- **Context:** *...m './pane-renderer'; import { TwoPointDrawing } from './two-point-drawing';   export abstract class DrawingPaneView implements ISeriesPrimitivePaneView {     _source: Drawing;      constructor(source: Drawing) {    ...*
- **Link:** [View in docs](./pane-view_docs.md)

### T

#### `TwoPointDrawing`

- **Occurrences:** 3
- **Context:** *...ort { Point } from './data-source'; import { DrawingPaneRenderer } from './pane-renderer'; import { TwoPointDrawing } from './two-point-drawing';   export abstract class DrawingPaneView implements ISeriesPrimitivePa...*
- **Link:** [View in docs](./pane-view_docs.md)

#### `TwoPointDrawingPaneView`

- **Occurrences:** 1
- **Context:** *... interface ViewPoint {     x: Coordinate | null;     y: Coordinate | null; }  export abstract class TwoPointDrawingPaneView extends DrawingPaneView {     _p1: ViewPoint = { x: null, y: null };     _p2: ViewPoint = { x: null...*
- **Link:** [View in docs](./pane-view_docs.md)

### V

#### `ViewPoint`

- **Occurrences:** 3
- **Context:** *...  }      abstract update(): void;     abstract renderer(): DrawingPaneRenderer; }  export interface ViewPoint {     x: Coordinate | null;     y: Coordinate | null; }  export abstract class TwoPointDrawingPaneV...*
- **Link:** [View in docs](./pane-view_docs.md)

---

*Keywords extracted on 2025-11-18T21:53:49.074246*
