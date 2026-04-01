
import pytest
from isort._vendored.tomli._parser import parse_inline_table, suffixed_err
from typing import Tuple, Callable

# Assuming Pos and ParseFloat are defined elsewhere in the module or imported from appropriate libraries
Pos = int
ParseFloat = Callable[[str], float]

def test_valid_input():
    src = "{key1= 'value1', key2= 3.14}"
    pos = 0
    parse_float = float
    
    result = parse_inline_table(src, pos, parse_float)
    
    assert isinstance(result[1], dict), "The parsed result should be a dictionary"
    assert result[1] == {'key1': 'value1', 'key2': 3.14}, "The parsed dictionary does not match the expected output"
