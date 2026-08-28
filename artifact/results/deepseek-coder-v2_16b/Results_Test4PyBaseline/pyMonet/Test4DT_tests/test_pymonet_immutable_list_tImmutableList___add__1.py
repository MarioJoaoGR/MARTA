
import pytest
from pymonet.immutable_list import ImmutableList

# Test adding an instance of a different type than ImmutableList
def test_add_instance_of_different_type():
    immutable_list = ImmutableList(head=1)
    with pytest.raises(ValueError, match="ImmutableList: you can not add any other instace than ImmutableList"):
        combined_list = immutable_list + "not an ImmutableList"
