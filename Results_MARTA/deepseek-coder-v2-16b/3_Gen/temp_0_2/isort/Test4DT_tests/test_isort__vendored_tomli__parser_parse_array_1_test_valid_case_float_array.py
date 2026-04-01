
from isort._vendored.tomli._parser import parse_array, Pos, ParseFloat
from typing import Tuple

def test_valid_case_float_array():
    src = "[1.1, 2.2, 3.3]"
    pos = 0
    parse_float = float
    
    result = parse_array(src, pos, parse_float)
    
    assert isinstance(result[1], list), "Result should be a list"
    assert all(isinstance(item, float) for item in result[1]), "All items in the list should be floats"
    assert result[0] == len(src), "Position should point to the end of the array"
