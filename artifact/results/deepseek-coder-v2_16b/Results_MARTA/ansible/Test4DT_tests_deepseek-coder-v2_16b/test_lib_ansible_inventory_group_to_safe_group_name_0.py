
import pytest
from ansible.inventory.group import Group

# Test valid input scenario
def test_valid_input():
    group = Group(name="my-group_name")
    result = to_safe_group_name(group.name)
    assert result == "my_group_name"

# Test edge case with None as input
def test_edge_case():
    result = to_safe_group_name(None)
    assert result is None

# Test invalid input and error handling scenario
def test_invalid_input():
    group = Group(name="my-group!name")
    with pytest.raises(TypeError):
        to_safe_group_name(group.name, force=True)
