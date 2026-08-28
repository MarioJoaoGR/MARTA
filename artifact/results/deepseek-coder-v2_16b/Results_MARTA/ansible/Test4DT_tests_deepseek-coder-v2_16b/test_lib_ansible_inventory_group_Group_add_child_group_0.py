
import pytest
from ansible.inventory.group import Group

# Test adding a valid child group to another group
def test_valid_input():
    parent_group = Group('parent')
    child_group = Group('child')
    assert parent_group.add_child_group(child_group) is True
    assert child_group in parent_group.child_groups
    assert len(parent_group.child_groups) == 1
    assert child_group.depth == parent_group.depth + 1

# Test adding the same group as a child, expecting an exception
def test_edge_case():
    same_group = Group('same')
    with pytest.raises(Exception) as e:
        same_group.add_child_group(same_group)
    assert str(e.value) == "can't add group to itself"
    assert len(same_group.child_groups) == 0

# Test adding a group to itself, expecting an exception
def test_invalid_input():
    self_referential_group = Group('self_ref')
    with pytest.raises(Exception) as e:
        self_referential_group.add_child_group(self_referential_group)
    assert str(e.value) == "can't add group to itself"
    assert len(self_referential_group.child_groups) == 0
