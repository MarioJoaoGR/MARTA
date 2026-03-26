
import pytest
from typing import Tuple, Any
from isort._vendored.tomli._parser import parse_key_value_pair, Pos, ParseFloat

def test_edge_case_none_input():
    with pytest.raises(TypeError):
        parse_key_value_pair(None, Pos(0), float)
