
import pytest
from pymonet.immutable_list import ImmutableList

def test_edge_cases():
    # Test None as head value
    with pytest.raises(TypeError):
        empty_list = ImmutableList()
        empty_list.map(lambda x: x + 1)
