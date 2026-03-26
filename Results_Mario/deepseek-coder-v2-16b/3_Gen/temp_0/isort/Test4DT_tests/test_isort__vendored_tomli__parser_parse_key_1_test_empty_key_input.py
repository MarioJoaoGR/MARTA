
import pytest

from isort._vendored.tomli._parser import Key, Pos, TOMLDecodeError, parse_key


def test_empty_key_input():
    src = ""
    pos = Pos(0)
    
    with pytest.raises(TOMLDecodeError):
        new_pos, parsed_key = parse_key(src, pos)
