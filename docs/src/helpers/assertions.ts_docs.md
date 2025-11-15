# assertions.ts Documentation

## File Metadata
- **Path**: `src/helpers/assertions.ts`
- **Extension**: `.ts`
- **Lines of Code**: 34
- **File Size**: 924 bytes

## Original Source

```ts
/**
 * Ensures that value is defined.
 * Throws if the value is undefined, returns the original value otherwise.
 *
 * @param value - The value, or undefined.
 * @returns The passed value, if it is not undefined
 */
export function ensureDefined(value: undefined): never;
export function ensureDefined<T>(value: T | undefined): T;
export function ensureDefined<T>(value: T | undefined): T {
	if (value === undefined) {
		throw new Error('Value is undefined');
	}

	return value;
}

/**
 * Ensures that value is not null.
 * Throws if the value is null, returns the original value otherwise.
 *
 * @param value - The value, or null.
 * @returns The passed value, if it is not null
 */
export function ensureNotNull(value: null): never;
export function ensureNotNull<T>(value: T | null): T;
export function ensureNotNull<T>(value: T | null): T {
	if (value === null) {
		throw new Error('Value is null');
	}

	return value;
}

```

## Overview

This file is located at `src/helpers/assertions.ts` and contains 34 lines of code.

## TypeScript/JavaScript Code Analysis

### Functions

- **ensureDefined**: Function implementation
- **ensureDefined**: Function implementation
- **ensureDefined**: Function implementation
- **ensureNotNull**: Function implementation
- **ensureNotNull**: Function implementation
- **ensureNotNull**: Function implementation

### Exports

- **ensureDefined**: Exported symbol
- **ensureDefined**: Exported symbol
- **ensureDefined**: Exported symbol
- **ensureNotNull**: Exported symbol
- **ensureNotNull**: Exported symbol
- **ensureNotNull**: Exported symbol


## Related Files

This file is part of the repository structure. Related files may be found in the same directory or referenced in the code above.

## Tests

To test this file, refer to the repository's test suite in the `test/` directory.

## Performance & Security Notes

- Always review code for potential security vulnerabilities
- Ensure proper error handling is implemented
- Follow best practices for the language/framework being used
