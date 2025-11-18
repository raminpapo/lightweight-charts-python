# Keywords: box.ts

**Source File:** `src/box/box.ts`
**Total Keywords:** 11

---

## Keyword Index (A-Z)

### A

#### `AutoscaleInfo`

- **Occurrences:** 1
- **Context:** *...ew BoxPaneView(this)];     }      // autoscaleInfo(startTimePoint: Logical, endTimePoint: Logical): AutoscaleInfo | null {         // const p1Index = this._pointIndex(this._p1);         // const p2Index = this._po...*
- **Link:** [View in docs](./box_docs.md)

### B

#### `Box`

- **Occurrences:** 2
- **Context:** *...illEnabled: true,     fillColor: 'rgba(255, 255, 255, 0.2)',     ...defaultOptions }   export class Box extends TwoPointDrawing {     _type = "Box";      constructor(         p1: Point,         p2: Point...*
- **Link:** [View in docs](./box_docs.md)

#### `BoxOptions`

- **Occurrences:** 2
- **Context:** *...m './pane-view'; import { TwoPointDrawing } from '../drawing/two-point-drawing';   export interface BoxOptions extends DrawingOptions {     fillEnabled: boolean;     fillColor: string; }  const defaultBoxOption...*
- **Link:** [View in docs](./box_docs.md)

#### `BoxPaneView`

- **Occurrences:** 2
- **Context:** *...'../drawing/drawing'; import { DrawingOptions, defaultOptions } from '../drawing/options'; import { BoxPaneView } from './pane-view'; import { TwoPointDrawing } from '../drawing/two-point-drawing';   export inte...*
- **Link:** [View in docs](./box_docs.md)

### D

#### `DRAGGING`

- **Occurrences:** 6
- **Context:** *...onState.DRAGGINGP3:             case InteractionState.DRAGGINGP4:             case InteractionState.DRAGGING:                 document.body.style.cursor = "grabbing";                 document.body.addEventLis...*
- **Link:** [View in docs](./box_docs.md)

#### `DrawingOptions`

- **Occurrences:** 2
- **Context:** *...nt } from '../drawing/data-source'; import { InteractionState } from '../drawing/drawing'; import { DrawingOptions, defaultOptions } from '../drawing/options'; import { BoxPaneView } from './pane-view'; import { Tw...*
- **Link:** [View in docs](./box_docs.md)

### H

#### `HOVERING`

- **Occurrences:** 1
- **Context:** *...down", this._handleMouseDownInteraction);                 break;              case InteractionState.HOVERING:                 document.body.style.cursor = "pointer";                 this._hovered = true;     ...*
- **Link:** [View in docs](./box_docs.md)

### I

#### `InteractionState`

- **Occurrences:** 22
- **Context:** *...EventParams, } from 'lightweight-charts';  import { Point } from '../drawing/data-source'; import { InteractionState } from '../drawing/drawing'; import { DrawingOptions, defaultOptions } from '../drawing/options'; i...*
- **Link:** [View in docs](./box_docs.md)

### M

#### `MouseEventParams`

- **Occurrences:** 2
- **Context:** *...import {     MouseEventParams, } from 'lightweight-charts';  import { Point } from '../drawing/data-source'; import { Interaction...*
- **Link:** [View in docs](./box_docs.md)

### N

#### `NONE`

- **Occurrences:** 1
- **Context:** *...  _moveToState(state: InteractionState) {         switch(state) {             case InteractionState.NONE:                 document.body.style.cursor = "default";                 this._hovered = false;    ...*
- **Link:** [View in docs](./box_docs.md)

### T

#### `TwoPointDrawing`

- **Occurrences:** 2
- **Context:** *...ns, defaultOptions } from '../drawing/options'; import { BoxPaneView } from './pane-view'; import { TwoPointDrawing } from '../drawing/two-point-drawing';   export interface BoxOptions extends DrawingOptions {     f...*
- **Link:** [View in docs](./box_docs.md)

---

*Keywords extracted on 2025-11-18T21:53:49.065260*
