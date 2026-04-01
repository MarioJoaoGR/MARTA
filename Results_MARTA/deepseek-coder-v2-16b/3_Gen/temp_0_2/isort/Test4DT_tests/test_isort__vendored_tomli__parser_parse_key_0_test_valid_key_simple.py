
import pytest
from typing import Tuple, Optional
from isort._vendored.tomli._parser import parse_key, skip_chars, TOML_WS

Key = Tuple[str, ...]
Pos = int

def test_valid_key_simple():
    src = 'key'
    pos = 0
    new_pos, key = parse_key(src, pos)
    assert new_pos == len(src)
    assert key == ('key',)
