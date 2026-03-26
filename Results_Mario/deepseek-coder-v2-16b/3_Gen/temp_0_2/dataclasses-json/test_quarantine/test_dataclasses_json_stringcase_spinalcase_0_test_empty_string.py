
import re
from dataclasses_json import stringcase

def spinalcase(string):
    """Convert a given string into spinal case. This involves replacing hyphens, dots, and spaces with hyphens and ensuring the first character is lowercase while subsequent words are joined by hyphens.

    Args:
        string (str): The input string to be converted into spinal case.

    Returns:
        str: The spinal cased version of the input string. If the input string is empty, it returns an empty string.

    Example:
        >>> spinalcase("HelloWorld")
        'hello-world'
        
        >>> spinalcase("Hello-World")
        'hello-world'
        
        >>> spinalcase("Hello World")
        'hello-world'
        
        >>> spinalcase("")
        ''
    """
    if not string:
        return ""
    return re.sub(r"[\s\-.]", "-", stringcase(string).lower())

import pytest

def test_empty_string():
    assert spinalcase("") == ""

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_stringcase_spinalcase_0_test_empty_string
dataclasses-json/Test4DT_tests/test_dataclasses_json_stringcase_spinalcase_0_test_empty_string.py:29:35: E1102: stringcase is not callable (not-callable)


"""