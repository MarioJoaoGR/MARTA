
import pytest

from isort._vendored.tomli._parser import Pos, parse_basic_str_escape


def test_valid_input_happy_path():
    src = '\\u1234\\U0010FFFF'
    pos = Pos(0)
    result = parse_basic_str_escape(src, pos)
    assert result == (Pos(6), "\u1234")
