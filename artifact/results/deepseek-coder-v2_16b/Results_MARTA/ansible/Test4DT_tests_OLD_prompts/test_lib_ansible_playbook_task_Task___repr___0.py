
import pytest
from unittest.mock import patch, MagicMock
from ansible.playbook.task import Task

def test_task_creation_with_block():
    with patch('ansible.playbook.task.C', new=MagicMock()):
        task = Task(block={'action': 'shell', 'args': {'cmd': 'echo hello'}})
        assert isinstance(task, Task)
        assert task._role is None
        assert task._parent == {'action': 'shell', 'args': {'cmd': 'echo hello'}}

def test_task_creation_with_role():
    with patch('ansible.playbook.task.C', new=MagicMock()):
        task = Task(role='example_role')
        assert isinstance(task, Task)
        assert task._role == 'example_role'
        assert task._parent is None

def test_task_creation_with_task_include():
    included_task = Task()
    with patch('ansible.playbook.task.C', new=MagicMock()):
        main_task = Task(task_include=included_task)
        assert isinstance(main_task, Task)
        assert main_task._parent == included_task



