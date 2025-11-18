# question.yaml

**File Path:** `.github/ISSUE_TEMPLATE/question.yaml`

**File Size:** 605 bytes
**Lines of Code:** 26
**Language:** yaml

---

## File Metadata

- **Relative Path:** `.github/ISSUE_TEMPLATE/question.yaml`
- **File Type:** .yaml
- **Size:** 605 bytes
- **Total Lines:** 26
- **Programming Language:** yaml

## Quick Summary

This file is part of the lightweight-charts-python repository.


## Original Source Code

```yaml

name: General Question
description: Ask a question/get help with the library

body:
  - type: textarea
    id: question
    attributes:
      label: Question
      description: >
        Please check previous issues before submitting. Please use screenshots if they help!
    validations:
      required: true

  - type: textarea
    id: code-behaviour
    attributes:
      label: Code example
      description: >
        Please provide any code relevant to your question.
      placeholder: >
        from lightweight_charts import Chart...
      render: python
    validations:
      required: false



```

## High-Level Overview

## Detailed Walkthrough

### Code Structure

This file contains 26 lines of yaml.
## Usage Examples

To use this file in your project:

## Performance & Security Notes

### Performance

- File size: 605 bytes
- Complexity: 0 functions, 0 classes

### Security

- **Recommendation:** Review this file for potential security vulnerabilities
- No obvious security concerns detected (basic scan)

## Related Files

*To be populated during folder indexing phase*

## Testing

Tests for this file may be located in the `test/` directory.

---

*Documentation generated on 2025-11-18T21:53:49.023258*
