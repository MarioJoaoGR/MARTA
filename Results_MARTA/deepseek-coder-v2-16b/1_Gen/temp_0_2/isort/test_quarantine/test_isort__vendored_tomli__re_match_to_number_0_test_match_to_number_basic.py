
import re
from isort._vendored.tomli._re import match_to_number, parse_float
import pytest

@pytest.mark.parametrize("input_string, expected", [
    ("123", 123),
    ("-456", -456),
    ("123.45", 123.45),
    ("-789.01", -789.01),
    (".234", 0.234),
    ("1e-6", 1e-6),
    ("-2e+7", -2e+7)
])
def test_match_to_number(input_string, expected):
    pattern = r'-?\d+(\.\d+)?|\.\d+|\d+\.\d*'
    match_obj = re.match(pattern, input_string)
    
    if match_obj:
        result = match_to_number(match_obj, parse_float)
        assert result == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__re_match_to_number_0_test_match_to_number_basic
isort/Test4DT_tests/test_isort__vendored_tomli__re_match_to_number_0_test_match_to_number_basic.py:3:0: E0611: No name 'parse_float' in module 'isort._vendored.tomli._re' (no-name-in-module)


"""