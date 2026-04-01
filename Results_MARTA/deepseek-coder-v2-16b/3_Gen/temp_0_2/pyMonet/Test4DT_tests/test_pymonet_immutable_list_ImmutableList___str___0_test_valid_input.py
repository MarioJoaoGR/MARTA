
import pytest
from pymonet.immutable_list import ImmutableList

def test_valid_input():
    # Setup
    immutable_list = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3, is_empty=False)))
    
    # Expected output from to_list method
    expected_output = [1, 2, 3]
    
    # Actual output from the instance
    actual_output = immutable_list.to_list()
    
    # Assert that the actual output matches the expected output
    assert actual_output == expected_output
