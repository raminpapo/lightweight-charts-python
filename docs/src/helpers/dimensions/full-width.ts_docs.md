# full-width.ts Documentation

## File Metadata
- **Path**: `src/helpers/dimensions/full-width.ts`
- **Extension**: `.ts`
- **Lines of Code**: 30
- **File Size**: 1103 bytes

## Original Source

```ts
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

## Overview

This file is located at `src/helpers/dimensions/full-width.ts` and contains 30 lines of code.

## TypeScript/JavaScript Code Analysis

### Functions

- **fullBarWidth**: Function implementation

### Exports

- **fullBarWidth**: Exported symbol


## Related Files

This file is part of the repository structure. Related files may be found in the same directory or referenced in the code above.

## Tests

To test this file, refer to the repository's test suite in the `test/` directory.

## Performance & Security Notes

- Always review code for potential security vulnerabilities
- Ensure proper error handling is implemented
- Follow best practices for the language/framework being used
