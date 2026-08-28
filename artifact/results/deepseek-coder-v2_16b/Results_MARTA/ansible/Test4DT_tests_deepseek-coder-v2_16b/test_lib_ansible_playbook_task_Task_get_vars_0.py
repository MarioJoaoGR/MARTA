
import pytest
from ansible.playbook.task import Task

# Test valid inputs for get_vars method
def test_valid_inputs():
    task = Task(block={'action': 'shell', 'args': {'cmd': 'echo hello'}})
    vars_dict = task.get_vars()
    assert isinstance(vars_dict, dict)
    assert 'tags' not in vars_dict
    assert 'when' not in vars_dict
    assert 'action' in vars_dict
    assert vars_dict['action'] == 'shell'
    assert 'cmd' in vars_dict['args']
    assert vars_dict['args']['cmd'] == 'echo hello'

# Test edge cases for get_vars method
def test_edge_cases():
    task = Task()
    vars_dict = task.get_vars()
    assert isinstance(vars_dict, dict)
    assert 'tags' not in vars_dict
    assert 'when' not in vars_dict
    # No additional assertions needed as the method should handle empty or minimal input gracefully

# Test raising exceptions for invalid inputs
def test_invalid_inputs():
    with pytest.raises(TypeError):
        task = Task(block=None)  # None is an invalid type for block parameter
