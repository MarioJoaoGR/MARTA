
# Module: ansible.playbook.task
# test_task.py
from ansible.playbook.task import Task
import pytest

def test_default_task():
    # Test creating a new Task instance with default values
    task = Task()
    assert task is not None, "Task creation failed"

def test_specific_role_and_block():
    # Test creating a task with specific role and block configuration
    block_data = {'action': 'shell', 'args': {'cmd': 'echo hello'}}
    task = Task(block=block_data, role='exampleRole')
    assert hasattr(task, '_role'), "Role not set correctly"
    assert hasattr(task, '_parent'), "Block or parent task not set correctly"

def test_inheriting_from_another_task():
    # Test creating a task that includes another task as its parent
    included_task = Task()
    main_task = Task(task_include=included_task)
    assert hasattr(main_task, '_parent'), "Parent task not set correctly"

def test_get_name():
    # Test using the `get_name` method
    block_data = {'action': 'shell', 'args': {'cmd': 'echo hello'}}
    task = Task(role='exampleRole', block=block_data)