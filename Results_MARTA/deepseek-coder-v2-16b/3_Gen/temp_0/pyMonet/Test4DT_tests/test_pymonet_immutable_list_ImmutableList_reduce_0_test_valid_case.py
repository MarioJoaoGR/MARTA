
import pytest
from pymonet.immutable_list import ImmutableList

def test_valid_case():
    lst = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3, is_empty=False)))
    
    def add(x, y):
        return x + y
    
    result = lst.reduce(add, 0)
    assert result == 6
