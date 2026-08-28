
import pytest
from pymonet.semigroups import All

def test_edge_case_none():
    with pytest.raises(TypeError):
        all_instance = All()
