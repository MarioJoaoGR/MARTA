
import pytest

from isort._vendored.tomli._parser import Pos, parse_basic_str_escape


def test_edge_case_none():
    src = None
    pos = Pos(0)
    
    with pytest.raises(TypeError):
        parse_basic_str_escape(src, pos)
