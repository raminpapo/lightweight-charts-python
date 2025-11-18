# Keywords: trend-line.ts

**Source File:** `src/trend-line/trend-line.ts`
**Total Keywords:** 9

---

## Keyword Index (A-Z)

### D

#### `DRAGGING`

- **Occurrences:** 5
- **Context:** *...onState.DRAGGINGP1:             case InteractionState.DRAGGINGP2:             case InteractionState.DRAGGING:                 document.body.style.cursor = "grabbing";                 this._subscribe("mouseup"...*
- **Link:** [View in docs](./trend-line_docs.md)

#### `DrawingOptions`

- **Occurrences:** 2
- **Context:** *...nt } from '../drawing/data-source'; import { InteractionState } from '../drawing/drawing'; import { DrawingOptions } from '../drawing/options'; import { TwoPointDrawing } from '../drawing/two-point-drawing';   expo...*
- **Link:** [View in docs](./trend-line_docs.md)

### H

#### `HOVERING`

- **Occurrences:** 1
- **Context:** *...down", this._handleMouseDownInteraction);                 break;              case InteractionState.HOVERING:                 document.body.style.cursor = "pointer";                 this._hovered = true;     ...*
- **Link:** [View in docs](./trend-line_docs.md)

### I

#### `InteractionState`

- **Occurrences:** 15
- **Context:** *... { TrendLinePaneView } from './pane-view'; import { Point } from '../drawing/data-source'; import { InteractionState } from '../drawing/drawing'; import { DrawingOptions } from '../drawing/options'; import { TwoPoint...*
- **Link:** [View in docs](./trend-line_docs.md)

### M

#### `MouseEventParams`

- **Occurrences:** 2
- **Context:** *...import {     MouseEventParams, } from 'lightweight-charts';   import { TrendLinePaneView } from './pane-view'; import { Point } f...*
- **Link:** [View in docs](./trend-line_docs.md)

### N

#### `NONE`

- **Occurrences:** 1
- **Context:** *... _moveToState(state: InteractionState) {         switch(state) {              case InteractionState.NONE:                 document.body.style.cursor = "default";                 this._hovered = false;    ...*
- **Link:** [View in docs](./trend-line_docs.md)

### T

#### `TrendLine`

- **Occurrences:** 2
- **Context:** *...../drawing/options'; import { TwoPointDrawing } from '../drawing/two-point-drawing';   export class TrendLine extends TwoPointDrawing {     _type = "TrendLine"      constructor(         p1: Point,         p2: ...*
- **Link:** [View in docs](./trend-line_docs.md)

#### `TrendLinePaneView`

- **Occurrences:** 2
- **Context:** *...import {     MouseEventParams, } from 'lightweight-charts';   import { TrendLinePaneView } from './pane-view'; import { Point } from '../drawing/data-source'; import { InteractionState } f...*
- **Link:** [View in docs](./trend-line_docs.md)

#### `TwoPointDrawing`

- **Occurrences:** 2
- **Context:** *...ionState } from '../drawing/drawing'; import { DrawingOptions } from '../drawing/options'; import { TwoPointDrawing } from '../drawing/two-point-drawing';   export class TrendLine extends TwoPointDrawing {     _type...*
- **Link:** [View in docs](./trend-line_docs.md)

---

*Keywords extracted on 2025-11-18T21:53:49.099801*
