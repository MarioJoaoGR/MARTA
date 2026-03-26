
import pytest
from isort._vendored.tomli._parser import parse_value, Pos, ParseFloat

def test_invalid_input():
    src = 'InvalidInput'
    pos = 0
    with pytest.raises(ValueError):
        parse_value(src, Pos(pos), float)
