
import re
from isort._vendored.tomli._re import match_to_number, parse_float
import pytest

@pytest.mark.parametrize("match, expected", [
    (re.Match(0, "123.456"), 123.456),
    (re.Match(0, "789"), 789),
])
def test_valid_input_with_decimal(match, expected):
    assert match_to_number(match, parse_float) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__re_match_to_number_0_test_valid_input_with_decimal
isort/Test4DT_tests/test_isort__vendored_tomli__re_match_to_number_0_test_valid_input_with_decimal.py:3:0: E0611: No name 'parse_float' in module 'isort._vendored.tomli._re' (no-name-in-module)


"""