
import pytest
from string_utils.manipulation import is_string, InvalidInputError

def booleanize(input_string: str) -> bool:
    """
    Turns a string into a boolean based on its content (CASE INSENSITIVE).

    A positive boolean (True) is returned if the string value is one of the following:

    - "true"
    - "1"
    - "yes"
    - "y"

    Otherwise False is returned.

    *Examples:*

    >>> booleanize('true') # returns True
    >>> booleanize('YES') # returns True
    >>> booleanize('nope') # returns False

    :param input_string: String to convert
    :type input_string: str
    :return: True if the string contains a boolean-like positive value, false otherwise
    """
    if not is_string(input_string):
        raise InvalidInputError(input_string)

    return input_string.lower() in ('true', '1', 'yes', 'y')

def test_invalid_input():
    with pytest.raises(InvalidInputError):
        booleanize('nope')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_manipulation_booleanize_2_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
>       with pytest.raises(InvalidInputError):
E       Failed: DID NOT RAISE <class 'string_utils.errors.InvalidInputError'>

python-string-utils/Test4DT_tests/test_string_utils_manipulation_booleanize_2_test_invalid_input.py:34: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation_booleanize_2_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.03s ===============================
"""