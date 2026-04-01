
import pytest
from isort._vendored.tomli._parser import parse_array
from isort._vendored.tomli._parser import Pos
from isort._vendored.tomli._parser import ParseFloat
from typing import Tuple

def test_invalid_input():
    src = "["  # Incomplete array
    pos = 0
    parse_float = lambda x: float(x) if '.' in x or 'e' in x else int(x)
    
    with pytest.raises(Exception):
        parse_array(src, pos, parse_float)
