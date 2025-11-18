# Keywords: time.ts

**Source File:** `src/helpers/time.ts`
**Total Keywords:** 3

---

## Keyword Index (A-Z)

### C

#### `convertTime`

- **Occurrences:** 1
- **Context:** *...import { Time, isUTCTimestamp, isBusinessDay } from 'lightweight-charts';  export function convertTime(t: Time): number { 	if (isUTCTimestamp(t)) return t * 1000; 	if (isBusinessDay(t)) return new Date(...*
- **Link:** [View in docs](./time_docs.md)

### D

#### `displayTime`

- **Occurrences:** 1
- **Context:** *...day] = t.split('-').map(parseInt); 	return new Date(year, month, day).valueOf(); }  export function displayTime(time: Time): string { 	if (typeof time == 'string') return time; 	const date = isBusinessDay(time) ...*
- **Link:** [View in docs](./time_docs.md)

### F

#### `formattedDateAndTime`

- **Occurrences:** 1
- **Context:** *...e.month, time.day) 		: new Date(time * 1000); 	return date.toLocaleDateString(); }  export function formattedDateAndTime(timestamp: number | undefined): [string, string] { 	if (!timestamp) return ['', '']; 	const dateObj...*
- **Link:** [View in docs](./time_docs.md)

---

*Keywords extracted on 2025-11-18T21:53:49.052158*
