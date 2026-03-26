
import pytest
from isort._vendored.tomli._parser import parse_inline_table, Pos, ParseFloat, suffixed_err

def test_valid_input():
    src = "{key1= 'value1', key2= 3.14}"
    pos = 0
    parse_float = float
    
    result = parse_inline_table(src, pos, parse_float)
    
    assert isinstance(result[1], dict)
    assert result[1] == {'key1': 'value1', 'key2': 3.14}
