
import pytest
from ansible.playbook.role.definition import RoleDefinition
from ansible.errors import AnsibleError

def test_valid_inputs_happy_path():
    # Arrange
    role_def = RoleDefinition(
        play='example_play',
        role_basedir='/path/to/roles',
        variable_manager=None,
        loader=None,
        collection_list=['collection1', 'collection2']
    )
    
    # Act
    with pytest.raises(AnsibleError):
        role_def.load({'role': 'example_role', 'vars': {'key': 'value'}})

def test_edge_cases():
    # Arrange
    role_def = RoleDefinition(
        play=None,
        role_basedir='',
        variable_manager=None,
        loader=None,
        collection_list=[]
    )
    
    # Act & Assert
    with pytest.raises(AnsibleError):
        role_def.load({'role': 'example_role', 'vars': {'key': 'value'}})

def test_invalid_inputs_error_handling():
    # Arrange
    role_def = RoleDefinition(
        play='example_play',
        role_basedir='/path/to/roles',
        variable_manager=None,
        loader=None,
        collection_list=['collection1']
    )
    
    # Act & Assert
    with pytest.raises(AnsibleError):
        role_def.load({'role': 'example_role', 'vars': {'key': 'value'}})
