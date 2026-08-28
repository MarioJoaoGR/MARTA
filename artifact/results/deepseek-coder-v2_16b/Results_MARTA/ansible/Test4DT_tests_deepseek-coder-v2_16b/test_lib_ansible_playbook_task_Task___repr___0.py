
import pytest
from ansible.playbook.task import Task

# Test valid inputs - happy path
def test_valid_inputs_happy_path():
    task = Task(block={'action': 'shell', 'args': {'cmd': 'echo hello'}}, role='example_role')
    assert task._role == 'example_role'
    assert task.resolved_action == 'shell'
    assert task._args['args']['cmd'] == 'echo hello'

# Test edge cases
def test_edge_cases():
    # None input
    with pytest.raises(TypeError):
        Task(block=None)
    
    # Empty list input
    with pytest.raises(TypeError):
        Task(block={})
    
    # No parameters
    task = Task()
    assert task._role is None
    assert task.resolved_action is None
    assert task._args == {}

# Test invalid inputs - error handling
def test_invalid_inputs_error_handling():
    with pytest.raises(TypeError):
        Task(block='invalid input')
    
    with pytest.raises(TypeError):
        Task(role=123)
    
    with pytest.raises(TypeError):
        Task(task_include='invalid input')
