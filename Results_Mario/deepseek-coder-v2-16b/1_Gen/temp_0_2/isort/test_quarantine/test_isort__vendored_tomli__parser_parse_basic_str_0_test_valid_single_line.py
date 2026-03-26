
import pytest
from isort._vendored.tomli._parser import parse_basic_str, POS, suffixed_err

def test_valid_single_line():
    src = 'hello world'
    pos = 0
    result = parse_basic_str(src, pos, multiline=False)
    assert result == (len(src), src)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__parser_parse_basic_str_0_test_valid_single_line
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_0_test_valid_single_line.py:3:0: E0611: No name 'POS' in module 'isort._vendored.tomli._parser' (no-name-in-module)


"""