
from isort._vendored.tomli._parser import parse_array
from typing import Tuple, List, Callable

# Assuming Pos and ParseFloat are defined elsewhere in your module or imported correctly
Pos = int  # Example definition; adjust according to actual implementation
ParseFloat = Callable[[str], float]

def test_edge_case_empty_array():
    src = "[]"
    pos = 0
    parse_float = None
    
    result: Tuple[Pos, List] = parse_array(src, pos, parse_float)
    
    assert result == (2, [])
