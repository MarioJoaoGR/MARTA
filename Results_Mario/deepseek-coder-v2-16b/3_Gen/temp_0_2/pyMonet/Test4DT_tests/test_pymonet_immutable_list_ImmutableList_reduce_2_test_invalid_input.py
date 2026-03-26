
import pytest
from pymonet.immutable_list import ImmutableList

def test_invalid_input():
    lst = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3, tail=None)))
    
    with pytest.raises(TypeError):
        lst.reduce(lambda x, y: x + y, 0)  # This should pass as the function is valid
        
        # The following line should raise TypeError because reduce is called without a callable
        lst.reduce("not_a_callable", 0)
