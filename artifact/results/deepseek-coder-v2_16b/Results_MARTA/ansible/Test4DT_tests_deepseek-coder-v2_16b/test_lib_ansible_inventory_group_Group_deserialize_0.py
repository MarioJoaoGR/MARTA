
import pytest
from ansible.inventory.group import Group

# Scenario 1: Test standard input with valid group name and attributes
def test_valid_input_happy_path():
    # Arrange
    group = Group(name="test-group")
    
    # Act & Assert
    assert group.name == "test-group"
    assert group.depth == 0
    assert group.hosts == []
    assert group.vars == {}
    assert group.child_groups == []
    assert group.parent_groups == []
    assert group.priority == 1

# Scenario 2: Test edge case with None values for all parameters
def test_edge_case_none_values():
    # Arrange
    group = Group()
    
    # Act & Assert
    assert group.name is None
    assert group.depth == 0
    assert group.hosts == []
    assert group.vars == {}
    assert group.child_groups == []
    assert group.parent_groups == []
    assert group.priority == 1

# Scenario 3: Test invalid input and error handling
def test_invalid_input_error_handling():
    # Arrange & Act (expecting a TypeError due to non-string name)
    with pytest.raises(TypeError):
        Group(name=None)
    
    with pytest.raises(TypeError):
        Group(name=12345)
    
    with pytest.raises(TypeError):
        Group(name=-1)
