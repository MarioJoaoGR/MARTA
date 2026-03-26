
import pytest
from isort._vendored.tomli._parser import parse_value, Pos

def test_invalid_input_error_handling():
    src = 'InvalidInput'
    pos = 0
    
    with pytest.raises(ValueError) as exc_info:
        parse_value(src, Pos(pos), float)
    
    assert str(exc_info.value) == "Invalid value (at line 1, column 1)"
