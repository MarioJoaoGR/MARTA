
import pytest
from ansible.playbook.task import Task

# Test valid inputs scenario
def test_valid_inputs():
    task = Task(block={'action': 'shell', 'args': {'cmd': 'echo hello'}}, role='example_role')
    assert task.get_name() == "example_role : shell"

# Test edge cases scenario
def test_edge_cases():
    # None input
    task = Task(block=None, role=None)
    with pytest.raises(AttributeError):
        task.get_name()
    
    # Empty list input
    task = Task(block={}, role='')
    assert task.get_name() == "shell"

# Test invalid inputs scenario
def test_invalid_inputs():
    task = Task(block=None, role='invalid_role')
    with pytest.raises(AttributeError):
        task.get_name()
