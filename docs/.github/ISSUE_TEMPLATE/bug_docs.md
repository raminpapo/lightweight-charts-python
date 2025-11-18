# bug.yaml

**File Path:** `.github/ISSUE_TEMPLATE/bug.yaml`

**File Size:** 1,666 bytes
**Lines of Code:** 49
**Language:** yaml

---

## File Metadata

- **Relative Path:** `.github/ISSUE_TEMPLATE/bug.yaml`
- **File Type:** .yaml
- **Size:** 1,666 bytes
- **Total Lines:** 49
- **Programming Language:** yaml

## Quick Summary

This file is part of the lightweight-charts-python repository.


## Original Source Code

```yaml

name: Bug Report
description: Report a bug/problem with the library
title: "[BUG] "
labels: ["bug"]

body:
  - type: textarea
    id: expected-behavior
    attributes:
      label: Expected Behavior
      description: >
        Please describe or show a code example of the expected behavior.
    validations:
      required: true

  - type: textarea
    id: current-behavior
    attributes:
      label: Current Behaviour
      description: >
        Please provide a description of the current behaviour. If this is a bug which produces no errors in Python, but causes unexpected output within the webview, please provide a screenshot of the web console using `Chart(debug=True)`.
    validations:
      required: true

  - type: textarea
    id: example
    attributes:
      label: Reproducible Example
      description: >
        Please provide a minimal reproducible example, using generic (`ohlcv.csv`) data where applicable which demonstrates the current behaviour. The code should be complete and not require any further adjustments. DO NOT provide: Incomplete code, unnecessarily long code, code which requires access to a broker/API, or code which uses additional functions/classes/libraries. In almost ALL cases the example should not exceed 50 lines.
      placeholder: >
        from lightweight_charts import Chart...
      render: python
    validations:
      required: true

  - type: textarea
    attributes:
      label: Environment
      description: |
        examples:
          - **OS**: macOS 13.2
          - **Library**: 1.0.16.2
      value: |
        - OS:
        - Library:
      render: markdown
    validations:
      required: true

```

## High-Level Overview

## Detailed Walkthrough

### Code Structure

This file contains 49 lines of yaml.
## Usage Examples

To use this file in your project:

## Performance & Security Notes

### Performance

- File size: 1,666 bytes
- Complexity: 0 functions, 0 classes

### Security

- **Recommendation:** Review this file for potential security vulnerabilities
- No obvious security concerns detected (basic scan)

## Related Files

*To be populated during folder indexing phase*

## Testing

Tests for this file may be located in the `test/` directory.

---

*Documentation generated on 2025-11-18T21:53:49.021878*
