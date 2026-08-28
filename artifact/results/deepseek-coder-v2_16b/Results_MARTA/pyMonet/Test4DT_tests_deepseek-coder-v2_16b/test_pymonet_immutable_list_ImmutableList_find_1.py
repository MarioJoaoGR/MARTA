
import pytest
from pymonet.immutable_list import ImmutableList

# Scenario 1: Test valid input where the function should return a valid element from the list.
def test_valid_input():
    sub_list = ImmutableList(head=2, tail=ImmutableList(head=3))
    immutable_list = ImmutableList(head=1, tail=sub_list)
    
    result = immutable_list.find(lambda x: x > 2)
    assert result == 3

# Scenario 2: Test when the list is empty and should return None.
def test_none_input():
    empty_list = ImmutableList(is_empty=True)
    
    result = empty_list.find(lambda x: True)
    assert result is None

# Scenario 3: Test with an invalid function that raises TypeError to check error handling.
def test_invalid_input():
    immutable_list = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3)))
    
    with pytest.raises(TypeError):
        immutable_list.find("not a function")
