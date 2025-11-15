# splash.css Documentation

## File Metadata
- **Path**: `docs/source/_static/splash.css`
- **Extension**: `.css`
- **Lines of Code**: 140
- **File Size**: 2286 bytes

## Original Source

```css
@font-face {
  font-family: 'Maison Neue';
  src: url('fonts/MaisonNeue-Demi.otf') format('opentype');

}
@font-face {
  font-family: 'Maison Neue Italic';
  src: url('fonts/MaisonNeue-MediumItalic.otf') format('opentype');
}



.splash-head {
    position: relative;
    display: flex;
    flex-direction: column;
    text-align: center;
    align-self: center;
    margin-bottom: 20px;
}

.splash-page-container {
    display: flex;
    flex-direction: column;
}

.theme-button {
position: absolute;
  top: 70px;
    right: -50px;
}

.top-nav {
    margin: 0;
    padding: 0;
    align-self: center;
}

.top-nav ul {
    list-style-type: none;
    padding: 0;
    display: flex;
    justify-content: space-evenly;
    background-color: var(--color-background-hover);
    border-radius: 5px;
    margin: 2rem 0 0;
}

.top-nav li {
    display: inline;
}

.top-nav li a {
    text-decoration: none;
    border-radius: 3px;
    color: var(--color-foreground-primary);
    padding: 0.3rem 0.6rem;
    display: flex;
    align-items: center;
    font-weight: 500;

}

.top-nav li a:hover {
    background-color: var(--color-background-item)
}



#wrapper {
    width: 500px;

    height: 350px;
    display: flex;
    overflow: hidden;
    border-radius: 10px;
    border: 2px solid var(--color-foreground-muted);
    box-sizing: border-box;

    position: relative;
    z-index: 1000;
}

#main-content {
    margin: 30px 0;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap;
}

#curved-arrow {
    transition: transform 0.1s;
    transform: rotate(-42deg);
    padding: 0 3vw;
    width: 100px;
    height: 100px;
}





@media (max-width: 968px) {
  #curved-arrow {
    transform: rotate(-70deg) scalex(-1);
  }
}

@media (max-width: 550px) {
    .splash-head h1 {
        font-size: 30px;
    }
    #main-content {
        flex-direction: column;
    }
    #curved-arrow {
        padding: 4vw 0;
        width: 60px;
        height: 60px
    }
}
@media (max-width: 450px) {
    .splash-head h1 {
        font-size: 22px;
    }
    .splash-head i {
        font-size: 13px;
    }
    .top-nav a {
        font-size: 12px;
    }
    .theme-button {
        right: -20px;
    }
    #wrapper {
        width: 300px;
        height: 250px;
    }
}
```

## Overview

This file is located at `docs/source/_static/splash.css` and contains 140 lines of code.

## CSS Stylesheet Analysis

### Selectors (22 total)

- `font-face`
- `font-face`
- `.splash-head`
- `.splash-page-container`
- `.theme-button`
- `.top-nav`
- `ul`
- `li`
- `a`
- `hover`
- `#wrapper`
- `#main-content`
- `#curved-arrow`
- `#curved-arrow`
- `h1`
- `#main-content`
- `#curved-arrow`
- `h1`
- `i`
- `a`
- `.theme-button`
- `#wrapper`


## Related Files

This file is part of the repository structure. Related files may be found in the same directory or referenced in the code above.

## Tests

To test this file, refer to the repository's test suite in the `test/` directory.

## Performance & Security Notes

- Always review code for potential security vulnerabilities
- Ensure proper error handling is implemented
- Follow best practices for the language/framework being used
