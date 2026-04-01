
import pytest
from pymonet.immutable_list import ImmutableList

def test_edge_case():
    # Create an empty ImmutableList instance
    empty_list = ImmutableList()
    
    # Define a reducer function that adds two numbers
    def add(x, y):
        return x + y
    
    # Test the reduce method with an empty list and the add function
    result = empty_list.reduce(add, 0)
    
    # The expected result should be the initial accumulator value (0) since the list is empty
    assert result == 0
