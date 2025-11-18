# Keywords: handler.ts

**Source File:** `src/general/handler.ts`
**Total Keywords:** 27

---

## Keyword Index (A-Z)

### A

#### `animateSpinner`

- **Occurrences:** 3
- **Context:** *...ODO below can be css (animate)         let rotation = 0;         const speed = 10;         function animateSpinner() {             if (!chart.spinner) return;             rotation += speed             chart.spinner...*
- **Link:** [View in docs](./handler_docs.md)

### B

#### `BarData`

- **Occurrences:** 1
- **Context:** *...r, crosshairOnly = false) {         function crosshairHandler(chart: Handler, point: any) {//point: BarData | LineData) {             if (!point) {                 chart.chart.clearCrosshairPosition()       ...*
- **Link:** [View in docs](./handler_docs.md)

### C

#### `ColorType`

- **Occurrences:** 2
- **Context:** *...import {     ColorType,     CrosshairMode,     DeepPartial,     HistogramStyleOptions,     IChartApi,     ISeriesApi,     ...*
- **Link:** [View in docs](./handler_docs.md)

#### `CrosshairMode`

- **Occurrences:** 2
- **Context:** *...import {     ColorType,     CrosshairMode,     DeepPartial,     HistogramStyleOptions,     IChartApi,     ISeriesApi,     LineStyleOptions,  ...*
- **Link:** [View in docs](./handler_docs.md)

#### `crosshairHandler`

- **Occurrences:** 3
- **Context:** *...atic syncCharts(childChart:Handler, parentChart: Handler, crosshairOnly = false) {         function crosshairHandler(chart: Handler, point: any) {//point: BarData | LineData) {             if (!point) {              ...*
- **Link:** [View in docs](./handler_docs.md)

### D

#### `DeepPartial`

- **Occurrences:** 3
- **Context:** *...import {     ColorType,     CrosshairMode,     DeepPartial,     HistogramStyleOptions,     IChartApi,     ISeriesApi,     LineStyleOptions,     LogicalRange, ...*
- **Link:** [View in docs](./handler_docs.md)

### G

#### `GlobalParams`

- **Occurrences:** 2
- **Context:** *...riesOptionsCommon,     SeriesType,     Time,     createChart } from "lightweight-charts";  import { GlobalParams, globalParamInit } from "./global-params"; import { Legend } from "./legend"; import { ToolBox } fr...*
- **Link:** [View in docs](./handler_docs.md)

#### `getPoint`

- **Occurrences:** 3
- **Context:** *...ime, chart.series);             chart.legend.legendHandler(point, true)         }          function getPoint(series: ISeriesApi<SeriesType>, param: MouseEventParams) {             if (!param.time) return null...*
- **Link:** [View in docs](./handler_docs.md)

### H

#### `Handler`

- **Occurrences:** 8
- **Context:** *...umber,     height: number, }   globalParamInit(); declare const window: GlobalParams;  export class Handler {     public id: string;     public commandFunctions: Function[] = [];      public wrapper: HTMLDiv...*
- **Link:** [View in docs](./handler_docs.md)

#### `HistogramStyleOptions`

- **Occurrences:** 2
- **Context:** *...import {     ColorType,     CrosshairMode,     DeepPartial,     HistogramStyleOptions,     IChartApi,     ISeriesApi,     LineStyleOptions,     LogicalRange,     LogicalRangeChangeEvent...*
- **Link:** [View in docs](./handler_docs.md)

### K

#### `KeyboardEvent`

- **Occurrences:** 1
- **Context:** *...ild(sBox)         chart.div.appendChild(searchWindow);          chart.commandFunctions.push((event: KeyboardEvent) => {             if (window.handlerInFocus !== chart.id || window.textBoxFocused) return false    ...*
- **Link:** [View in docs](./handler_docs.md)

### L

#### `LineData`

- **Occurrences:** 1
- **Context:** *...irOnly = false) {         function crosshairHandler(chart: Handler, point: any) {//point: BarData | LineData) {             if (!point) {                 chart.chart.clearCrosshairPosition()                 r...*
- **Link:** [View in docs](./handler_docs.md)

#### `LineStyleOptions`

- **Occurrences:** 2
- **Context:** *...,     CrosshairMode,     DeepPartial,     HistogramStyleOptions,     IChartApi,     ISeriesApi,     LineStyleOptions,     LogicalRange,     LogicalRangeChangeEventHandler,     MouseEventHandler,     MouseEventParams,...*
- **Link:** [View in docs](./handler_docs.md)

#### `LogicalRange`

- **Occurrences:** 3
- **Context:** *...   DeepPartial,     HistogramStyleOptions,     IChartApi,     ISeriesApi,     LineStyleOptions,     LogicalRange,     LogicalRangeChangeEventHandler,     MouseEventHandler,     MouseEventParams,     SeriesOptions...*
- **Link:** [View in docs](./handler_docs.md)

#### `LogicalRangeChangeEventHandler`

- **Occurrences:** 3
- **Context:** *...  HistogramStyleOptions,     IChartApi,     ISeriesApi,     LineStyleOptions,     LogicalRange,     LogicalRangeChangeEventHandler,     MouseEventHandler,     MouseEventParams,     SeriesOptionsCommon,     SeriesType,     Time,   ...*
- **Link:** [View in docs](./handler_docs.md)

### M

#### `MouseEventHandler`

- **Occurrences:** 3
- **Context:** *...pi,     ISeriesApi,     LineStyleOptions,     LogicalRange,     LogicalRangeChangeEventHandler,     MouseEventHandler,     MouseEventParams,     SeriesOptionsCommon,     SeriesType,     Time,     createChart } from "l...*
- **Link:** [View in docs](./handler_docs.md)

#### `MouseEventParams`

- **Occurrences:** 4
- **Context:** *... LineStyleOptions,     LogicalRange,     LogicalRangeChangeEventHandler,     MouseEventHandler,     MouseEventParams,     SeriesOptionsCommon,     SeriesType,     Time,     createChart } from "lightweight-charts";  i...*
- **Link:** [View in docs](./handler_docs.md)

### S

#### `SeriesOptionsCommon`

- **Occurrences:** 3
- **Context:** *... LogicalRange,     LogicalRangeChangeEventHandler,     MouseEventHandler,     MouseEventParams,     SeriesOptionsCommon,     SeriesType,     Time,     createChart } from "lightweight-charts";  import { GlobalParams, glo...*
- **Link:** [View in docs](./handler_docs.md)

#### `SeriesType`

- **Occurrences:** 5
- **Context:** *...lRangeChangeEventHandler,     MouseEventHandler,     MouseEventParams,     SeriesOptionsCommon,     SeriesType,     Time,     createChart } from "lightweight-charts";  import { GlobalParams, globalParamInit } f...*
- **Link:** [View in docs](./handler_docs.md)

#### `setChildCrosshair`

- **Occurrences:** 4
- **Context:** *...          crosshairHandler(parentChart, getPoint(childChart.series, param))         }         const setChildCrosshair = (param: MouseEventParams) => {             crosshairHandler(childChart, getPoint(parentChart.seri...*
- **Link:** [View in docs](./handler_docs.md)

#### `setChildRange`

- **Occurrences:** 4
- **Context:** *...rt.chart.timeScale();         const parentTimeScale = parentChart.chart.timeScale();          const setChildRange = (timeRange: LogicalRange | null) => {             if(timeRange) childTimeScale.setVisibleLogicalR...*
- **Link:** [View in docs](./handler_docs.md)

#### `setParentCrosshair`

- **Occurrences:** 3
- **Context:** *...          if(timeRange) parentTimeScale.setVisibleLogicalRange(timeRange);         }          const setParentCrosshair = (param: MouseEventParams) => {             crosshairHandler(parentChart, getPoint(childChart.seri...*
- **Link:** [View in docs](./handler_docs.md)

#### `setParentRange`

- **Occurrences:** 3
- **Context:** *...            if(timeRange) childTimeScale.setVisibleLogicalRange(timeRange);         }         const setParentRange = (timeRange: LogicalRange | null) => {             if(timeRange) parentTimeScale.setVisibleLogical...*
- **Link:** [View in docs](./handler_docs.md)

### T

#### `TODO`

- **Occurrences:** 4
- **Context:** *...pinner: HTMLDivElement | undefined;      public _seriesList: ISeriesApi<SeriesType>[] = [];      // TODO find a better solution rather than the 'position' parameter     constructor(         chartId: strin...*
- **Link:** [View in docs](./handler_docs.md)

#### `ToolBox`

- **Occurrences:** 3
- **Context:** *...GlobalParams, globalParamInit } from "./global-params"; import { Legend } from "./legend"; import { ToolBox } from "./toolbox"; import { TopBar } from "./topbar";   export interface Scale{     width: number,...*
- **Link:** [View in docs](./handler_docs.md)

#### `TopBar`

- **Occurrences:** 3
- **Context:** *..."./global-params"; import { Legend } from "./legend"; import { ToolBox } from "./toolbox"; import { TopBar } from "./topbar";   export interface Scale{     width: number,     height: number, }   globalParam...*
- **Link:** [View in docs](./handler_docs.md)

### V

#### `volume_scale`

- **Occurrences:** 1
- **Context:** *...            color: '#26a69a',             priceFormat: {type: 'volume'},             priceScaleId: 'volume_scale',         })         volumeSeries.priceScale().applyOptions({             scaleMargins: {top: 0.8, ...*
- **Link:** [View in docs](./handler_docs.md)

---

*Keywords extracted on 2025-11-18T21:53:49.124216*
