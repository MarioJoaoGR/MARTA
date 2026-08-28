
import pytest
from ansible.cli.scripts.ansible_connection_cli_stub import ConnectionProcess, JsonRpcServer

@pytest.fixture
def setup_connection_process():
    fd = 123
    play_context = {'host': 'example.com', 'private_key_file': None}
    socket_path = 'unix:/tmp/ansible.sock'
    original_path = '/path/to/playbook'
    task_uuid = None
    ansible_playbook_pid = None
    return ConnectionProcess(fd, play_context, socket_path, original_path, task_uuid, ansible_playbook_pid)

def test_connection_process_initialization(setup_connection_process):
    cp = setup_connection_process
    
    assert cp.fd == 123
    assert cp.play_context == {'host': 'example.com', 'private_key_file': None}
    assert cp.socket_path == 'unix:/tmp/ansible.sock'
    assert cp.original_path == '/path/to/playbook'
    assert cp._task_uuid is None
    assert cp._ansible_playbook_pid is None
    assert isinstance(cp.srv, JsonRpcServer)
    assert cp.sock is None