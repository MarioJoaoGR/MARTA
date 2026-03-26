
import pytest
from isort._vendored.tomli._parser import parse_hex_char, HEXDIGIT_CHARS, is_unicode_scalar_value, suffixed_err
from typing import Tuple, Pos

def test_invalid_input():
    with pytest.raises(ValueError) as excinfo:
        pos, char = parse_hex_char("1a3g", 0, 2)
    assert str(excinfo.value) == "Invalid hex value"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__parser_parse_hex_char_1_test_invalid_input
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_hex_char_1_test_invalid_input.py:4:0: E0611: No name 'Pos' in module 'typing' (no-name-in-module)


"""