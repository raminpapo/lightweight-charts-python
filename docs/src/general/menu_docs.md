# menu.ts

**File Path:** `src/general/menu.ts`

**File Size:** 2,005 bytes
**Lines of Code:** 63
**Language:** typescript

---

## File Metadata

- **Relative Path:** `src/general/menu.ts`
- **File Type:** .ts
- **Size:** 2,005 bytes
- **Total Lines:** 63
- **Programming Language:** typescript

## Quick Summary

This file is part of the lightweight-charts-python repository.
 It defines 1 class(es).


## Original Source Code

```typescript

import { GlobalParams } from "./global-params";

declare const window: GlobalParams

export class Menu {
    private div: HTMLDivElement;
    private isOpen: boolean = false;
    private widget: any;

    constructor(
        private makeButton: Function,
        private callbackName: string,
        items: string[],
        activeItem: string,
        separator: boolean,
        align: 'right'|'left') {

        this.div = document.createElement('div')
        this.div.classList.add('topbar-menu');

        this.widget = this.makeButton(activeItem+' ↓', null, separator, true, align)

        this.updateMenuItems(items)

        this.widget.elem.addEventListener('click', () => {
            this.isOpen = !this.isOpen;
            if (!this.isOpen) {
                this.div.style.display = 'none';
                return;
            }
            let rect = this.widget.elem.getBoundingClientRect()
            this.div.style.display = 'flex'
            this.div.style.flexDirection = 'column'

            let center = rect.x+(rect.width/2)
            this.div.style.left = center-(this.div.clientWidth/2)+'px'
            this.div.style.top = rect.y+rect.height+'px'
        })
        document.body.appendChild(this.div)
    }

    updateMenuItems(items: string[]) {
        this.div.innerHTML = '';

        items.forEach(text => {
            let button = this.makeButton(text, null, false, false)
            button.elem.addEventListener('click', () => {
                this._clickHandler(button.elem.innerText);
            });
            button.elem.style.margin = '4px 4px'
            button.elem.style.padding = '2px 2px'
            this.div.appendChild(button.elem)
        })
        this.widget.elem.innerText = items[0]+' ↓';
    }
    
    private _clickHandler(name: string) {
        this.widget.elem.innerText = name+' ↓'
        window.callbackFunction(`${this.callbackName}_~_${name}`)
        this.div.style.display = 'none'
        this.isOpen = false
    }
}

```

## High-Level Overview

### Classes (1)

- **`Menu`** (line 5)

## Detailed Walkthrough

### Code Structure

This file contains 63 lines of typescript.

#### Classes

##### Menu (Line 5)

## Usage Examples

To use this file in your project:

```javascript
import { ... } from './src/general/menu.ts';
```

## Performance & Security Notes

### Performance

- File size: 2,005 bytes
- Complexity: 0 functions, 1 classes

### Security

- **Recommendation:** Review this file for potential security vulnerabilities
- No obvious security concerns detected (basic scan)

## Related Files

*To be populated during folder indexing phase*

## Testing

Tests for this file may be located in the `test/` directory.

---

*Documentation generated on 2025-11-18T21:53:49.129903*
