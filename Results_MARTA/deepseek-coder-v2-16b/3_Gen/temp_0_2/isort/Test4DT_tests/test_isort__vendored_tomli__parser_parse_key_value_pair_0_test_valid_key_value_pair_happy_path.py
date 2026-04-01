
import pytest
from isort._vendored.tomli._parser import parse_key_value_pair, suffixed_err
from typing import Tuple, Any, Optional

@pytest.mark.parametrize("src, expected_pos, expected_key, expected_value", [
    ("key=42", len("key=42"), ("key",), 42),
    ('"hello"=42', len('"hello"=42'), ('hello',), 42),
    ('"pi"=3.14', len('"pi"=3.14'), ('pi',), 3.14)
])
def test_valid_key_value_pair_happy_path(src, expected_pos, expected_key, expected_value):
    pos = 0
    parse_float = float
    new_pos, key, value = parse_key_value_pair(src, pos, parse_float)
    assert new_pos == expected_pos
    assert key == expected_key
    assert value == expected_value
