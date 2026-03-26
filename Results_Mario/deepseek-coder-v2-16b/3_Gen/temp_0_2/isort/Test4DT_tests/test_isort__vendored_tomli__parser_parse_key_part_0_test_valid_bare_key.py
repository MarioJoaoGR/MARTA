
from typing import Tuple
from isort._vendored.tomli._parser import parse_key_part, BARE_KEY_CHARS, Pos
import pytest

def test_valid_bare_key():
    src = "hello_world"
    pos = 0
    new_pos, key_part = parse_key_part(src, pos)
    assert new_pos == len("hello_world")
    assert key_part == "hello_world"
