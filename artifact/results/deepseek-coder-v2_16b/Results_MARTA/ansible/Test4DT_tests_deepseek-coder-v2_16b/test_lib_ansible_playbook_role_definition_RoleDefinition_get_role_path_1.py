
import pytest
from ansible.playbook.role.definition import RoleDefinition

# Test initialization of RoleDefinition with valid inputs
def test_init_with_valid_inputs():
    role_def = RoleDefinition(play="example_play", role_basedir="/path/to/roles", variable_manager=None, loader=None, collection_list=["collection1", "collection2"])
    assert role_def._play == "example_play"
    assert role_def._role_basedir == "/path/to/roles"
    assert role_def._collection_list == ["collection1", "collection2"]

# Test get_role_path method with a pre-set _role_path
def test_get_role_path():
    role_def = RoleDefinition(play="example_play", role_basedir="/path/to/roles", variable_manager=None, loader=None, collection_list=["collection1", "collection2"])
    role_def._role_path = "/expected/role/path"
    assert role_def.get_role_path() == "/expected/role/path"

# Test get_role_path method with no pre-set _role_path (should return None)
def test_get_role_path_none():
    role_def = RoleDefinition(play="example_play", role_basedir="/path/to/roles", variable_manager=None, loader=None, collection_list=["collection1", "collection2"])
    assert role_def.get_role_path() is None
