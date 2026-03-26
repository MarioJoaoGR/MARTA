
import re

def is_number(input_string: str) -> bool:
    """
    Checks if a string represents a valid number, including integers and floating-point numbers in scientific notation.

    The function supports signed (e.g., +1, -2, -3.3) or unsigned (e.g., 1, 2, 3.3) numbers as well as numbers using scientific notation (e.g., 1e5).

    *Examples:*

    >>> is_number('42') # returns true
    >>> is_number('19.99') # returns true
    >>> is_number('-9.12') # returns true
    >>> is_number('1e3') # returns true
    >>> is_number('1 2 3') # returns false

    :param input_string: The string to check for whether it represents a valid number.
    :type input_string: str
    :return: True if the string represents a valid number, False otherwise.
    """
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")

    # Regular expression to match numbers including scientific notation and signs
    number_pattern = r'^[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?$'
    return bool(re.match(number_pattern, input_string))

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