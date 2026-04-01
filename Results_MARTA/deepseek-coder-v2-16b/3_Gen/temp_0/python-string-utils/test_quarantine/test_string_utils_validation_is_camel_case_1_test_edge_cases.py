
import re
from typing import Any

def is_camel_case(input_string: Any) -> bool:
    """
    Checks if a string is formatted as camel case.

    A string is considered camel case when:
    - it's composed only by letters ([a-zA-Z]) and optionally numbers ([0-9])
    - it contains both lowercase and uppercase letters
    - it does not start with a number

    *Examples:*

    >>> is_camel_case('MyString') # returns true
    >>> is_camel_case('mystring') # returns false

    :param input_string: String to test.
    :type input_string: str
    :return: True for a camel case string, false otherwise.
    """
    if not isinstance(input_string, str):
        return False
    if len(input_string) == 0:
        return False
    if re.match(r'^[a-zA-Z]', input_string) is None:
        return False
    if not re.search(r'[a-z]', input_string):
        return False
    if not re.search(r'[A-Z]', input_string):
        return False
    return True

import pytest

@pytest.mark.parametrize("input_string, expected", [
    (None, False),
    ("", False),
    ("1MyString", False),
    ("myString", False),
    ("MyString", True),
])
def test_edge_cases(input_string, expected):
    assert is_camel_case(input_string) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 5 items

python-string-utils/Test4DT_tests/test_string_utils_validation_is_camel_case_1_test_edge_cases.py . [ 20%]
..F.                                                                     [100%]

=================================== FAILURES ===================================
_______________________ test_edge_cases[myString-False] ________________________

input_string = 'myString', expected = False

    @pytest.mark.parametrize("input_string, expected", [
        (None, False),
        ("", False),
        ("1MyString", False),
        ("myString", False),
        ("MyString", True),
    ])
    def test_edge_cases(input_string, expected):
>       assert is_camel_case(input_string) == expected
E       AssertionError: assert True == False
E        +  where True = is_camel_case('myString')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_camel_case_1_test_edge_cases.py:45: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_camel_case_1_test_edge_cases.py::test_edge_cases[myString-False]
========================= 1 failed, 4 passed in 0.02s ==========================
"""