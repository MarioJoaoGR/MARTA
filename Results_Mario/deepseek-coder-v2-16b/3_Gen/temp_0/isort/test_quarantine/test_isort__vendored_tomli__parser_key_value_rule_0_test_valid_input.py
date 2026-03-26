
import pytest
from your_module import key_value_rule  # Replace 'your_module' with the actual module name
from isort._vendored.tomli._parser import Pos, Output, Key, ParseFloat

def test_valid_input():
    src = "key=value"
    pos = Pos(0)
    out = Output()
    header = Key(['section'])
    parsed_pos = key_value_rule(src, pos, out, header, float)
    assert parsed_pos == 4  # Assuming the length of 'key' is 4 in this case

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__parser_key_value_rule_0_test_valid_input
isort/Test4DT_tests/test_isort__vendored_tomli__parser_key_value_rule_0_test_valid_input.py:3:0: E0401: Unable to import 'your_module' (import-error)


"""