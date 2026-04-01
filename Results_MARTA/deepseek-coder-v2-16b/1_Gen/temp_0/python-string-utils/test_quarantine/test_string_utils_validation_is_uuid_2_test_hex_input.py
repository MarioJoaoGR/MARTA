
import re
from uuid import UUID

# Define regular expressions for standard and hex UUIDs
UUID_RE = re.compile(r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$', re.IGNORECASE)
UUID_HEX_OK_RE = re.compile(r'^[0-9a-f]{32}$', re.IGNORECASE)

def is_uuid(input_string: str, allow_hex: bool = False) -> bool:
    """
    Check if a string is a valid UUID.

    This function validates whether the provided input string conforms to the universally unique identifier (UUID) format. It supports both standard UUID formats and allows for hexadecimal representation when specified.

    *Examples:*

    >>> is_uuid('6f8aa2f9-686c-4ac3-8766-5712354a04cf') # returns True
    >>> is_uuid('6f8aa2f9686c4ac387665712354a04cf') # returns False
    >>> is_uuid('6f8aa2f9686c4ac387665712354a04cf', allow_hex=True) # returns True

    :param input_string: The string to be checked for UUID validity. It must be a string (str).
    :param allow_hex: A boolean flag that, when set to True, allows the function to validate strings that represent a hexadecimal UUID. Default is False.
    :return: Returns True if the input string is a valid UUID according to the specified conditions, otherwise returns False.
    """
    s = str(input_string)

    if allow_hex:
        return UUID_HEX_OK_RE.match(s) is not None

    return UUID_RE.match(s) is not None

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