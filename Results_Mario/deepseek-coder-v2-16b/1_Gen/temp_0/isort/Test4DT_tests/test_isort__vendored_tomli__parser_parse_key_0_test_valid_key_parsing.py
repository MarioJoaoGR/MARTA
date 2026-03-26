
import pytest
from isort._vendored.tomli._parser import parse_key, Pos, Key

def test_valid_key_parsing():
    src = 'example.key1.key2'
    pos = 0
    new_pos, key = parse_key(src, pos)
    assert new_pos == len(src)
    assert key == ('example', 'key1', 'key2')
