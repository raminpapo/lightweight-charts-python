# style-picker.ts Documentation

## File Metadata
- **Path**: `src/context-menu/style-picker.ts`
- **Extension**: `.ts`
- **Lines of Code**: 57
- **File Size**: 1881 bytes

## Original Source

```ts
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

## Overview

This file is located at `src/context-menu/style-picker.ts` and contains 57 lines of code.

## TypeScript/JavaScript Code Analysis

### Classes

- **StylePicker**: Class implementation

### Exports

- **StylePicker**: Exported symbol


## Related Files

This file is part of the repository structure. Related files may be found in the same directory or referenced in the code above.

## Tests

To test this file, refer to the repository's test suite in the `test/` directory.

## Performance & Security Notes

- Always review code for potential security vulnerabilities
- Ensure proper error handling is implemented
- Follow best practices for the language/framework being used
