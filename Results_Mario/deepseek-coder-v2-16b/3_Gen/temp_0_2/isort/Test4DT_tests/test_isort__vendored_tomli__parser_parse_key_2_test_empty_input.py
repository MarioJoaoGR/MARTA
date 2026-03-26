
import pytest
from isort._vendored.tomli._parser import parse_key, TOMLDecodeError

def test_empty_input():
    src = ''
    pos = 0
    with pytest.raises(TOMLDecodeError):
        new_pos, key = parse_key(src, pos)
