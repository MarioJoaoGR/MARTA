
import pytest
from ansible.playbook.play_context import PlayContext

@pytest.fixture
def default_play_context():
    return PlayContext()

@pytest.fixture
def play_context_with_passwords():
    return PlayContext(play={'force_handlers': True}, passwords={'conn_pass': 'password123', 'become_pass': 'root'})

def test_default_init(default_play_context):
    assert default_play_context.password == ''
    assert default_play_context.become_pass == ''