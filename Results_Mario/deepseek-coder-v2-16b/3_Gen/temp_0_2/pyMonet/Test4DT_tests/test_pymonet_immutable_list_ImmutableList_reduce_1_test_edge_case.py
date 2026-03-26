
import pytest
from pymonet.immutable_list import ImmutableList

def test_edge_case():
    # Create an empty ImmutableList instance
    empty_list = ImmutableList()
    
    # Define a reducer function that adds the values together
    def add_to_acc(acc, val):
        return acc + val
    
    # Test the reduce method with an initial accumulator value of 0
    assert empty_list.reduce(add_to_acc, 0) == 0
