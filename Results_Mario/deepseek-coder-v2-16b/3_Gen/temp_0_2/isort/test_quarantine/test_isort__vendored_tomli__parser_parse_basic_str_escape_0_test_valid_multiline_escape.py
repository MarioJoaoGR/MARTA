
from isort._vendored.tomli._parser import parse_basic_str_escape
from isort._vendored.tomli._constants import BASIC_STR_ESCAPE_REPLACEMENTS, Pos, TOML_WS, TOML_WS_AND_NEWLINE
from typing import Tuple

def test_valid_multiline_escape():
    # Test case for parsing a multiline string with escape sequences
    src = "Hello\\\nWorld"
    pos = 0
    new_pos, parsed_str = parse_basic_str_escape(src, pos, multiline=True)
    assert parsed_str == "Hello\nWorld", f"Expected 'Hello\\nWorld', but got {parsed_str}"
    assert new_pos == len(src), f"Expected position to be at the end of the string, but it is at {new_pos}"

# Add more test cases if needed

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__parser_parse_basic_str_escape_0_test_valid_multiline_escape
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_escape_0_test_valid_multiline_escape.py:3:0: E0401: Unable to import 'isort._vendored.tomli._constants' (import-error)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_escape_0_test_valid_multiline_escape.py:3:0: E0611: No name '_constants' in module 'isort._vendored.tomli' (no-name-in-module)


"""