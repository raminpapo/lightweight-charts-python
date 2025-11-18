# Keywords: context-menu.ts

**Source File:** `src/context-menu/context-menu.ts`
**Total Keywords:** 8

---

## Keyword Index (A-Z)

### C

#### `ColorPicker`

- **Occurrences:** 3
- **Context:** *...ions } from "../drawing/options"; import { GlobalParams } from "../general/global-params"; import { ColorPicker } from "./color-picker"; import { StylePicker } from "./style-picker";   export function camelToTit...*
- **Link:** [View in docs](./context-menu_docs.md)

#### `ContextMenu`

- **Occurrences:** 1
- **Context:** *...: Function;     closeAction: Function | null; }  declare const window: GlobalParams;   export class ContextMenu {     private div: HTMLDivElement     private hoverItem: Item | null;     private items: HTMLElemen...*
- **Link:** [View in docs](./context-menu_docs.md)

#### `camelToTitle`

- **Occurrences:** 2
- **Context:** *...olorPicker } from "./color-picker"; import { StylePicker } from "./style-picker";   export function camelToTitle(inputString: string) {     const result = [];     for (const c of inputString) {         if (result...*
- **Link:** [View in docs](./context-menu_docs.md)

### D

#### `DrawingOptions`

- **Occurrences:** 2
- **Context:** *...rawing } from "../drawing/drawing"; import { DrawingTool } from "../drawing/drawing-tool"; import { DrawingOptions } from "../drawing/options"; import { GlobalParams } from "../general/global-params"; import { Colo...*
- **Link:** [View in docs](./context-menu_docs.md)

#### `DrawingTool`

- **Occurrences:** 2
- **Context:** *...import { Drawing } from "../drawing/drawing"; import { DrawingTool } from "../drawing/drawing-tool"; import { DrawingOptions } from "../drawing/options"; import { Glo...*
- **Link:** [View in docs](./context-menu_docs.md)

### G

#### `GlobalParams`

- **Occurrences:** 2
- **Context:** *...ool } from "../drawing/drawing-tool"; import { DrawingOptions } from "../drawing/options"; import { GlobalParams } from "../general/global-params"; import { ColorPicker } from "./color-picker"; import { StylePick...*
- **Link:** [View in docs](./context-menu_docs.md)

### M

#### `MouseEvent`

- **Occurrences:** 3
- **Context:** *...  document.body.addEventListener('contextmenu', this._onRightClick);     }      _handleClick = (ev: MouseEvent) => this._onClick(ev);      private _onClick(ev: MouseEvent) {         if (!ev.target) return;     ...*
- **Link:** [View in docs](./context-menu_docs.md)

### S

#### `StylePicker`

- **Occurrences:** 3
- **Context:** *...balParams } from "../general/global-params"; import { ColorPicker } from "./color-picker"; import { StylePicker } from "./style-picker";   export function camelToTitle(inputString: string) {     const result = [...*
- **Link:** [View in docs](./context-menu_docs.md)

---

*Keywords extracted on 2025-11-18T21:53:49.047789*
