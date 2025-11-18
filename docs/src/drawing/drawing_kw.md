# Keywords: drawing.ts

**Source File:** `src/drawing/drawing.ts`
**Total Keywords:** 12

---

## Keyword Index (A-Z)

### D

#### `DRAGGING`

- **Occurrences:** 2
- **Context:** *...{ DrawingPaneView } from './pane-view';  export enum InteractionState {     NONE,     HOVERING,     DRAGGING,     DRAGGINGP1,     DRAGGINGP2,     DRAGGINGP3,     DRAGGINGP4, }  export abstract class Drawing e...*
- **Link:** [View in docs](./drawing_docs.md)

#### `DiffPoint`

- **Occurrences:** 4
- **Context:** *...     SeriesType } from 'lightweight-charts';  import { PluginBase } from '../plugin-base'; import { DiffPoint, Point } from './data-source'; import { DrawingOptions, defaultOptions } from './options'; import {...*
- **Link:** [View in docs](./drawing_docs.md)

#### `DocumentEventMap`

- **Occurrences:** 2
- **Context:** *...     }      get points() {         return this._points;     }      protected _subscribe(name: keyof DocumentEventMap, listener: any) {         document.body.addEventListener(name, listener);         this._listeners.p...*
- **Link:** [View in docs](./drawing_docs.md)

#### `Drawing`

- **Occurrences:** 14
- **Context:** *... DRAGGING,     DRAGGINGP1,     DRAGGINGP2,     DRAGGINGP3,     DRAGGINGP4, }  export abstract class Drawing extends PluginBase {     _paneViews: DrawingPaneView[] = [];     _options: DrawingOptions;      abs...*
- **Link:** [View in docs](./drawing_docs.md)

#### `DrawingOptions`

- **Occurrences:** 4
- **Context:** *...rt { PluginBase } from '../plugin-base'; import { DiffPoint, Point } from './data-source'; import { DrawingOptions, defaultOptions } from './options'; import { DrawingPaneView } from './pane-view';  export enum Int...*
- **Link:** [View in docs](./drawing_docs.md)

#### `DrawingPaneView`

- **Occurrences:** 2
- **Context:** *... Point } from './data-source'; import { DrawingOptions, defaultOptions } from './options'; import { DrawingPaneView } from './pane-view';  export enum InteractionState {     NONE,     HOVERING,     DRAGGING,     DRA...*
- **Link:** [View in docs](./drawing_docs.md)

### H

#### `HOVERING`

- **Occurrences:** 3
- **Context:** *...ions'; import { DrawingPaneView } from './pane-view';  export enum InteractionState {     NONE,     HOVERING,     DRAGGING,     DRAGGINGP1,     DRAGGINGP2,     DRAGGINGP3,     DRAGGINGP4, }  export abstract c...*
- **Link:** [View in docs](./drawing_docs.md)

### I

#### `InteractionState`

- **Occurrences:** 14
- **Context:** *...ons, defaultOptions } from './options'; import { DrawingPaneView } from './pane-view';  export enum InteractionState {     NONE,     HOVERING,     DRAGGING,     DRAGGINGP1,     DRAGGINGP2,     DRAGGINGP3,     DRAGGIN...*
- **Link:** [View in docs](./drawing_docs.md)

### M

#### `MouseEventParams`

- **Occurrences:** 5
- **Context:** *...import {     ISeriesApi,     Logical,     MouseEventParams,     SeriesType } from 'lightweight-charts';  import { PluginBase } from '../plugin-base'; import {...*
- **Link:** [View in docs](./drawing_docs.md)

### N

#### `NONE`

- **Occurrences:** 5
- **Context:** *...rom './options'; import { DrawingPaneView } from './pane-view';  export enum InteractionState {     NONE,     HOVERING,     DRAGGING,     DRAGGINGP1,     DRAGGINGP2,     DRAGGINGP3,     DRAGGINGP4, }  exp...*
- **Link:** [View in docs](./drawing_docs.md)

### P

#### `PluginBase`

- **Occurrences:** 2
- **Context:** *...SeriesApi,     Logical,     MouseEventParams,     SeriesType } from 'lightweight-charts';  import { PluginBase } from '../plugin-base'; import { DiffPoint, Point } from './data-source'; import { DrawingOptions,...*
- **Link:** [View in docs](./drawing_docs.md)

### S

#### `SeriesType`

- **Occurrences:** 2
- **Context:** *...import {     ISeriesApi,     Logical,     MouseEventParams,     SeriesType } from 'lightweight-charts';  import { PluginBase } from '../plugin-base'; import { DiffPoint, Poin...*
- **Link:** [View in docs](./drawing_docs.md)

---

*Keywords extracted on 2025-11-18T21:53:49.078498*
