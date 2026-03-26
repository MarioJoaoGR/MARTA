
from isort._vendored.tomli._parser import parse_multiline_str
from isort._vendored.tomli._parser import Pos
from typing import Tuple

def test_valid_multiline_literal():
    # Test parsing a valid multi-line literal string
    src = "'''Hello\nworld'''"
    pos = 0
    new_pos, parsed_str = parse_multiline_str(src, pos, literal=True)
    assert new_pos == len(src)
    assert parsed_str == "Hello\nworld"

    # Test parsing a basic string with multi-line support
    src = '"""Hello\nworld"""'
    pos = 0
    new_pos, parsed_str = parse_multiline_str(src, pos, literal=False)
    assert new_pos == len(src)
    assert parsed_str == "Hello\nworld"
