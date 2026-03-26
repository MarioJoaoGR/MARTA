
from isort._vendored.tomli._parser import parse_one_line_basic_str, Pos
import pytest

def test_none_input():
    with pytest.raises(TypeError):
        pos, parsed_str = parse_one_line_basic_str(None, Pos(0))
