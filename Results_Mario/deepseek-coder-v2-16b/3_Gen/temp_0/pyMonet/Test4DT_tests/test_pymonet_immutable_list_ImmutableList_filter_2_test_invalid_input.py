
import pytest
from pymonet.immutable_list import ImmutableList

def test_invalid_input():
    empty_list = ImmutableList()
    
    # Test with None as the filter function
    with pytest.raises(TypeError):
        filtered_list = empty_list.filter(None)
