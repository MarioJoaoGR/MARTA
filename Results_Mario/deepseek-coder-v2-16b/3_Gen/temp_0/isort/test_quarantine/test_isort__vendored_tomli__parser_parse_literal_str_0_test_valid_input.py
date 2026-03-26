
from isort._vendored.tomli._parser import parse_literal_str, skip_until, ILLEGAL_LITERAL_STR_CHARS
from typing import Tuple, Pos

def test_valid_input():
    src = "hello 'world'"
    pos = 0
    new_pos, parsed_str = parse_literal_str(src, pos)
    assert parsed_str == "hello 'world'", f"Expected 'hello 'world', but got {parsed_str}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__parser_parse_literal_str_0_test_valid_input
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_literal_str_0_test_valid_input.py:3:0: E0611: No name 'Pos' in module 'typing' (no-name-in-module)


"""