
import pytest

from isort._vendored.tomli._parser import ParseFloat, Pos, parse_value


@pytest.mark.parametrize("src", [None])
def test_edge_case_none(src):
    with pytest.raises(TypeError):
        parse_value(src, Pos(0), float)
