
import pytest
from ansible.playbook.task import Task

def test_valid_input_with_complete_block():
    block = {'action': 'shell', 'args': {'cmd': 'echo hello'}}
    task = Task(block=block)
    assert task._action == 'shell'
    assert task._args['cmd'] == 'echo hello'

def test_edge_case_with_none_input():
    task = Task(block=None)
    assert task._action is None
    assert task._args == {}

def test_invalid_input_raises_error():
    block = {'action': 'unknown_module', 'args': {'cmd': 'echo hello'}}
    with pytest.raises(ValueError):
        Task(block=block)
