
import pytest
from typesystem.base import Position

def test_edge_cases():
    with pytest.raises(TypeError):
        pos = Position()
