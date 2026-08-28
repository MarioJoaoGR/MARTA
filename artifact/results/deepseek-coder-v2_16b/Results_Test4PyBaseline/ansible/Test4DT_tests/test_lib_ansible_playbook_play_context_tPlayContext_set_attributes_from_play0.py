
import pytest
from ansible.playbook.play_context import PlayContext

@pytest.fixture
def default_context():
    return PlayContext(play={}, passwords={})

@pytest.fixture
def full_config_context():
    play = {
        'force_handlers': True,
        'pipelining': False,
        'remote_addr': '192.168.1.100',
        'remote_user': 'admin'
    }
    passwords = {
        'conn_pass': 'password123',
        'become_pass': 'root'
    }
    return PlayContext(play=play, passwords=passwords)

def test_default_context_initialization():
    play = {}
    passwords = {}
    context = PlayContext(play=play, passwords=passwords)
    assert not hasattr(context, 'force_handlers'), "Expected force_handlers to be set from the default value"
    assert context.password == '', "Expected password to be an empty string by default"
    assert context.become_pass == '', "Expected become_pass to be an empty string by default"

def test_full_config_context_initialization():
    play = {
        'force_handlers': True,
        'pipelining': False,
        'remote_addr': '192.168.1.100',
        'remote_user': 'admin'
    }
    passwords = {
        'conn_pass': 'password123',
        'become_pass': 'root'
    }
    context = PlayContext(play=play, passwords=passwords)
    assert context.force_handlers is True, "Expected force_handlers to be set from the play configuration"
    assert context.password == 'password123', "Expected password to be overridden by the play configuration"
    assert context.become_pass == 'root', "Expected become_pass to be overridden by the play configuration"

def test_set_attributes_from_cli(default_context):
    default_context.set_attributes_from_cli()
    assert not hasattr(default_context, 'force_handlers'), "Expected force_handlers to be set from the CLI arguments"

def test_set_attributes_from_play(full_config_context):
    play = {'force_handlers': True}
    full_config_context.set_attributes_from_play(play)
    assert full_config_context.force_handlers is True, "Expected force_handlers to be set from the play configuration"

def test_set_attributes_from_play_override(default_context):
    play = {'force_handlers': False}
    default_context.set_attributes_from_play(play)
    assert not hasattr(default_context, 'force_handlers'), "Expected force_handlers to be set from the play configuration"
