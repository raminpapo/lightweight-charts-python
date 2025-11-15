# crosshair-width.ts Documentation

## File Metadata
- **Path**: `src/helpers/dimensions/crosshair-width.ts`
- **Extension**: `.ts`
- **Lines of Code**: 24
- **File Size**: 690 bytes

## Original Source

```ts
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

## Overview

This file is located at `src/helpers/dimensions/crosshair-width.ts` and contains 24 lines of code.

## TypeScript/JavaScript Code Analysis

### Functions

- **gridAndCrosshairBitmapWidth**: Function implementation
- **gridAndCrosshairMediaWidth**: Function implementation

### Exports

- **gridAndCrosshairBitmapWidth**: Exported symbol
- **gridAndCrosshairMediaWidth**: Exported symbol


## Related Files

This file is part of the repository structure. Related files may be found in the same directory or referenced in the code above.

## Tests

To test this file, refer to the repository's test suite in the `test/` directory.

## Performance & Security Notes

- Always review code for potential security vulnerabilities
- Ensure proper error handling is implemented
- Follow best practices for the language/framework being used
