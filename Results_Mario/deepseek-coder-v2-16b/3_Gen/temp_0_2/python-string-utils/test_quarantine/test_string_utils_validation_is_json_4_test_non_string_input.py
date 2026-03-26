
import json
from typing import Any
from string_utils.validation import is_full_string, JSON_WRAPPER_RE

def is_json(input_string: Any) -> bool:
    """
    Check if a string is a valid JSON.

    This function verifies whether the provided `input_string` is a valid JSON object or array by attempting to parse it using `json.loads`. It first ensures that the input string is not empty and contains at least one non-whitespace character (using the `is_full_string` function). Then, it checks if the parsed result is either a dictionary (`dict`) or a list.

    *Examples:*

    - When you pass a valid JSON string to the function, it will return `True`:
      ```python
      >>> is_json('{"name": "Peter"}')  # returns True
      >>> is_json('[1, 2, 3]')  # returns True
      ```

    - When you pass an invalid JSON string or a non-string input to the function, it will return `False`:
      ```python
      >>> is_json('{nope}')  # returns False
      >>> is_json(None)  # returns False
      >>> is_json('')  # returns False
      >>> is_json(' ')  # returns False
      ```

    :param input_string: The string to check. It must be a valid JSON object or array for the function to return `True`.
    :type input_string: str
    :return: True if the input string is a valid JSON, False otherwise.
    """
    if is_full_string(input_string) and JSON_WRAPPER_RE.match(input_string) is not None:
        try:
            parsed = json.loads(input_string)
            return isinstance(parsed, (dict, list))
        except (TypeError, ValueError, OverflowError):
            pass
    return False

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items

--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
============================ no tests ran in 0.02s =============================
"""