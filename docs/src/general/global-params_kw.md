# Keywords: global-params.ts

**Source File:** `src/general/global-params.ts`
**Total Keywords:** 9

---

## Keyword Index (A-Z)

### G

#### `GlobalParams`

- **Occurrences:** 2
- **Context:** *...export interface GlobalParams extends Window {     pane: paneStyle;    // TODO shouldnt need this cause of css variables     hand...*
- **Link:** [View in docs](./global-params_docs.md)

#### `globalParamInit`

- **Occurrences:** 1
- **Context:** *...lor: '#d8d9db',     activeColor: '#ececed', }  declare const window: GlobalParams;  export function globalParamInit() {     window.pane = {         ...paneStyleDefault,     }     window.containerDiv = document.getEl...*
- **Link:** [View in docs](./global-params_docs.md)

### H

#### `HorizontalLine`

- **Occurrences:** 1
- **Context:** *...//     series: ISeriesApi<SeriesType>; //     markers: SeriesMarker<"">[], //     horizontal_lines: HorizontalLine[], //     name?: string, //     precision: number, // }  ...*
- **Link:** [View in docs](./global-params_docs.md)

#### `horizontal_lines`

- **Occurrences:** 1
- **Context:** *...    type: string; //     series: ISeriesApi<SeriesType>; //     markers: SeriesMarker<"">[], //     horizontal_lines: HorizontalLine[], //     name?: string, //     precision: number, // }  ...*
- **Link:** [View in docs](./global-params_docs.md)

### S

#### `SeriesHandler`

- **Occurrences:** 1
- **Context:** *...type) window.cursor = type;     document.body.style.cursor = window.cursor; }   // export interface SeriesHandler { //     type: string; //     series: ISeriesApi<SeriesType>; //     markers: SeriesMarker<"">[], /...*
- **Link:** [View in docs](./global-params_docs.md)

#### `SeriesMarker`

- **Occurrences:** 1
- **Context:** *...terface SeriesHandler { //     type: string; //     series: ISeriesApi<SeriesType>; //     markers: SeriesMarker<"">[], //     horizontal_lines: HorizontalLine[], //     name?: string, //     precision: number, /...*
- **Link:** [View in docs](./global-params_docs.md)

#### `SeriesType`

- **Occurrences:** 1
- **Context:** *...ndow.cursor; }   // export interface SeriesHandler { //     type: string; //     series: ISeriesApi<SeriesType>; //     markers: SeriesMarker<"">[], //     horizontal_lines: HorizontalLine[], //     name?: stri...*
- **Link:** [View in docs](./global-params_docs.md)

#### `setCursor`

- **Occurrences:** 3
- **Context:** *...ng;     textBoxFocused: boolean;     callbackFunction: Function;     containerDiv: HTMLElement;     setCursor: Function;     cursor: string; }  interface paneStyle {     backgroundColor: string;     hoverBackg...*
- **Link:** [View in docs](./global-params_docs.md)

### T

#### `TODO`

- **Occurrences:** 1
- **Context:** *...export interface GlobalParams extends Window {     pane: paneStyle;    // TODO shouldnt need this cause of css variables     handlerInFocus: string;     textBoxFocused: boolean; ...*
- **Link:** [View in docs](./global-params_docs.md)

---

*Keywords extracted on 2025-11-18T21:53:49.133380*
