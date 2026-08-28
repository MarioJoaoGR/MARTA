
import pytest
from pymonet.immutable_list import ImmutableList

# Test valid input scenario
def test_valid_input():
    sub_list = ImmutableList(head=2, tail=ImmutableList(head=3))
    immutable_list = ImmutableList(head=1, tail=sub_list)
    
    result = immutable_list.find(lambda x: x > 2)
    assert result == 3

# Test None input scenario
def test_none_input():
    empty_list = ImmutableList()
    
    result = empty_list.find(lambda x: x > 2)
    assert result is None

# Test invalid lambda function scenario
def test_invalid_input():
    immutable_list = ImmutableList(head=1, tail=ImmutableList(head=2, tail=ImmutableList(head=3)))
    
    with pytest.raises(TypeError):  # Assuming the error type based on the documentation
        result = immutable_list.find("invalid lambda")
