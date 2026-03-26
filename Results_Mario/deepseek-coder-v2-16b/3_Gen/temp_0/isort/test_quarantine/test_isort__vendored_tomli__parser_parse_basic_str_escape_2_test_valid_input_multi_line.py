
from isort._vendored.tomli._parser import parse_basic_str_escape
from isort._vendored.tomli._shared_types import Pos, TOML_WS, TOML_WS_AND_NEWLINE, BASIC_STR_ESCAPE_REPLACEMENTS
from typing import Tuple

def test_valid_input_multi_line():
    src = "\\\n \t"
    pos = 0
    result = parse_basic_str_escape(src, pos, multiline=True)
    assert result == (3, "")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__parser_parse_basic_str_escape_2_test_valid_input_multi_line
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_escape_2_test_valid_input_multi_line.py:3:0: E0401: Unable to import 'isort._vendored.tomli._shared_types' (import-error)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_escape_2_test_valid_input_multi_line.py:3:0: E0611: No name '_shared_types' in module 'isort._vendored.tomli' (no-name-in-module)


"""