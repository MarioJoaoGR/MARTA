
import pytest
from lib.ansible.playbook.task import Task

# Scenario 1: Test standard input with valid tasks and new block
def test_valid_case():
    task1 = Task(block={'action': 'shell', 'args': {'cmd': 'echo "Hello, World!"'}})
    task2 = Task(block={'action': 'yum', 'args': {'name': 'some_package'}})
    new_block = Task(block={'action': 'debug', 'args': {'msg': 'This is a new block'}})
    
    new_task_list = _dupe_task_list([task1, task2], new_block)
    
    assert len(new_task_list) == 3
    for task in new_task_list:
        if isinstance(task._parent, Task):
            assert task._parent != new_block
        else:
            assert task._parent == new_block

# Scenario 2: Test edge case with empty task list
def test_edge_case():
    new_block = Task(block={'action': 'debug', 'args': {'msg': 'This is a new block'}})
    
    new_task_list = _dupe_task_list([], new_block)
    
    assert len(new_task_list) == 1
    assert new_task_list[0]._parent == new_block

# Scenario 3: Test invalid input with non-task objects in the list
def test_invalid_input():
    task1 = Task(block={'action': 'shell', 'args': {'cmd': 'echo "Hello, World!"'}})
    invalid_object = {"not": "a task"}
    
    with pytest.raises(TypeError):
        _dupe_task_list([task1, invalid_object], Task())
