
import pytest
from pymonet.immutable_list import ImmutableList  # Assuming the module name is pymonet.immutable_list

def test_valid_input():
    lst = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3, is_empty=False)))
    
    def add(acc, x): return acc + x
    
    assert lst.reduce(add, 0) == 6  # Expected output: 6 (1 + 2 + 3)
