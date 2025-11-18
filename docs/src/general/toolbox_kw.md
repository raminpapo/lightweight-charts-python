# Keywords: toolbox.ts

**Source File:** `src/general/toolbox.ts`
**Total Keywords:** 19

---

## Keyword Index (A-Z)

### B

#### `BOX_SVG`

- **Occurrences:** 2
- **Context:** *....67L3.67,14.5z M7.91,14.5L6.5,15.91L5.09,14.5l1.41-1.41L7.91,14.5z"/>';     private static readonly BOX_SVG: string = '<rect x="8" y="6" width="12" height="1"/><rect x="9" y="22" width="11" height="1"/><path...*
- **Link:** [View in docs](./toolbox_docs.md)

### C

#### `ContextMenu`

- **Occurrences:** 2
- **Context:** *...end-line"; import { Box } from "../box/box"; import { Drawing } from "../drawing/drawing"; import { ContextMenu } from "../context-menu/context-menu"; import { GlobalParams } from "./global-params"; import { ICh...*
- **Link:** [View in docs](./toolbox_docs.md)

### D

#### `DrawingTool`

- **Occurrences:** 3
- **Context:** *...import { DrawingTool } from "../drawing/drawing-tool"; import { TrendLine } from "../trend-line/trend-line"; import { Bo...*
- **Link:** [View in docs](./toolbox_docs.md)

#### `DrawingType`

- **Occurrences:** 2
- **Context:** *...       div.appendChild(button);         }         return div     }      private _makeToolBoxElement(DrawingType: new (...args: any[]) => Drawing, keyCmd: string, paths: string, rotate=false) {         const elem...*
- **Link:** [View in docs](./toolbox_docs.md)

### G

#### `GlobalParams`

- **Occurrences:** 2
- **Context:** *...g } from "../drawing/drawing"; import { ContextMenu } from "../context-menu/context-menu"; import { GlobalParams } from "./global-params"; import { IChartApi, ISeriesApi, SeriesType } from "lightweight-charts"; i...*
- **Link:** [View in docs](./toolbox_docs.md)

### H

#### `HORZ_SVG`

- **Occurrences:** 2
- **Context:** *...6,25.83L8.83,23L6,20.17z M6,24.41L4.59,23L6,21.59L7.41,23L6,24.41z"/>';     private static readonly HORZ_SVG: string = '<rect x="4" y="14" width="9" height="1"/><rect x="16" y="14" width="9" height="1"/><path...*
- **Link:** [View in docs](./toolbox_docs.md)

#### `HorizontalLine`

- **Occurrences:** 4
- **Context:** *..."./global-params"; import { IChartApi, ISeriesApi, SeriesType } from "lightweight-charts"; import { HorizontalLine } from "../horizontal-line/horizontal-line"; import { RayLine } from "../horizontal-line/ray-line";...*
- **Link:** [View in docs](./toolbox_docs.md)

### J

#### `JSON`

- **Occurrences:** 1
- **Context:** *...nts: d.points,                 options: d._options             });         }         const string = JSON.stringify(drawingMeta);         window.callbackFunction(`save_drawings${this._handlerID}_~_${string...*
- **Link:** [View in docs](./toolbox_docs.md)

### K

#### `KeyboardEvent`

- **Occurrences:** 2
- **Context:** *...      new ContextMenu(this.saveDrawings, this._drawingTool);          commandFunctions.push((event: KeyboardEvent) => {             if ((event.metaKey || event.ctrlKey) && event.code === 'KeyZ') {                 ...*
- **Link:** [View in docs](./toolbox_docs.md)

### R

#### `RAY_SVG`

- **Occurrences:** 3
- **Context:** *...1.67,14.5z M15.91,14.5l-1.41,1.41l-1.41-1.41l1.41-1.41L15.91,14.5z"/>';     private static readonly RAY_SVG: string = '<rect x="8" y="14" width="17" height="1"/><path d="M3.67,14.5l2.83,2.83l2.83-2.83L6.5,11...*
- **Link:** [View in docs](./toolbox_docs.md)

#### `RayLine`

- **Occurrences:** 4
- **Context:** *..."lightweight-charts"; import { HorizontalLine } from "../horizontal-line/horizontal-line"; import { RayLine } from "../horizontal-line/ray-line"; import { VerticalLine } from "../vertical-line/vertical-line"...*
- **Link:** [View in docs](./toolbox_docs.md)

### S

#### `SeriesType`

- **Occurrences:** 2
- **Context:** *...menu/context-menu"; import { GlobalParams } from "./global-params"; import { IChartApi, ISeriesApi, SeriesType } from "lightweight-charts"; import { HorizontalLine } from "../horizontal-line/horizontal-line"; i...*
- **Link:** [View in docs](./toolbox_docs.md)

#### `save_drawings`

- **Occurrences:** 1
- **Context:** *... });         }         const string = JSON.stringify(drawingMeta);         window.callbackFunction(`save_drawings${this._handlerID}_~_${string}`)     }      loadDrawings(drawings: any[]) { // TODO any         draw...*
- **Link:** [View in docs](./toolbox_docs.md)

### T

#### `TODO`

- **Occurrences:** 1
- **Context:** *...nction(`save_drawings${this._handlerID}_~_${string}`)     }      loadDrawings(drawings: any[]) { // TODO any         drawings.forEach((d) => {             switch (d.type) {                 case "Box":    ...*
- **Link:** [View in docs](./toolbox_docs.md)

#### `TREND_SVG`

- **Occurrences:** 2
- **Context:** *...> Drawing }  declare const window: GlobalParams  export class ToolBox {     private static readonly TREND_SVG: string = '<rect x="3.84" y="13.67" transform="matrix(0.7071 -0.7071 0.7071 0.7071 -5.9847 14.4482)...*
- **Link:** [View in docs](./toolbox_docs.md)

#### `ToolBox`

- **Occurrences:** 7
- **Context:** *...ment,     type: new (...args: any[]) => Drawing }  declare const window: GlobalParams  export class ToolBox {     private static readonly TREND_SVG: string = '<rect x="3.84" y="13.67" transform="matrix(0.707...*
- **Link:** [View in docs](./toolbox_docs.md)

#### `TrendLine`

- **Occurrences:** 4
- **Context:** *...import { DrawingTool } from "../drawing/drawing-tool"; import { TrendLine } from "../trend-line/trend-line"; import { Box } from "../box/box"; import { Drawing } from "../dr...*
- **Link:** [View in docs](./toolbox_docs.md)

### V

#### `VERT_SVG`

- **Occurrences:** 2
- **Context:** *...="9" width="1" height="11"/><rect x="6" y="9" width="1" height="11"/>';     private static readonly VERT_SVG: string = ToolBox.RAY_SVG;      div: HTMLDivElement;     private activeIcon: Icon | null = null;   ...*
- **Link:** [View in docs](./toolbox_docs.md)

#### `VerticalLine`

- **Occurrences:** 4
- **Context:** *..../horizontal-line/horizontal-line"; import { RayLine } from "../horizontal-line/ray-line"; import { VerticalLine } from "../vertical-line/vertical-line";   interface Icon {     div: HTMLDivElement,     group: SVG...*
- **Link:** [View in docs](./toolbox_docs.md)

---

*Keywords extracted on 2025-11-18T21:53:49.112329*
