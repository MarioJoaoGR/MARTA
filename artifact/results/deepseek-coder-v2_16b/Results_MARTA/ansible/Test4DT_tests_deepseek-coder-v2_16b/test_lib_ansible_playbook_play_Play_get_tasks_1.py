
import pytest
from ansible.playbook.play import Play
from ansible.errors import AnsibleError



def test_invalid_inputs():
    datastructure = {
        'roles': ['role1', 'role2']
    }
    with pytest.raises(AnsibleError):
        Play.load(datastructure)