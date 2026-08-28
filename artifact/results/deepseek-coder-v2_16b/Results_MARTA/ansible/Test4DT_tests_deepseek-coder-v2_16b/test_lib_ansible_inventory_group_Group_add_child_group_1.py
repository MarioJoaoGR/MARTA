
import pytest
from ansible.inventory.group import Group

# Test adding a valid child group to the current group
def test_valid_input_add_child_group():
    parent = Group("parent")
    child = Group("child")
    assert len(parent.child_groups) == 0
    parent.add_child_group(child)
    assert len(parent.child_groups) == 1
    assert child in parent.child_groups

# Test adding None as a child group, should raise Exception
def test_edge_case_none_as_child():
    parent = Group("parent")
    with pytest.raises(Exception):
        parent.add_child_group(None)

# Test adding the same group as a child, should raise Exception
def test_invalid_input_recursive_add():
    group = Group("same")
    with pytest.raises(Exception):
        group.add_child_group(group)
