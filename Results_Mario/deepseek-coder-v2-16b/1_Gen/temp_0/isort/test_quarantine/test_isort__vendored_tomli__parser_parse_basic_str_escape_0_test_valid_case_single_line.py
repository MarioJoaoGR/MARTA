
import pytest
from isort._vendored.tomli._parser import parse_basic_str_escape, TOMLDecodeError
from isort._vendored.tomli._shared_types import Pos

def test_valid_case_single_line():
    src = 'Hello\nWorld'
    pos = Pos(0)
    with pytest.raises(TOMLDecodeError) as excinfo:
        parse_basic_str_escape(src, pos)
    assert str(excinfo.value) == "Unescaped \"\\\" in a string (at line 1, column 3)"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__parser_parse_basic_str_escape_0_test_valid_case_single_line
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_escape_0_test_valid_case_single_line.py:4:0: E0401: Unable to import 'isort._vendored.tomli._shared_types' (import-error)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_escape_0_test_valid_case_single_line.py:4:0: E0611: No name '_shared_types' in module 'isort._vendored.tomli' (no-name-in-module)


"""