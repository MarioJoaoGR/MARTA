
import pytest

from isort._vendored.tomli._parser import (Pos, TOMLDecodeError,
                                           parse_basic_str_escape)


def test_valid_input():
    src = 'This is a test string without any escape sequences'
    pos = Pos(0)
    with pytest.raises(TOMLDecodeError) as excinfo:
        parse_basic_str_escape(src, pos)
    assert str(excinfo.value) == "Unescaped \"\\\" in a string (at line 1, column 3)"
