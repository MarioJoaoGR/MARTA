
from isort._vendored.tomli._parser import skip_chars, Pos
from typing import Iterable

def test_invalid_pos():
    # Test when pos is out of range
    src = "hello world"
    chars = ["l", "o"]
    pos = len(src) + 1  # Out of range position
    result = skip_chars(src, pos, chars)
    assert result == pos  # Should not change the position since it's out of range
