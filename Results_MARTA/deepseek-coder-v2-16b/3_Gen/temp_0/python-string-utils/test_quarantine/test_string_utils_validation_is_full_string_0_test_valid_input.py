
import re
from typing import Any

def is_full_string(input_string: Any) -> bool:
    """
    Check if a string contains at least one non-space character and is not empty.

    This function verifies whether the provided `input_string` is a non-empty string, meaning it must contain at least one character that is not a whitespace character (e.g., space, tab, newline). The function returns `True` if the string meets this criterion, and `False` otherwise.

    *Examples:*

    - When you pass `None` to the function, it will return `False`:
      ```python
      >>> is_full_string(None)  # returns False
      ```
    - When you pass an empty string to the function, it will return `False`:
      ```python
      >>> is_full_string('')  # returns False
      ```
    - When you pass a string that consists only of whitespace characters to the function, it will return `False`:
      ```python
      >>> is_full_string(' ')  # returns False
      ```
    - When you pass a non-empty string (containing at least one non-space character) to the function, it will return `True`:
      ```python
      >>> is_full_string('hello')  # returns True
      ```

    :param input_string: The string to check.
    :type input_string: str
    :return: True if the string contains at least one non-space character and is not empty, False otherwise.
    """
    return isinstance(input_string, str) and bool(re.search('\S', input_string))
```

And here's the pytest function to test this functionality:

```python
import pytest
from string_utils.validation import is_full_string

def test_valid_input():
    # Test None input
    assert not is_full_string(None)
    
    # Test empty string
    assert not is_full_string('')
    
    # Test whitespace only string
    assert not is_full_string(' ')
    
    # Test non-empty string with at least one non-space character
    assert is_full_string('hello')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_validation_is_full_string_0_test_valid_input
python-string-utils/Test4DT_tests/test_string_utils_validation_is_full_string_0_test_valid_input.py:37:9: E0001: Parsing failed: 'unterminated string literal (detected at line 37) (Test4DT_tests.test_string_utils_validation_is_full_string_0_test_valid_input, line 37)' (syntax-error)


"""