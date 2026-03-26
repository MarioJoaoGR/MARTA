
import pytest
from typing import Tuple
from isort._vendored.tomli._parser import Pos, parse_one_line_basic_str

def test_invalid_input():
    src = "hello world'"
    pos = Pos(0)
    
    with pytest.raises(ValueError):
        parse_one_line_basic_str(src, pos)
