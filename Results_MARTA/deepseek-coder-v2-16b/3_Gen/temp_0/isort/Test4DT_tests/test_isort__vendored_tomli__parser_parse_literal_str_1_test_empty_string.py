
import pytest

from isort._vendored.tomli._parser import parse_literal_str


def test_empty_string():
    src = "''"
    pos = 0
    new_pos, parsed_str = parse_literal_str(src, pos)
    assert parsed_str == ''
    assert new_pos == 2
