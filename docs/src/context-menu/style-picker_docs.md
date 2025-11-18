# style-picker.ts

**File Path:** `src/context-menu/style-picker.ts`

**File Size:** 1,881 bytes
**Lines of Code:** 57
**Language:** typescript

---

## File Metadata

- **Relative Path:** `src/context-menu/style-picker.ts`
- **File Type:** .ts
- **Size:** 1,881 bytes
- **Total Lines:** 57
- **Programming Language:** typescript

## Quick Summary

This file is part of the lightweight-charts-python repository.
 It defines 1 class(es).


## Original Source Code

```typescript

import { LineStyle } from "lightweight-charts";
import { GlobalParams } from "../general/global-params";
import { Drawing } from "../drawing/drawing";

declare const window: GlobalParams;


export class StylePicker {
    private static readonly _styles = [
        {name: 'Solid', var: LineStyle.Solid},
        {name: 'Dotted', var: LineStyle.Dotted},
        {name: 'Dashed', var: LineStyle.Dashed},
        {name: 'Large Dashed', var: LineStyle.LargeDashed},
        {name: 'Sparse Dotted', var: LineStyle.SparseDotted},
    ]

    public _div: HTMLDivElement;
    private _saveDrawings: Function;

    constructor(saveDrawings: Function) {
        this._saveDrawings = saveDrawings

        this._div = document.createElement('div');
        this._div.classList.add('context-menu');
        StylePicker._styles.forEach((style) => {
            this._div.appendChild(this._makeTextBox(style.name, style.var))
        })
        window.containerDiv.appendChild(this._div);
    }

    private _makeTextBox(text: string, style: LineStyle) {
        const item = document.createElement('span');
        item.classList.add('context-menu-item');
        item.innerText = text
        item.addEventListener('click', () => {
            Drawing.lastHoveredObject?.applyOptions({lineStyle: style});
            this._saveDrawings();
        })
        return item
    }

    openMenu(rect: DOMRect) {
        this._div.style.top = (rect.top-30)+'px'
        this._div.style.left = rect.right+'px'
        this._div.style.display = 'block'

        setTimeout(() => document.addEventListener('mousedown', (event: MouseEvent) => {
            if (!this._div.contains(event.target as Node)) {
                this.closeMenu()
            }
        }), 10)
    }
    closeMenu() {
        document.removeEventListener('click', this.closeMenu)
        this._div.style.display = 'none'
    }
}

```

## High-Level Overview

### Classes (1)

- **`StylePicker`** (line 8)

## Detailed Walkthrough

### Code Structure

This file contains 57 lines of typescript.

#### Classes

##### StylePicker (Line 8)

## Usage Examples

To use this file in your project:

```javascript
import { ... } from './src/context-menu/style-picker.ts';
```

## Performance & Security Notes

### Performance

- File size: 1,881 bytes
- Complexity: 0 functions, 1 classes

### Security

- **Recommendation:** Review this file for potential security vulnerabilities
- No obvious security concerns detected (basic scan)

## Related Files

*To be populated during folder indexing phase*

## Testing

Tests for this file may be located in the `test/` directory.

---

*Documentation generated on 2025-11-18T21:53:49.040527*
