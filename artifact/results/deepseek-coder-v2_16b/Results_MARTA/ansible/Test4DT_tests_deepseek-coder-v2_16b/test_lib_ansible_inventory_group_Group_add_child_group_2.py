
import pytest
from ansible.inventory.group import Group

# Test adding a valid child group to another group
def test_valid_input():
    parent = Group("parent")
    child = Group("child")
    assert parent.add_child_group(child) is True
    assert child in parent.child_groups
    assert len(parent.child_groups) == 1
    assert parent.depth == 1
    assert child.depth == 1

# Test adding a group to itself, which should raise an exception
def test_edge_case():
    g = Group("same")
    with pytest.raises(Exception) as e:
        g.add_child_group(g)
    assert str(e.value) == "can't add group to itself"
    assert len(g.child_groups) == 0

# Test adding a None type as a child group, which should raise an exception
def test_invalid_input():
    parent = Group("parent")
    with pytest.raises(Exception) as e:
        parent.add_child_group(None)
    assert str(e.value) == "can't add group to itself"
    assert len(parent.child_groups) == 0
