
import pytest
from isort._vendored.tomli._parser import parse_value, Pos, ParseFloat

@pytest.mark.parametrize("src", [None])
def test_edge_case_none(src):
    with pytest.raises(TypeError):
        parse_value(src, Pos(0), float)
