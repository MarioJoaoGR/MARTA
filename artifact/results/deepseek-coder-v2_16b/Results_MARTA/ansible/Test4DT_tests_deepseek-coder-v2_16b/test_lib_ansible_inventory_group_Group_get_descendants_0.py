
import pytest
from ansible.inventory.group import Group

# Test for valid case scenario
def test_valid_case():
    group = Group("test_group")
    assert group.name == "test_group"
    assert group.hosts == []
    assert group.vars == {}
    assert group.child_groups == []
    assert group.parent_groups == []
    assert group.priority == 1

# Test for edge case scenario with None input
def test_edge_case_none():
    group = Group(name=None)
    assert group.name is None
    assert group.hosts == []
    assert group.vars == {}
    assert group.child_groups == []
    assert group.parent_groups == []
    assert group.priority == 1

# Test for invalid input scenario with invalid arguments
def test_invalid_input():
    with pytest.raises(TypeError):
        Group("test_group", extra_arg="extra_value")
