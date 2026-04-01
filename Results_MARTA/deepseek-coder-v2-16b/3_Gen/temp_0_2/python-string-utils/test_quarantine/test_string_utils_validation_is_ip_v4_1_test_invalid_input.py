
import re
from typing import Any
from string_utils.validation import is_full_string, SHALLOW_IP_V4_RE

def is_ip_v4(input_string: Any) -> bool:
    """
    Checks if a string is a valid IPv4 address.

    This function verifies whether the provided `input_string` is a valid IPv4 address by checking two main conditions:
    1. The string contains at least one non-space character and is not empty (checked using `is_full_string`).
    2. The string matches the regular expression pattern for IPv4 addresses (`SHALLOW_IP_V4_RE`).
    Additionally, it ensures that each segment of the IP address (separated by dots) is within the valid range of 0 to 255.

    *Examples:*

    - Valid IPv4 address:
      ```python
      >>> is_ip_v4('255.200.100.75')  # returns True
      ```

    - Invalid input (not an IP):
      ```python
      >>> is_ip_v4('nope')  # returns False
      ```

    - Invalid IPv4 address due to out-of-range segment:
      ```python
      >>> is_ip_v4('255.200.100.999')  # returns False
      ```

    :param input_string: The string to check for validity as an IPv4 address.
    :type input_string: str
    :return: True if the string is a valid IPv4 address, False otherwise.
    """
    if not is_full_string(input_string) or SHALLOW_IP_V4_RE.match(input_string) is None:
        return False

    # checks that each entry in the ip is in the valid range (0 to 255)
    for token in input_string.split('.'):
        if not (0 <= int(token) <= 255):
            return False

    return True

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
============================ no tests ran in 0.01s =============================
"""