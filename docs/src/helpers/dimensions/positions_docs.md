# positions.ts

**File Path:** `src/helpers/dimensions/positions.ts`

**File Size:** 1,871 bytes
**Lines of Code:** 49
**Language:** typescript

---

## File Metadata

- **Relative Path:** `src/helpers/dimensions/positions.ts`
- **File Type:** .ts
- **Size:** 1,871 bytes
- **Total Lines:** 49
- **Programming Language:** typescript

## Quick Summary

This file is part of the lightweight-charts-python repository.
 It contains 1 function(s).


## Original Source Code

```typescript

import { BitmapPositionLength } from './common';

function centreOffset(lineBitmapWidth: number): number {
	return Math.floor(lineBitmapWidth * 0.5);
}

/**
 * Calculates the bitmap position for an item with a desired length (height or width), and centred according to
 * an position coordinate defined in media sizing.
 * @param positionMedia - position coordinate for the bar (in media coordinates)
 * @param pixelRatio - pixel ratio. Either horizontal for x positions, or vertical for y positions
 * @param desiredWidthMedia - desired width (in media coordinates)
 * @returns Position of of the start point and length dimension.
 */
export function positionsLine(
	positionMedia: number,
	pixelRatio: number,
	desiredWidthMedia: number = 1,
	widthIsBitmap?: boolean
): BitmapPositionLength {
	const scaledPosition = Math.round(pixelRatio * positionMedia);
	const lineBitmapWidth = widthIsBitmap
		? desiredWidthMedia
		: Math.round(desiredWidthMedia * pixelRatio);
	const offset = centreOffset(lineBitmapWidth);
	const position = scaledPosition - offset;
	return { position, length: lineBitmapWidth };
}

/**
 * Determines the bitmap position and length for a dimension of a shape to be drawn.
 * @param position1Media - media coordinate for the first point
 * @param position2Media - media coordinate for the second point
 * @param pixelRatio - pixel ratio for the corresponding axis (vertical or horizontal)
 * @returns Position of of the start point and length dimension.
 */
export function positionsBox(
	position1Media: number,
	position2Media: number,
	pixelRatio: number
): BitmapPositionLength {
	const scaledPosition1 = Math.round(pixelRatio * position1Media);
	const scaledPosition2 = Math.round(pixelRatio * position2Media);
	return {
		position: Math.min(scaledPosition1, scaledPosition2),
		length: Math.abs(scaledPosition2 - scaledPosition1) + 1,
	};
}


```

## High-Level Overview

### Functions (1)

- **`centreOffset(lineBitmapWidth: number)`** (line 3)

## Detailed Walkthrough

### Code Structure

This file contains 49 lines of typescript.

#### Functions

##### centreOffset (Line 3)

**Parameters:** `lineBitmapWidth: number`

## Usage Examples

To use this file in your project:

```javascript
import { ... } from './src/helpers/dimensions/positions.ts';
```

## Performance & Security Notes

### Performance

- File size: 1,871 bytes
- Complexity: 1 functions, 0 classes

### Security

- **Recommendation:** Review this file for potential security vulnerabilities
- No obvious security concerns detected (basic scan)

## Related Files

*To be populated during folder indexing phase*

## Testing

Tests for this file may be located in the `test/` directory.

---

*Documentation generated on 2025-11-18T21:53:49.053097*
