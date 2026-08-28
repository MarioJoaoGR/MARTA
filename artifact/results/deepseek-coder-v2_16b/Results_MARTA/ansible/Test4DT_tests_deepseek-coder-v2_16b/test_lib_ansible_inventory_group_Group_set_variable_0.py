
import pytest
from ansible.inventory.group import Group

# Test setting priority with valid input
def test_valid_input_set_priority():
    group = Group(name="test_group")
    group.set_variable('ansible_group_priority', 2)
    assert group.priority == 2

# Test setting priority with invalid input (non-integer)
def test_invalid_input_set_priority():
    group = Group(name="test_group")
    with pytest.raises(ValueError):
        group.set_variable('ansible_group_priority', 'invalid')
    assert group.priority == 1  # Default priority should remain unchanged

# Test setting variable with invalid input (non-string key)
def test_invalid_input_set_variable():
    group = Group(name="test_group")
    with pytest.raises(TypeError):
        group.set_variable(42, 'valid_value')  # Non-string key should raise TypeError
    assert 'valid_value' not in group.vars
