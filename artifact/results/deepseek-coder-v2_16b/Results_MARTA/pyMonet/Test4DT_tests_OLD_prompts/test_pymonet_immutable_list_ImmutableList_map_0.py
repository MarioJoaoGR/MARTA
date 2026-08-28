
import pytest
from pymonet.immutable_list import ImmutableList

def test_map_empty():
    my_list = ImmutableList(is_empty=True)
    
    def add_one(x):
        return x + 1
    
    with pytest.raises(TypeError):
        mapped_list = my_list.map(add_one)
