# full-width.ts

**File Path:** `src/helpers/dimensions/full-width.ts`

**File Size:** 1,103 bytes
**Lines of Code:** 30
**Language:** typescript

---

## File Metadata

- **Relative Path:** `src/helpers/dimensions/full-width.ts`
- **File Type:** .ts
- **Size:** 1,103 bytes
- **Total Lines:** 30
- **Programming Language:** typescript

## Quick Summary

This file is part of the lightweight-charts-python repository.


## Original Source Code

```typescript

import { BitmapPositionLength } from './common';

/**
 * Calculates the position and width which will completely full the space for the bar.
 * Useful if you want to draw something that will not have any gaps between surrounding bars.
 * @param xMedia - x coordinate of the bar defined in media sizing
 * @param halfBarSpacingMedia - half the width of the current barSpacing (un-rounded)
 * @param horizontalPixelRatio - horizontal pixel ratio
 * @returns position and width which will completely full the space for the bar
 */
export function fullBarWidth(
	xMedia: number,
	halfBarSpacingMedia: number,
	horizontalPixelRatio: number
): BitmapPositionLength {
	const fullWidthLeftMedia = xMedia - halfBarSpacingMedia;
	const fullWidthRightMedia = xMedia + halfBarSpacingMedia;
	const fullWidthLeftBitmap = Math.round(
		fullWidthLeftMedia * horizontalPixelRatio
	);
	const fullWidthRightBitmap = Math.round(
		fullWidthRightMedia * horizontalPixelRatio
	);
	const fullWidthBitmap = fullWidthRightBitmap - fullWidthLeftBitmap;
	return {
		position: fullWidthLeftBitmap,
		length: fullWidthBitmap,
	};
}


```

## High-Level Overview

## Detailed Walkthrough

### Code Structure

This file contains 30 lines of typescript.
## Usage Examples

To use this file in your project:

```javascript
import { ... } from './src/helpers/dimensions/full-width.ts';
```

## Performance & Security Notes

### Performance

- File size: 1,103 bytes
- Complexity: 0 functions, 0 classes

### Security

- **Recommendation:** Review this file for potential security vulnerabilities
- No obvious security concerns detected (basic scan)

## Related Files

*To be populated during folder indexing phase*

## Testing

Tests for this file may be located in the `test/` directory.

---

*Documentation generated on 2025-11-18T21:53:49.056201*
