
import re
from isort._vendored.tomli._re import match_to_number, parse_float

def test_invalid_input():
    pattern = re.compile(r"(\d+)(?:\.(\d+)?)?")
    
    # Test with a valid number containing a decimal point
    match = pattern.search("123.456")
    result = match_to_number(match, parse_float)
    assert isinstance(result, float), f"Expected float but got {type(result)}"
    
    # Test with an invalid number (no decimal point)
    match = pattern.search("789")
    result = match_to_number(match, parse_float)
    assert isinstance(result, int), f"Expected integer but got {type(result)}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__re_match_to_number_0_test_invalid_input
isort/Test4DT_tests/test_isort__vendored_tomli__re_match_to_number_0_test_invalid_input.py:3:0: E0611: No name 'parse_float' in module 'isort._vendored.tomli._re' (no-name-in-module)


"""