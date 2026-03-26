
import pytest

from isort._vendored.tomli._parser import ParseFloat, Pos, parse_value


def test_invalid_input():
    src = 'InvalidInput'
    pos = 0
    with pytest.raises(ValueError):
        parse_value(src, Pos(pos), float)
