
import pytest
from typing import Tuple, Any, Optional
from isort._vendored.tomli._parser import parse_value, Pos, ParseFloat

@pytest.mark.parametrize("src", ["'hello world'"])
def test_valid_literal_string(src: str):
    pos = 0
    parse_float = float
    new_pos, parsed_value = parse_value(src, pos, parse_float)
    assert parsed_value == "hello world"
    assert new_pos == len(src)
