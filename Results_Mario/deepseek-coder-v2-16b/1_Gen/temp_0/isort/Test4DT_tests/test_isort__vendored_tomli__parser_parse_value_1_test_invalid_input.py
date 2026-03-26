
import pytest
from isort._vendored.tomli._parser import parse_value, Pos, ParseFloat
from typing import Tuple, Any, Optional

def test_invalid_input():
    src = "invalid input"
    pos = 0
    parse_float = float
    
    with pytest.raises(ValueError):
        parse_value(src, pos, parse_float)
