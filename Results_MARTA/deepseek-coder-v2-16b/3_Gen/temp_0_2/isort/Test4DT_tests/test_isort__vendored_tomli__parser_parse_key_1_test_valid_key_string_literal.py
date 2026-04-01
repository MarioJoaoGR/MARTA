
import pytest
from isort._vendored.tomli._parser import parse_key, Pos
from typing import Tuple, Optional

def test_valid_key_string_literal():
    src = '"hello".world'
    pos = 0
    new_pos, key = parse_key(src, pos)
    assert new_pos == len('"hello".world')
    assert key == ('hello', 'world')
