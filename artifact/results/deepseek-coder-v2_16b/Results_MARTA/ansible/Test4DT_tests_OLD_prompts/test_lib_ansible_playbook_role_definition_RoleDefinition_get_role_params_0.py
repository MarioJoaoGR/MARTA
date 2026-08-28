
import pytest
from unittest.mock import MagicMock, patch
from ansible.playbook.role.definition import RoleDefinition



def test_get_role_params():
    my_var_mgr = MagicMock()
    my_loader = MagicMock()
    
    role_def = RoleDefinition(variable_manager=my_var_mgr, loader=my_loader)
    role_def._role_params = {'key': 'value'}
    
    params = role_def.get_role_params()
    assert isinstance(params, dict), "Expected a dictionary but got something else"
    assert len(params) == 1, "Expected one item in the dictionary but found more or less"
    assert 'key' in params, "'key' not found in returned parameters"