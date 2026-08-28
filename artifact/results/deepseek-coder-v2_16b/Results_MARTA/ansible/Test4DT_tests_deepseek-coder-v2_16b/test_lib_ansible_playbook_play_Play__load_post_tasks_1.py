
import pytest
from ansible.playbook.play import Play
from ansible.errors import AnsibleParserError

def test_load_post_tasks():
    play = Play()
    setattr(play, '_ds', None)
    
    with pytest.raises(AnsibleParserError):
        play._load_post_tasks('post_tasks', {})
