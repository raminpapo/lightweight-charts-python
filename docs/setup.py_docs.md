# setup.py Documentation

## File Metadata
- **Path**: `setup.py`
- **Extension**: `.py`
- **Lines of Code**: 25
- **File Size**: 680 bytes

## Original Source

```py
from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='lightweight_charts',
    version='2.1',
    packages=find_packages(),
    python_requires='>=3.8',
    install_requires=[
        'pandas',
        'pywebview>=5.0.5',
    ],
    package_data={
        'lightweight_charts': ['js/*'],
    },
    author='louisnw',
    license='MIT',
    description="Python framework for TradingView's Lightweight Charts JavaScript library.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/louisnw01/lightweight-charts-python',
)

```

## Overview

This file is located at `setup.py` and contains 25 lines of code.

## Python Code Analysis

### Dependencies

- setup, find_packages


## Related Files

This file is part of the repository structure. Related files may be found in the same directory or referenced in the code above.

## Tests

To test this file, refer to the repository's test suite in the `test/` directory.

## Performance & Security Notes

- Always review code for potential security vulnerabilities
- Ensure proper error handling is implemented
- Follow best practices for the language/framework being used
