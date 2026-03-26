
import pytest
from typing import Tuple
from isort._vendored.tomli._parser import parse_basic_str

# Assuming Pos and ILLEGAL_BASIC_STR_CHARS, ILLEGAL_MULTILINE_BASIC_STR_CHARS are defined elsewhere in the module

def test_parse_basic_str_non_multiline():
    src = "Hello, \\nworld!"
    pos = 0
    result = parse_basic_str(src, pos, multiline=False)
    assert result[1] == "Hello, world!"

def test_parse_basic_str_multiline():
    multiline_src = "\\n\\tThis is a test."
    pos = 0
    result = parse_basic_str(multiline_src, pos, multiline=True)
    assert result[1] == "	This is a test."

def test_parse_basic_str_unterminated():
    src = "Hello, \\nworld!"
    pos = 0
    with pytest.raises(isort._vendored.tomli._parser.TOMLDecodeError):
        parse_basic_str(src, pos, multiline=False)

def test_parse_basic_str_illegal_character():
    src = "Hello, \\xworld!"
    pos = 0
    with pytest.raises(isort._vendored.tomli._parser.TOMLDecodeError):
        parse_basic_str(src, pos, multiline=False)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__parser_parse_basic_str_0
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_0.py:23:23: E0602: Undefined variable 'isort' (undefined-variable)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_0.py:29:23: E0602: Undefined variable 'isort' (undefined-variable)


"""