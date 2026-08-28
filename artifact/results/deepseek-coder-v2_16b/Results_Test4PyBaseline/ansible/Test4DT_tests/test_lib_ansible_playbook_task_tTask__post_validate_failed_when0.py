
# Module: ansible.playbook.task
import pytest
from unittest.mock import Mock  # Importing Mock from unittest, not standard library
from ansible.playbook.task import Task

# Example Usage 1: Creating a Task Instance with Role and Block
def test_create_task_with_role_and_block():
    block = {'action': 'shell', 'args': {'cmd': 'echo hello'}}
    task = Task(block=block, role='exampleRole')
    assert isinstance(task, Task)
    assert task._role == 'exampleRole'
    assert task._parent is not None

# Example Usage 2: Creating a Task Instance Including Another Task
def test_create_task_with_included_task():
    included_task = Task()
    main_task = Task(task_include=included_task)
    assert isinstance(main_task, Task)
    assert main_task._parent is not None

# Example Usage 3: Creating a Task Instance with Both Role and Block
def test_create_task_with_both_role_and_block():
    block_data = {'action': 'shell', 'args': {'cmd': 'echo hello'}}
    task = Task(block=block_data, role='exampleRole')
    assert isinstance(task, Task)
    assert task._role == 'exampleRole'