
# Module: isort._vendored.tomli._parser
import pytest
from tomli import Pos  # Corrected import statement for 'Pos'
from typing import Tuple
from isort._vendored.tomli._parser import parse_one_line_basic_str

# Test cases for single-line string parsing
def test_parse_single_line_string():
    src = "Hello, world!"
    pos = Pos(0)  # Assuming 'Pos' is correctly defined in the tomli module
    result = parse_one_line_basic_str(src, pos)
    assert result == (Pos(13), "Hello, world!")

# Test cases for multi-line string parsing
def test_parse_multi_line_string():
    src = """Hello, world!
    This is a multi-line string."""
    pos = Pos(0)  # Assuming 'Pos' is correctly defined in the tomli module
    result = parse_one_line_basic_str(src, pos)
    assert result == (Pos(39), "Hello, world!\nThis is a multi-line string.")

# Test cases for parsing from different positions within the same multi-line string
def test_parse_multi_line_string_different_positions():
    src = """Hello, world!
    This is a multi-line string."""
    pos1 = Pos(0)  # Starting at the beginning of the first line
    result1 = parse_one_line_basic_str(src, pos1)
    
    pos2 = Pos(14)  # Starting in the middle of the first line
    result2 = parse_one_line_basic_str(src, pos2)
    
    assert result1 == (Pos(13), "Hello, world!")
    assert result2 == (Pos(28), "world!\nThis is a multi-line string.")

# Test cases for edge cases
def test_parse_empty_string():
    src = ""
    pos = Pos(0)  # Assuming 'Pos' is correctly defined in the tomli module
    with pytest.raises(IndexError):
        parse_one_line_basic_str(src, pos)

def test_parse_position_beyond_end():
    src = "Hello, world!"
    pos = Pos(100)  # Position beyond the end of the string
    with pytest.raises(IndexError):
        parse_one_line_basic_str(src, pos)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__parser_parse_one_line_basic_str_0
isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_one_line_basic_str_0.py:4:0: E0611: No name 'Pos' in module 'tomli' (no-name-in-module)


"""