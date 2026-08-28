
import pytest
from pymonet.immutable_list import ImmutableList

# Test valid input
def test_valid_input():
    sub_list = ImmutableList(head=2, tail=ImmutableList(head=3))
    immutable_list = ImmutableList(head=1, tail=sub_list)
    
    result = immutable_list.find(lambda x: x > 2)
    assert result == 3

# Test None input
def test_none_input():
    immutable_list = ImmutableList()
    
    result = immutable_list.find(lambda x: x > 2)
    assert result is None

# Test invalid lambda function
def test_invalid_input():
    sub_list = ImmutableList(head=2, tail=ImmutableList(head=3))
    immutable_list = ImmutableList(head=1, tail=sub_list)
    
    with pytest.raises(TypeError):
        result = immutable_list.find("invalid lambda")
