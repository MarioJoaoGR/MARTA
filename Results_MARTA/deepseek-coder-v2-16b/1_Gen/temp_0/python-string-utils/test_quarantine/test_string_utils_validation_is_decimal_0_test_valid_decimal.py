
import re

def is_decimal(input_string: str) -> bool:
    """
    Checks whether the given string represents a decimal number. A decimal number may be signed or unsigned, and it can include a decimal point followed by digits (optionally with a leading sign). It also supports scientific notation with an 'e' or 'E' followed by an integer.
    
    *Examples:*
    
    >>> is_decimal('42.0') # returns true
    >>> is_decimal('-123.45e6') # returns true
    >>> is_decimal('123') # returns false
    >>> is_decimal('+78.9') # returns true
    >>> is_decimal('abc') # returns false
    
    :param input_string: String to check for whether it represents a decimal number.
    :type input_string: str
    :return: True if the string represents a valid decimal number, False otherwise.
    """
    pattern = re.compile(r"""^[-+]?  # Optional sign at the beginning
                             (\d+\.\d*|\.\d+)  # Decimal point followed by digits (optional)
                             ([eE][-+]?\d+)?$  # Scientific notation with optional exponent
                          """, re.VERBOSE)
    return bool(pattern.match(input_string))

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