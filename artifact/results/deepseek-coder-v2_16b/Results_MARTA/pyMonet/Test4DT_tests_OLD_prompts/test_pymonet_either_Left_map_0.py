
import pytest
from pymonet.either import Left, Right

def test_edge_case():
    with pytest.raises(TypeError):
        left_value = Left()
