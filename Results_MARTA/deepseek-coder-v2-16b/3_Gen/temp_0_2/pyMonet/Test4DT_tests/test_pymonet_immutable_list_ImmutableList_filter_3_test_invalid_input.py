
import pytest
from pymonet.immutable_list import ImmutableList

def test_invalid_input():
    empty_list = ImmutableList()
    
    # Test with a function that always returns False
    filtered_list = empty_list.filter(lambda x: False)
    assert filtered_list.is_empty is True, f"Expected is_empty to be True, but got {filtered_list.is_empty}"
    
    # Test with a function that always returns True
    filtered_list = empty_list.filter(lambda x: True)
    assert filtered_list.is_empty is False, f"Expected is_empty to be False, but got {filtered_list.is_empty}"
