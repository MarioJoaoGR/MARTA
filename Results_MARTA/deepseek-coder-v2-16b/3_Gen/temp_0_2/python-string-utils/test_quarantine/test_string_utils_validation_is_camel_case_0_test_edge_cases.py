
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
    return is_full_string(input_string) and CAMEL_CASE_TEST_RE.match(input_string) is not None

# Assuming this import is correct based on the context of your module
from string_utils.validation import is_full_string, CAMEL_CASE_TEST_RE

import pytest

@pytest.mark.parametrize("test_input, expected", [
    (None, False),
    ("", False),
    ("1MyString", False),
    ("myString", False),
    ("MyString", True),
    ("mystring", False),
])
def test_edge_cases(test_input, expected):
    assert is_camel_case(test_input) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 6 items

python-string-utils/Test4DT_tests/test_string_utils_validation_is_camel_case_0_test_edge_cases.py . [ 16%]
..F..                                                                    [100%]

=================================== FAILURES ===================================
_______________________ test_edge_cases[myString-False] ________________________

test_input = 'myString', expected = False

    @pytest.mark.parametrize("test_input, expected", [
        (None, False),
        ("", False),
        ("1MyString", False),
        ("myString", False),
        ("MyString", True),
        ("mystring", False),
    ])
    def test_edge_cases(test_input, expected):
>       assert is_camel_case(test_input) == expected
E       AssertionError: assert True == False
E        +  where True = is_camel_case('myString')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_camel_case_0_test_edge_cases.py:39: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_camel_case_0_test_edge_cases.py::test_edge_cases[myString-False]
========================= 1 failed, 5 passed in 0.03s ==========================
"""