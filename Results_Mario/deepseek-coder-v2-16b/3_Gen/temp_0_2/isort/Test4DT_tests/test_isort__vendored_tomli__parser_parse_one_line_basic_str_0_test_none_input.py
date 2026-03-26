
import pytest
from typing import Tuple, Optional
from isort._vendored.tomli._parser import parse_one_line_basic_str, Pos

def test_none_input():
    src = None
    pos = 0
    
    with pytest.raises(TypeError):
        new_pos, parsed_str = parse_one_line_basic_str(src, pos)
