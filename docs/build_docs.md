# build.sh

**File Path:** `build.sh`

**File Size:** 745 bytes
**Lines of Code:** 35
**Language:** bash

---

## File Metadata

- **Relative Path:** `build.sh`
- **File Type:** .sh
- **Size:** 745 bytes
- **Total Lines:** 35
- **Programming Language:** bash

## Quick Summary

This file is part of the lightweight-charts-python repository.


## Original Source Code

```bash

#!/usr/bin/env bash

GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[0;33m'
CYAN='\033[0;36m'
NC='\033[0m'

ERROR="${RED}[ERROR]${NC} "
INFO="${CYAN}[INFO]${NC} "
WARNING="${WARNING}[WARNING]${NC} "

rm -rf dist/bundle.js dist/typings/

if [[ $? -eq 0 ]]; then
    echo -e "${INFO}deleted bundle.js and typings.."
else
    echo -e "${WARNING}could not delete old dist files, continuing.."
fi

npx rollup -c rollup.config.js
if [[ $? -ne 0 ]]; then
    exit 1
fi

cp dist/bundle.js src/general/styles.css lightweight_charts/js
if [[ $? -eq 0 ]]; then
    echo -e "${INFO}copied bundle.js, style.css into python package"
else
    echo -e "${ERROR}could not copy dist into python package ?"
    exit 1
fi
echo -e "\n${GREEN}[BUILD SUCCESS]${NC}"



```

## High-Level Overview

## Detailed Walkthrough

### Code Structure

This file contains 35 lines of bash.
## Usage Examples

To use this file in your project:

## Performance & Security Notes

### Performance

- File size: 745 bytes
- Complexity: 0 functions, 0 classes

### Security

- **Recommendation:** Review this file for potential security vulnerabilities
- No obvious security concerns detected (basic scan)

## Related Files

*To be populated during folder indexing phase*

## Testing

Tests for this file may be located in the `test/` directory.

---

*Documentation generated on 2025-11-18T21:53:48.984628*
