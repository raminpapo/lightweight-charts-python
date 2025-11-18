# crosshair-width.ts

**File Path:** `src/helpers/dimensions/crosshair-width.ts`

**File Size:** 690 bytes
**Lines of Code:** 24
**Language:** typescript

---

## File Metadata

- **Relative Path:** `src/helpers/dimensions/crosshair-width.ts`
- **File Type:** .ts
- **Size:** 690 bytes
- **Total Lines:** 24
- **Programming Language:** typescript

## Quick Summary

This file is part of the lightweight-charts-python repository.


## Original Source Code

```typescript

/**
 * Default grid / crosshair line width in Bitmap sizing
 * @param horizontalPixelRatio - horizontal pixel ratio
 * @returns default grid / crosshair line width in Bitmap sizing
 */
export function gridAndCrosshairBitmapWidth(
	horizontalPixelRatio: number
): number {
	return Math.max(1, Math.floor(horizontalPixelRatio));
}

/**
 * Default grid / crosshair line width in Media sizing
 * @param horizontalPixelRatio - horizontal pixel ratio
 * @returns default grid / crosshair line width in Media sizing
 */
export function gridAndCrosshairMediaWidth(
	horizontalPixelRatio: number
): number {
	return (
		gridAndCrosshairBitmapWidth(horizontalPixelRatio) / horizontalPixelRatio
	);
}


```

## High-Level Overview

## Detailed Walkthrough

### Code Structure

This file contains 24 lines of typescript.
## Usage Examples

To use this file in your project:

```javascript
import { ... } from './src/helpers/dimensions/crosshair-width.ts';
```

## Performance & Security Notes

### Performance

- File size: 690 bytes
- Complexity: 0 functions, 0 classes

### Security

- **Recommendation:** Review this file for potential security vulnerabilities
- No obvious security concerns detected (basic scan)

## Related Files

*To be populated during folder indexing phase*

## Testing

Tests for this file may be located in the `test/` directory.

---

*Documentation generated on 2025-11-18T21:53:49.054659*
