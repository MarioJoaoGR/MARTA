
import pytest
from your_module import InventoryData  # Replace 'your_module' with the actual module name where InventoryData is defined

@pytest.fixture(scope="function")
def inventory():
    return InventoryData()

# Test for standard input for get_groups_dict method
def test_valid_input_get_groups_dict(inventory):
    # Add some groups and hosts to simulate a valid scenario
    group1 = type('Group', (object,), {'name': 'group1', 'get_hosts': lambda: []})()
    host1 = type('Host', (object,), {'name': 'host1', 'group_names': set(['group1'])})()
    inventory.groups['group1'] = group1
    inventory.hosts['host1'] = host1
    
    # Call the method under test
    groups_dict = inventory.get_groups_dict()
    
    # Assert that the result is a dictionary and contains the expected keys and values
    assert isinstance(groups_dict, dict)
    assert 'group1' in groups_dict
    assert len(groups_dict['group1']) == 1
    assert groups_dict['group1'][0] == 'host1'

# Test for edge case with empty inventory
def test_edge_case_empty_inventory(inventory):
    # Call the method under test
    groups_dict = inventory.get_groups_dict()
    
    # Assert that the result is a dictionary and should be empty since there are no groups or hosts
    assert isinstance(groups_dict, dict)
    assert not groups_dict  # Should be an empty dictionary

# Test for invalid input for get_groups_dict method, expecting error handling
def test_invalid_input_get_groups_dict(inventory):
    # Ensure there are no groups or hosts added to simulate an invalid scenario
    
    with pytest.raises(TypeError):  # Assuming the method raises a TypeError if called incorrectly
        inventory.get_groups_dict()  # Call the method under test within the context of the exception
