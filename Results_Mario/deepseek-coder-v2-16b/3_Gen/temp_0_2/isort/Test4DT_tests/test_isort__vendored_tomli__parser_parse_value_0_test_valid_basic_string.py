
from isort._vendored.tomli._parser import parse_value, Pos, ParseFloat
from typing import Tuple, Any, Optional
import pytest

@pytest.mark.parametrize("src, pos, expected", [
    ('"Hello world"', 0, "Hello world"),
    ("'hello world'", 0, "hello world"),
    ("true", 0, True),
    # Add more test cases for other types like datetime, integers, floats, arrays, etc.
])
def test_valid_basic_string(src: str, pos: int, expected: Any):
    parse_float = float  # Example implementation of ParseFloat
    new_pos, parsed_value = parse_value(src, Pos(pos), parse_float)
    assert parsed_value == expected
    assert new_pos == len(src)
