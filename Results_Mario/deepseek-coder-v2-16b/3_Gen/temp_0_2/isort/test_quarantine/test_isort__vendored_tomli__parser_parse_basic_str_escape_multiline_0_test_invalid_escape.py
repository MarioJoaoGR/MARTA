
import pytest
from isort._vendored.tomli._parser import parse_basic_str_escape_multiline
from isort._vendored.tomli._shared_lib import Pos

def test_invalid_escape():
    with pytest.raises(ValueError):
        src = "Hello\\xWorld"
        pos = Pos(0)
        parse_basic_str_escape_multiline(src, pos)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__parser_parse_basic_str_escape_multiline_0_test_invalid_escape
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_escape_multiline_0_test_invalid_escape.py:4:0: E0401: Unable to import 'isort._vendored.tomli._shared_lib' (import-error)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_escape_multiline_0_test_invalid_escape.py:4:0: E0611: No name '_shared_lib' in module 'isort._vendored.tomli' (no-name-in-module)


"""