
import pytest
from ansible.playbook.role.definition import RoleDefinition

# Test valid inputs
def test_valid_inputs():
    my_var_mgr = "variable_manager"
    my_loader = "loader"
    role_def = RoleDefinition(play='example_play', role_basedir='/path/to/roles', variable_manager=my_var_mgr, loader=my_loader, collection_list=['collection1', 'collection2'])
    
    assert role_def._play == 'example_play'
    assert role_def._role_basedir == '/path/to/roles'
    assert role_def._variable_manager == my_var_mgr
    assert role_def._loader == my_loader
    assert role_def._collection_list == ['collection1', 'collection2']

# Test edge cases with None and empty values
def test_edge_cases():
    role_def = RoleDefinition(play=None, role_basedir='', variable_manager=None, loader=None, collection_list=[])
    
    assert role_def._play is None
    assert role_def._role_basedir == ''
    assert role_def._variable_manager is None
    assert role_def._loader is None
    assert role_def._collection_list == []

# Test invalid inputs and error handling
def test_invalid_inputs():
    with pytest.raises(Exception) as e:
        RoleDefinition(play='example_play', role_basedir='/path/to/roles', variable_manager=None, loader=None, collection_list=['collection1', 'collection2'])
    
    assert str(e.value) == "variable_manager is required"
