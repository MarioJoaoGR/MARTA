
# Module: isort._vendored.tomli._parser
import pytest
from tomli._parser import Pos, parse_basic_str, suffixed_err

# Define constants for testing
ILLEGAL_BASIC_STR_CHARS = " \t\n\r"
ILLEGAL_MULTILINE_BASIC_STR_CHARS = "\""

def test_parse_basic_str_single_line():
    src = 'This is a single-line string.'
    pos = Pos(0)
    result = parse_basic_str(src, pos, multiline=False)
    assert result == (Pos(1), 'This is a single-line string.')

def test_parse_basic_str_multi_line():
    src = '''This is the first line.
This is the second line.'''
    pos = Pos(0)
    result = parse_basic_str(src, pos, multiline=True)
    assert result == (Pos(3), 'This is the first line.\nThis is the second line.')

def test_parse_basic_str_unterminated():
    src = 'This string is not terminated.'
    pos = Pos(0)
    with pytest.raises(suffixed_err):
        parse_basic_str(src, pos, multiline=False)

def test_parse_basic_str_illegal_char():
    src = 'This string contains\na newline character.'
    pos = Pos(0)
    with pytest.raises(suffixed_err):
        parse_basic_str(src, pos, multiline=False)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__parser_parse_basic_str_0
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_0.py:4:0: E0611: No name 'Pos' in module 'tomli._parser' (no-name-in-module)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_0.py:4:0: E0611: No name 'parse_basic_str' in module 'tomli._parser' (no-name-in-module)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_0.py:4:0: E0611: No name 'suffixed_err' in module 'tomli._parser' (no-name-in-module)


"""