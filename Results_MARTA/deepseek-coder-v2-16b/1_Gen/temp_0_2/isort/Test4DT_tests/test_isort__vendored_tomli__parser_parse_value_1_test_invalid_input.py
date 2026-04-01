
import pytest
from isort._vendored.tomli._parser import parse_value, Pos

def test_invalid_input():
    with pytest.raises(ValueError):
        parse_value('invalid input', Pos(0), float)
