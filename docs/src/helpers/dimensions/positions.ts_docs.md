# positions.ts Documentation

## File Metadata
- **Path**: `src/helpers/dimensions/positions.ts`
- **Extension**: `.ts`
- **Lines of Code**: 49
- **File Size**: 1871 bytes

## Original Source

```ts
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

## Overview

This file is located at `src/helpers/dimensions/positions.ts` and contains 49 lines of code.

## TypeScript/JavaScript Code Analysis

### Functions

- **centreOffset**: Function implementation
- **positionsLine**: Function implementation
- **positionsBox**: Function implementation

### Exports

- **positionsLine**: Exported symbol
- **positionsBox**: Exported symbol


## Related Files

This file is part of the repository structure. Related files may be found in the same directory or referenced in the code above.

## Tests

To test this file, refer to the repository's test suite in the `test/` directory.

## Performance & Security Notes

- Always review code for potential security vulnerabilities
- Ensure proper error handling is implemented
- Follow best practices for the language/framework being used
