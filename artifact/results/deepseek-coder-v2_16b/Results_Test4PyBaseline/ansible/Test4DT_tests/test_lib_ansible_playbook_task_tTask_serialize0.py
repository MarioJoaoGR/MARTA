
import pytest
from ansible.playbook.task import Task

# Test creating a Task with default values
def test_create_task_with_default_values():
    task = Task()
    assert hasattr(task, '_role'), "Task should have a role attribute"
    assert task._role is None, "Default role should be None"
    assert not hasattr(task, 'parent'), "Task should not have a parent by default"

# Test creating a Task with specific role
def test_create_task_with_specific_role():
    task = Task(role='exampleRole')
    assert task._role == 'exampleRole', "Task role should be set to 'exampleRole'"
    assert not hasattr(task, 'parent'), "Task should not have a parent by default"

# Test creating a Task that includes another Task as its parent
def test_create_task_with_included_task():
    included_task = Task()
    main_task = Task(task_include=included_task)
    assert main_task._parent == included_task, "Main task should have the included task as its parent"

# Test creating a Task with both role and block
def test_create_task_with_block_and_role():
    block_data = {'action': 'shell', 'args': {'cmd': 'echo hello'}}
    task = Task(block=block_data, role='exampleRole')
    assert task._role == 'exampleRole', "Task role should be set to 'exampleRole'"