# Keywords: sample-data.ts

**Source File:** `src/sample-data.ts`
**Total Keywords:** 6

---

## Keyword Index (A-Z)

### C

#### `CandleData`

- **Occurrences:** 2
- **Context:** *... Time, } from 'lightweight-charts';  type LineData = { 	time: Time; 	value: number; };  export type CandleData = { 	time: Time; 	high: number; 	low: number; 	close: number; 	open: number; };  let randomFactor =...*
- **Link:** [View in docs](./sample-data_docs.md)

### G

#### `generateCandleData`

- **Occurrences:** 1
- **Context:** *...ime, 			value, 		});  		date.setUTCDate(date.getUTCDate() + 1); 	}  	return res; }  export function generateCandleData(numberOfPoints: number = 250): CandleData[] { 	const lineData = generateLineData(numberOfPoints); 	...*
- **Link:** [View in docs](./sample-data_docs.md)

#### `generateLineData`

- **Occurrences:** 2
- **Context:** *... * 0.4 + 			Math.sin(i / randomFactor) * 0.8 + 			Math.sin(i / 500) * 0.5) + 	200;  export function generateLineData(numberOfPoints: number = 500): LineData[] { 	randomFactor = 25 + Math.random() * 25; 	const res = [...*
- **Link:** [View in docs](./sample-data_docs.md)

### L

#### `LineData`

- **Occurrences:** 2
- **Context:** *...import type { Time, } from 'lightweight-charts';  type LineData = { 	time: Time; 	value: number; };  export type CandleData = { 	time: Time; 	high: number; 	low: n...*
- **Link:** [View in docs](./sample-data_docs.md)

### S

#### `samplePoint`

- **Occurrences:** 3
- **Context:** *... 	low: number; 	close: number; 	open: number; };  let randomFactor = 25 + Math.random() * 25; const samplePoint = (i: number) => 	i * 		(0.5 + 			Math.sin(i / 10) * 0.2 + 			Math.sin(i / 20) * 0.4 + 			Math.sin(...*
- **Link:** [View in docs](./sample-data_docs.md)

### U

#### `UTC`

- **Occurrences:** 1
- **Context:** *... LineData[] { 	randomFactor = 25 + Math.random() * 25; 	const res = []; 	const date = new Date(Date.UTC(2018, 0, 1, 12, 0, 0, 0)); 	for (let i = 0; i < numberOfPoints; ++i) { 		const time = (date.getTime...*
- **Link:** [View in docs](./sample-data_docs.md)

---

*Keywords extracted on 2025-11-18T21:53:49.026421*
