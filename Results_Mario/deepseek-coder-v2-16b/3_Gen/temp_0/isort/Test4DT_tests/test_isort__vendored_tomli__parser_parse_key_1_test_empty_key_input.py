
from isort._vendored.tomli._parser import parse_key, Pos, Key, TOMLDecodeError
import pytest

def test_empty_key_input():
    src = ""
    pos = Pos(0)
    
    with pytest.raises(TOMLDecodeError):
        new_pos, parsed_key = parse_key(src, pos)
