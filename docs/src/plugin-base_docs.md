# plugin-base.ts

**File Path:** `src/plugin-base.ts`

**File Size:** 1,429 bytes
**Lines of Code:** 57
**Language:** typescript

---

## File Metadata

- **Relative Path:** `src/plugin-base.ts`
- **File Type:** .ts
- **Size:** 1,429 bytes
- **Total Lines:** 57
- **Programming Language:** typescript

## Quick Summary

This file is part of the lightweight-charts-python repository.
 It defines 1 class(es).


## Original Source Code

```typescript

import {
	DataChangedScope,
	IChartApi,
	ISeriesApi,
	ISeriesPrimitive,
	SeriesAttachedParameter,
	SeriesOptionsMap,
	Time,
} from 'lightweight-charts';
import { ensureDefined } from './helpers/assertions';

//* PluginBase is a useful base to build a plugin upon which
//* already handles creating getters for the chart and series,
//* and provides a requestUpdate method.
export abstract class PluginBase implements ISeriesPrimitive<Time> {
	private _chart: IChartApi | undefined = undefined;
	private _series: ISeriesApi<keyof SeriesOptionsMap> | undefined = undefined;

	protected dataUpdated?(scope: DataChangedScope): void;
	protected requestUpdate(): void {
		if (this._requestUpdate) this._requestUpdate();
	}
	private _requestUpdate?: () => void;

	public attached({
		chart,
		series,
		requestUpdate,
	}: SeriesAttachedParameter<Time>) {
		this._chart = chart;
		this._series = series;
		this._series.subscribeDataChanged(this._fireDataUpdated);
		this._requestUpdate = requestUpdate;
		this.requestUpdate();
	}

	public detached() {
		this._chart = undefined;
		this._series = undefined;
		this._requestUpdate = undefined;
	}

	public get chart(): IChartApi {
		return ensureDefined(this._chart);
	}

	public get series(): ISeriesApi<keyof SeriesOptionsMap> {
		return ensureDefined(this._series);
	}

	private _fireDataUpdated(scope: DataChangedScope) {
		if (this.dataUpdated) {
			this.dataUpdated(scope);
		}
	}
}


```

## High-Level Overview

### Classes (1)

- **`PluginBase`** (line 15)

## Detailed Walkthrough

### Code Structure

This file contains 57 lines of typescript.

#### Classes

##### PluginBase (Line 15)

## Usage Examples

To use this file in your project:

```javascript
import { ... } from './src/plugin-base.ts';
```

## Performance & Security Notes

### Performance

- File size: 1,429 bytes
- Complexity: 0 functions, 1 classes

### Security

- **Recommendation:** Review this file for potential security vulnerabilities
- No obvious security concerns detected (basic scan)

## Related Files

*To be populated during folder indexing phase*

## Testing

Tests for this file may be located in the `test/` directory.

---

*Documentation generated on 2025-11-18T21:53:49.029393*
