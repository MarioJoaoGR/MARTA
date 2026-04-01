
from isort._vendored.tomli._parser import parse_array, skip_comments_and_array_ws, parse_value
from typing import Tuple

def test_valid_case_simple_array():
    src = "[1, 2, 3]"
    pos = 0
    parse_float = float
    
    result = parse_array(src, pos, parse_float)
    
    assert isinstance(result[1], list), "The result should be a list"
    assert result[1] == [1, 2, 3], "The parsed array should match the input array"
    assert result[0] == len(src), "The position should point to the end of the array"
