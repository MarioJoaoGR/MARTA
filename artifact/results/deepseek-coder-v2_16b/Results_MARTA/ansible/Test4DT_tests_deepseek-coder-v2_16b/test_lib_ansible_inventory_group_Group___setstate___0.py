
import pytest
from ansible.inventory.group import Group

# Test for valid input scenario
def test_valid_input():
    group = Group("validGroupName")
    assert group.name == "validGroupName"
    assert group.depth == 0
    assert group.hosts == []
    assert group.vars == {}
    assert group.child_groups == []
    assert group.parent_groups == []
    assert group.priority == 1

# Test for edge case scenario with None and empty string
def test_edge_case():
    # Test with None as name
    group_none = Group(name=None)
    assert group_none.name is None
    
    # Test with empty string as name
    group_empty = Group("")
    assert group_empty.name == ""

# Test for invalid input scenario that should raise exceptions
def test_invalid_input():
    with pytest.raises(TypeError):
        Group(123)  # Passing an integer instead of a string
