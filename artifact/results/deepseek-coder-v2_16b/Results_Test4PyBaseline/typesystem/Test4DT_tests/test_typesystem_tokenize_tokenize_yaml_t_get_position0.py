
import pytest
from typesystem.tokenize.tokenize_yaml import _get_position, Position

# Test cases for _get_position function

def test_basic_usage():
    text = "line1\nline2\nline3"
    index = 8
    pos = _get_position(text, index)
    assert pos.line_no == 2
    assert pos.column_no == 3
    assert pos.char_index == 8

def test_edge_case_index_at_start_of_line():
    text = "line1\nline2\nline3"
    index = 0
    pos = _get_position(text, index)
    assert pos.line_no == 1