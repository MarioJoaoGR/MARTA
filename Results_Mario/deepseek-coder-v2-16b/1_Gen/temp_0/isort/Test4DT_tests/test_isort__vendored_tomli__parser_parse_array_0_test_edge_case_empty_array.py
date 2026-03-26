
from isort._vendored.tomli._parser import parse_array, Pos, ParseFloat
from typing import Tuple

def test_edge_case_empty_array():
    src = "[]"
    pos = 0
    parse_float = float
    
    final_pos, parsed_array = parse_array(src, pos, parse_float)
    
    assert parsed_array == []
    assert final_pos == 2
