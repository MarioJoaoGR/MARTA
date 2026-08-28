
import pytest
from ansible.playbook.role.definition import RoleDefinition
from ansible.errors import AnsibleError

def test_valid_inputs():
    my_var_mgr = None  # Placeholder for variable manager
    my_loader = None   # Placeholder for loader
    role_def = RoleDefinition(play='example_play', role_basedir='/path/to/roles', variable_manager=my_var_mgr, loader=my_loader, collection_list=['collection1', 'collection2'])
    data = {'role': 'example_role', 'vars': {'key': 'value'}}
    with pytest.raises(AnsibleError):
        role_def.load(data)
