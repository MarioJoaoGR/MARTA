
from isort._vendored.tomli._parser import parse_value
from isort._vendored.tomli._parser import Pos
from isort._vendored.tomli._parser import ParseFloat
import pytest
from typing import Tuple, Any, Optional

@pytest.mark.parametrize("src, pos, expected", [
    ('"Hello world"', 0, "Hello world"),
    ("'hello world'", 0, "hello world"),
    ("true", 0, True),
    # Add more test cases for other types as needed
])
def test_valid_literal_string(src: str, pos: int, expected: Any):
    parse_float = float  # Assuming a default implementation for parse_float
    new_pos, parsed_value = parse_value(src, Pos(pos), parse_float)
    assert new_pos == len(src)
    assert parsed_value == expected
