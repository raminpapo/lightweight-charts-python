# Keywords: horizontal-line.ts

**Source File:** `src/horizontal-line/horizontal-line.ts`
**Total Keywords:** 11

---

## Keyword Index (A-Z)

### D

#### `DRAGGING`

- **Occurrences:** 2
- **Context:** *...chart.applyOptions({handleScroll: true});                 break;              case InteractionState.DRAGGING:                 document.body.style.cursor = "grabbing";                 this._subscribe("mouseup"...*
- **Link:** [View in docs](./horizontal-line_docs.md)

#### `DeepPartial`

- **Occurrences:** 2
- **Context:** *...import {     DeepPartial,     MouseEventParams } from "lightweight-charts"; import { Point } from "../drawing/data-source"; ...*
- **Link:** [View in docs](./horizontal-line_docs.md)

#### `DrawingOptions`

- **Occurrences:** 2
- **Context:** *... "../drawing/data-source"; import { Drawing, InteractionState } from "../drawing/drawing"; import { DrawingOptions } from "../drawing/options"; import { HorizontalLinePaneView } from "./pane-view"; import { GlobalP...*
- **Link:** [View in docs](./horizontal-line_docs.md)

### G

#### `GlobalParams`

- **Occurrences:** 2
- **Context:** *...Options } from "../drawing/options"; import { HorizontalLinePaneView } from "./pane-view"; import { GlobalParams } from "../general/global-params"; import { HorizontalLineAxisView } from "./axis-view";   declare ...*
- **Link:** [View in docs](./horizontal-line_docs.md)

### H

#### `HOVERING`

- **Occurrences:** 1
- **Context:** *...down", this._handleMouseDownInteraction);                 break;              case InteractionState.HOVERING:                 document.body.style.cursor = "pointer";                 this._unsubscribe("mouseup...*
- **Link:** [View in docs](./horizontal-line_docs.md)

#### `HorizontalLine`

- **Occurrences:** 2
- **Context:** *... { HorizontalLineAxisView } from "./axis-view";   declare const window: GlobalParams;  export class HorizontalLine extends Drawing {     _type = 'HorizontalLine';     _paneViews: HorizontalLinePaneView[];     _poin...*
- **Link:** [View in docs](./horizontal-line_docs.md)

#### `HorizontalLineAxisView`

- **Occurrences:** 3
- **Context:** *...inePaneView } from "./pane-view"; import { GlobalParams } from "../general/global-params"; import { HorizontalLineAxisView } from "./axis-view";   declare const window: GlobalParams;  export class HorizontalLine extends Dr...*
- **Link:** [View in docs](./horizontal-line_docs.md)

#### `HorizontalLinePaneView`

- **Occurrences:** 3
- **Context:** *...ionState } from "../drawing/drawing"; import { DrawingOptions } from "../drawing/options"; import { HorizontalLinePaneView } from "./pane-view"; import { GlobalParams } from "../general/global-params"; import { HorizontalL...*
- **Link:** [View in docs](./horizontal-line_docs.md)

### I

#### `InteractionState`

- **Occurrences:** 6
- **Context:** *...rams } from "lightweight-charts"; import { Point } from "../drawing/data-source"; import { Drawing, InteractionState } from "../drawing/drawing"; import { DrawingOptions } from "../drawing/options"; import { Horizont...*
- **Link:** [View in docs](./horizontal-line_docs.md)

### M

#### `MouseEventParams`

- **Occurrences:** 2
- **Context:** *...import {     DeepPartial,     MouseEventParams } from "lightweight-charts"; import { Point } from "../drawing/data-source"; import { Drawing, Inte...*
- **Link:** [View in docs](./horizontal-line_docs.md)

### N

#### `NONE`

- **Occurrences:** 1
- **Context:** *...  _moveToState(state: InteractionState) {         switch(state) {             case InteractionState.NONE:                 document.body.style.cursor = "default";                 this._unsubscribe("mousedo...*
- **Link:** [View in docs](./horizontal-line_docs.md)

---

*Keywords extracted on 2025-11-18T21:53:49.039529*
