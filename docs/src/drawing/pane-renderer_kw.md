# Keywords: pane-renderer.ts

**Source File:** `src/drawing/pane-renderer.ts`
**Total Keywords:** 5

---

## Keyword Index (A-Z)

### B

#### `BitmapCoordinatesRenderingScope`

- **Occurrences:** 4
- **Context:** *...rts"; import { ViewPoint } from "./pane-view"; import { DrawingOptions } from "./options"; import { BitmapCoordinatesRenderingScope, CanvasRenderingTarget2D } from "fancy-canvas";  export abstract class DrawingPaneRenderer implemen...*
- **Link:** [View in docs](./pane-renderer_docs.md)

### D

#### `DrawingOptions`

- **Occurrences:** 4
- **Context:** *...rimitivePaneRenderer } from "lightweight-charts"; import { ViewPoint } from "./pane-view"; import { DrawingOptions } from "./options"; import { BitmapCoordinatesRenderingScope, CanvasRenderingTarget2D } from "fancy...*
- **Link:** [View in docs](./pane-renderer_docs.md)

#### `DrawingPaneRenderer`

- **Occurrences:** 2
- **Context:** *...mapCoordinatesRenderingScope, CanvasRenderingTarget2D } from "fancy-canvas";  export abstract class DrawingPaneRenderer implements ISeriesPrimitivePaneRenderer {     _options: DrawingOptions;      constructor(options: D...*
- **Link:** [View in docs](./pane-renderer_docs.md)

### T

#### `TwoPointDrawingPaneRenderer`

- **Occurrences:** 1
- **Context:** *...options;     }      abstract draw(target: CanvasRenderingTarget2D): void;  }  export abstract class TwoPointDrawingPaneRenderer extends DrawingPaneRenderer {     _p1: ViewPoint;     _p2: ViewPoint;     protected _hovered: boole...*
- **Link:** [View in docs](./pane-renderer_docs.md)

### V

#### `ViewPoint`

- **Occurrences:** 5
- **Context:** *...import { ISeriesPrimitivePaneRenderer } from "lightweight-charts"; import { ViewPoint } from "./pane-view"; import { DrawingOptions } from "./options"; import { BitmapCoordinatesRenderi...*
- **Link:** [View in docs](./pane-renderer_docs.md)

---

*Keywords extracted on 2025-11-18T21:53:49.069995*
