
import pytest
from pymonet.immutable_list import ImmutableList

# Test edge case where the list is empty
def test_edge_case_empty_list():
    my_list = ImmutableList(is_empty=True)
    assert my_list.is_empty is True

# Test error case where an invalid type is passed
def test_error_case_invalid_type():
    with pytest.raises(TypeError):
        ImmutableList.of()
