
import pytest
from pymonet.immutable_list import ImmutableList

def test_invalid_input():
    empty_list = ImmutableList()
    
    with pytest.raises(TypeError):
        empty_list.filter(lambda x: x > 1)
