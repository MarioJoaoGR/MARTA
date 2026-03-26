
from typing import Tuple
from isort._vendored.tomli._parser import parse_basic_str_escape
from isort._vendored.tomli._shared_types import Pos
import pytest

def test_valid_input_multiline():
    src = 'This is a "multi\\nline" string with \\u1234 escape.'
    pos = Pos(0)
    
    result_pos, parsed_str = parse_basic_str_escape(src, pos, multiline=True)
    
    assert result_pos == Pos(len(src))
    assert parsed_str == 'This is a "multi\nline" string with \u1234 escape.'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__parser_parse_basic_str_escape_multiline_3_test_valid_input_multiline
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_escape_multiline_3_test_valid_input_multiline.py:4:0: E0401: Unable to import 'isort._vendored.tomli._shared_types' (import-error)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_escape_multiline_3_test_valid_input_multiline.py:4:0: E0611: No name '_shared_types' in module 'isort._vendored.tomli' (no-name-in-module)


"""