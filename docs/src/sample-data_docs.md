# sample-data.ts

**File Path:** `src/sample-data.ts`

**File Size:** 1,342 bytes
**Lines of Code:** 59
**Language:** typescript

---

## File Metadata

- **Relative Path:** `src/sample-data.ts`
- **File Type:** .ts
- **Size:** 1,342 bytes
- **Total Lines:** 59
- **Programming Language:** typescript

## Quick Summary

This file is part of the lightweight-charts-python repository.
 It contains 3 function(s).


## Original Source Code

```typescript

import type { Time, } from 'lightweight-charts';

type LineData = {
	time: Time;
	value: number;
};

export type CandleData = {
	time: Time;
	high: number;
	low: number;
	close: number;
	open: number;
};

let randomFactor = 25 + Math.random() * 25;
const samplePoint = (i: number) =>
	i *
		(0.5 +
			Math.sin(i / 10) * 0.2 +
			Math.sin(i / 20) * 0.4 +
			Math.sin(i / randomFactor) * 0.8 +
			Math.sin(i / 500) * 0.5) +
	200;

export function generateLineData(numberOfPoints: number = 500): LineData[] {
	randomFactor = 25 + Math.random() * 25;
	const res = [];
	const date = new Date(Date.UTC(2018, 0, 1, 12, 0, 0, 0));
	for (let i = 0; i < numberOfPoints; ++i) {
		const time = (date.getTime() / 1000) as Time;
		const value = samplePoint(i);
		res.push({
			time,
			value,
		});

		date.setUTCDate(date.getUTCDate() + 1);
	}

	return res;
}

export function generateCandleData(numberOfPoints: number = 250): CandleData[] {
	const lineData = generateLineData(numberOfPoints);
	return lineData.map((d, i) => {
		const randomRanges = [-1 * Math.random(), Math.random(), Math.random()].map(
			j => j * 10
		);
		const sign = Math.sin(Math.random() - 0.5);
		return {
			time: d.time,
			low: d.value + randomRanges[0],
			high: d.value + randomRanges[1],
			open: d.value + sign * randomRanges[2],
			close: samplePoint(i + 1),
		};
	});
}

```

## High-Level Overview

### Functions (3)

- **`generateLineData(numberOfPoints: number = 500)`** (line 26)
- **`generateCandleData(numberOfPoints: number = 250)`** (line 44)
- **`samplePoint()`** (line 17)

## Detailed Walkthrough

### Code Structure

This file contains 59 lines of typescript.

#### Functions

##### generateLineData (Line 26)

**Parameters:** `numberOfPoints: number = 500`

##### generateCandleData (Line 44)

**Parameters:** `numberOfPoints: number = 250`

##### samplePoint (Line 17)

**Parameters:** `None`

## Usage Examples

To use this file in your project:

```javascript
import { ... } from './src/sample-data.ts';
```

## Performance & Security Notes

### Performance

- File size: 1,342 bytes
- Complexity: 3 functions, 0 classes

### Security

- **Recommendation:** Review this file for potential security vulnerabilities
- No obvious security concerns detected (basic scan)

## Related Files

*To be populated during folder indexing phase*

## Testing

Tests for this file may be located in the `test/` directory.

---

*Documentation generated on 2025-11-18T21:53:49.025570*
