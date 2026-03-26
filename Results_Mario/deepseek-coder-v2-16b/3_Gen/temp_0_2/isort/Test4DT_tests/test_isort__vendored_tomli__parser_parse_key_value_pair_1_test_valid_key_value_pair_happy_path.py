
import pytest
from isort._vendored.tomli._parser import parse_key_value_pair, suffixed_err
from typing import Tuple, Any, Optional

@pytest.mark.parametrize("src", ["key=42", '"hello"=42', '"pi"=3.14'])
def test_valid_key_value_pair_happy_path(src):
    pos = 0
    parse_float = float
    new_pos, key, value = parse_key_value_pair(src, pos, parse_float)
    
    assert new_pos == len(src)
    assert isinstance(key, tuple) and all(isinstance(k, str) for k in key)
    if src.startswith('key='):
        assert key == ('key',)
        assert value == 42
    elif src.startswith('"hello"'):
        assert key == ('hello',)
        assert value == 42
    elif src.startswith('"pi"'):
        assert key == ('pi',)
        assert value == 3.14
