
import pytest
from isort._vendored.tomli._parser import parse_basic_str_escape, TOMLDecodeError
from isort._vendored.tomli._shared_lib import Pos, skip_chars

TOML_WS = " \t"
TOML_WS_AND_NEWLINE = " \t\n"
BASIC_STR_ESCAPE_REPLACEMENTS = {
    "\\": "\\",
    "\"": "\"",
    "/": "/"
}

def test_valid_case_multi_line():
    src = "\\ \\\t\\\n"
    pos = Pos(0)
    with pytest.raises(TOMLDecodeError, match="Unescaped \\\"\\ in a string"):
        parse_basic_str_escape(src, pos, multiline=True)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__parser_parse_basic_str_escape_0_test_valid_case_multi_line
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_escape_0_test_valid_case_multi_line.py:4:0: E0401: Unable to import 'isort._vendored.tomli._shared_lib' (import-error)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_escape_0_test_valid_case_multi_line.py:4:0: E0611: No name '_shared_lib' in module 'isort._vendored.tomli' (no-name-in-module)


"""