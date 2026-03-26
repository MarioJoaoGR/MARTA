
import re
from typing import Any

# Assuming SHALLOW_IP_V4_RE is defined somewhere in the string_utils.validation module
SHALLOW_IP_V4_RE = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')

def is_ip_v4(input_string: Any) -> bool:
    """
    Checks if a string is a valid IPv4 address.

    This function verifies whether the provided `input_string` represents a valid IPv4 address. An IPv4 address consists of four numbers separated by dots, where each number ranges from 0 to 255. The function returns `True` if the input string matches this pattern and all its components are within the valid range, and `False` otherwise.

    *Examples:*

    - Valid IPv4 addresses:
      ```python
      >>> is_ip_v4('255.200.100.75')  # returns True
      ```
    - Invalid IPv4 addresses:
      ```python
      >>> is_ip_v4('nope')  # returns False (not an IP)
      >>> is_ip_v4('255.200.100.999')  # returns False (number out of range)
      >>> is_ip_v4('256.200.100.75')  # returns False (first number out of range)
      >>> is_ip_v4('255.200.100')  # returns False (not enough numbers)
      ```
    - Strings that are not valid IPv4 addresses:
      ```python
      >>> is_ip_v4('nope')  # returns False (not an IP)
      ```

    :param input_string: The string to check for a valid IPv4 address.
    :type input_string: str
    :return: True if the input string is a valid IPv4 address, False otherwise.
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
************* Module Test4DT_tests.test_string_utils_validation_is_ip_v4_0_test_valid_ipv4
python-string-utils/Test4DT_tests/test_string_utils_validation_is_ip_v4_0_test_valid_ipv4.py:36:11: E0602: Undefined variable 'is_full_string' (undefined-variable)


"""