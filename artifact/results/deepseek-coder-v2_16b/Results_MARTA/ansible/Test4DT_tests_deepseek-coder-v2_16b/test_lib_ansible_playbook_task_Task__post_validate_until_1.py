
import pytest
from ansible.playbook.task import Task


def test_init_with_role():
    role = "example_role"
    task = Task(block={'action': 'shell', 'args': {'cmd': 'echo hello'}}, role=role)
    assert hasattr(task, '_role')
    assert task._role == role

def test_init_with_task_include():
    included_task = Task()
    task = Task(task_include=included_task)
    assert hasattr(task, '_parent')
    assert task._parent is not None
