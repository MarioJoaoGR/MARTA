
import pytest
from ansible.playbook.role.definition import RoleDefinition
from ansible.errors import AnsibleError


def test_get_role_params():
    role_def = RoleDefinition(play="example_play", role_basedir="/path/to/roles", variable_manager=None, loader=None, collection_list=["collection1", "collection2"])
    data = {
        'role': 'example_role',
        'vars': {'key': 'value'}
    }
    with pytest.raises(AnsibleError):
        role_def.load(data)