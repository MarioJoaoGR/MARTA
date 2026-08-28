
import pytest
from ansible.playbook.role.definition import RoleDefinition

def test_valid_initialization():
    role_def = RoleDefinition(play="example_play", role_basedir="/path/to/roles")
    assert hasattr(role_def, '_play') and role_def._play == "example_play"
    assert hasattr(role_def, '_role_basedir') and role_def._role_basedir == "/path/to/roles"

def test_initialization_with_all_parameters():
    my_var_mgr = None  # Replace with actual mock or object if necessary
    my_loader = None   # Replace with actual mock or object if necessary
    role_def = RoleDefinition(play="example_play", role_basedir="/path/to/roles", variable_manager=my_var_mgr, loader=my_loader, collection_list=["collection1", "collection2"])
    assert hasattr(role_def, '_play') and role_def._play == "example_play"
    assert hasattr(role_def, '_role_basedir') and role_def._role_basedir == "/path/to/roles"
    assert hasattr(role_def, '_variable_manager') and role_def._variable_manager is my_var_mgr
    assert hasattr(role_def, '_loader') and role_def._loader is my_loader
    assert hasattr(role_def, '_collection_list') and role_def._collection_list == ["collection1", "collection2"]

def test_get_name_with_fqcn():
    role_def = RoleDefinition(play="example_play", role_basedir="/path/to/roles")
    role_def._role_collection = "example_collection"
    role_def.role = "example_role"
    assert role_def.get_name(include_role_fqcn=True) == 'example_collection.example_role'

def test_get_name_without_fqcn():
    role_def = RoleDefinition(play="example_play", role_basedir="/path/to/roles")
    role_def._role_collection = "example_collection"
    role_def.role = "example_role"
    assert role_def.get_name(include_role_fqcn=False) == 'example_role'
