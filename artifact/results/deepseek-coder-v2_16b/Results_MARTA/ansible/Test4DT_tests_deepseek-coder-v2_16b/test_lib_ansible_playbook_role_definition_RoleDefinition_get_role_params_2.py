
import pytest
from ansible.playbook.role.definition import RoleDefinition

def test_get_role_params():
    role_def = RoleDefinition(play="example_play", role_basedir="/path/to/roles", variable_manager=None, loader=None, collection_list=["collection1", "collection2"])
    params = role_def.get_role_params()
    assert isinstance(params, dict), "Expected a dictionary but got something else"
    assert len(params) == 0, "Expected no parameters to be set initially"
