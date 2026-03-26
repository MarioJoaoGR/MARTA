
import pytest
from isort._vendored.tomli._parser import parse_basic_str_escape, suffixed_err
from typing import Tuple

def test_parse_basic_str_escape():
    # Test case for a basic string with an escape sequence
    src = "Hello\\nWorld"
    pos = 0
    new_pos, parsed_str = parse_basic_str_escape(src, pos)
    assert parsed_str == "Hello\nWorld", f"Expected 'Hello\\nWorld' to be parsed as 'Hello\\nWorld', but got {parsed_str}"

def test_parse_basic_str_escape_multiline():
    # Test case for a multiline string with an escape sequence
    src = "Hello\\\nWorld"
    pos = 0
    new_pos, parsed_str = parse_basic_str_escape(src, pos, multiline=True)
    assert parsed_str == "Hello\nWorld", f"Expected 'Hello\\nWorld' to be parsed as 'Hello\\nWorld', but got {parsed_str}"

def test_parse_basic_str_escape_invalid():
    # Test case for a string with an invalid escape sequence
    src = "Hello\\xWorld"
    pos = 0
    with pytest.raises(ValueError) as excinfo:
        parse_basic_str_escape(src, pos)
    assert str(excinfo.value) == 'Unescaped "\\" in a string', f"Expected error message to be 'Unescaped \\"\\" in a string', but got {excinfo.value}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__parser_parse_basic_str_escape_0_test_parse_basic_str_escape_basic
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_escape_0_test_parse_basic_str_escape_basic.py:26:110: E0001: Parsing failed: 'unexpected character after line continuation character (Test4DT_tests.test_isort__vendored_tomli__parser_parse_basic_str_escape_0_test_parse_basic_str_escape_basic, line 26)' (syntax-error)


"""