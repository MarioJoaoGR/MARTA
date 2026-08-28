
import pytest
from ansible.playbook.play import Play
from ansible.errors import AnsibleError

def test_valid_input():
    play_config = {
        'hosts': ['localhost'],
        'roles': ['role1', 'role2']
    }
    with pytest.raises(AnsibleError):
        play = Play.load(play_config)
