
import pytest
from typing import Tuple, Any, Optional
from isort._vendored.tomli._parser import parse_key_value_pair, Pos, ParseFloat, skip_chars, TOML_WS

def test_none_input():
    src = None
    pos = 0
    parse_float = float
    
    with pytest.raises(TypeError):
        parse_key_value_pair(src, pos, parse_float)
