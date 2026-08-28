
import pytest
from ansible.vars.manager import HostVars

def groups_plugins_inventory():
    ''' gets plugin sources from inventory for groups '''
    return _plugins_inventory(host_groups)

# Test cases

@pytest.mark.parametrize("host_groups", [['group1', 'group2']])
def test_valid_input(host_groups):
    # Arrange
    expected_output = {'plugin1': ['source1'], 'plugin2': ['source2']}  # Example expected output
    
    # Act
    result = groups_plugins_inventory()
    
    # Assert
    assert result == expected_output

def test_missing_host_groups():
    # Arrange
    with pytest.raises(TypeError):
        # Act and Assert
        groups_plugins_inventory()

@pytest.mark.parametrize("host_groups", [None])
def test_invalid_input(host_groups):
    # Arrange
    expected_output = {}  # Example expected output for invalid input
    
    # Act
    result = groups_plugins_inventory()
    
    # Assert
    assert result == expected_output
