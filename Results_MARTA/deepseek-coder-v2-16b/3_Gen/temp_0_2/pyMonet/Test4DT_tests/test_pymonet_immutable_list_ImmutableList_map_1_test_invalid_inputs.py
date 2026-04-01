
import pytest
from pymonet.immutable_list import ImmutableList

def test_invalid_inputs():
    empty_list = ImmutableList()
    
    # Test map with None as function
    with pytest.raises(TypeError):
        empty_list.map(None)
