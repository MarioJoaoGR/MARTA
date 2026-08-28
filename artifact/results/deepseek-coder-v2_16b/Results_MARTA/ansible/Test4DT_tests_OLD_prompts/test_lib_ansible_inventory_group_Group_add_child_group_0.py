
import pytest
from ansible.inventory.group import Group
from unittest.mock import patch, MagicMock

# Test adding a child group recursively in a loop
def test_add_child_group_recursive_loop():
    with pytest.raises(Exception) as excinfo:
        group = Group('test_group')
        group.add_child_group(group)  # Attempt to add the same group to itself
    assert str(excinfo.value) == "can't add group to itself"
