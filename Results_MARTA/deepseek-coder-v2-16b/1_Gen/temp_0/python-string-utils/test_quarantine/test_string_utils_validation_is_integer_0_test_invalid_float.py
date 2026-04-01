
import re

def is_number(input_string: str) -> bool:
    """
    Checks whether the given string can be converted to a float, which includes integers in their standard form.
    
    This function verifies whether the provided input can be successfully converted to a float without raising any exceptions. It returns `True` if the conversion is possible and the value is within the range of standard floats, and `False` otherwise. The function supports scientific notation for floating-point numbers.
    
    *Examples:*
    
    >>> is_number('42') # returns true
    >>> is_number('-42') # returns true
    >>> is_number('+42') # returns true
    >>> is_number('42.0') # returns true
    >>> is_number('1e3') # returns true
    >>> is_number('abc') # returns false
    
    :param input_string: String to check for whether it can be converted to a float.
    :type input_string: str
    :return: True if the string can be converted to a float, False otherwise.
    """
    try:
        float(input_string)
        return True
    except ValueError:
        return False

def is_integer(input_string: str) -> bool:
    """
    Checks whether the given string represents an integer or not.
    
    An integer may be signed or unsigned or use a "scientific notation".
    
    *Examples:*
    
    >>> is_integer('42') # returns true
    >>> is_integer('-42') # returns true
    >>> is_integer('+42') # returns true
    >>> is_integer('42.0') # returns false
    >>> is_integer('1e3') # returns false
    
    :param input_string: String to check
    :type input_string: str
    :return: True if integer, false otherwise
    """
    return is_number(input_string) and '.' not in input_string

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