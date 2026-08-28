
# Module: ansible.playbook.task
# test_task.py
from ansible.playbook.task import Task
import pytest

def test_default_initialization():
    task = Task()
    assert task is not None, "Task creation failed"
    assert task._parent is None
    assert not task.implicit
    assert task.resolved_action is None

def test_initialization_with_role():
    role = 'exampleRole'
    task = Task(role=role)
    assert hasattr(task, '_role'), "Role not set correctly"
    assert task._role == role
    assert task._parent is None

def test_initialization_with_block():
    block = {'action': 'shell', 'args': {'cmd': 'echo hello'}}
    task = Task(block=block)
    assert hasattr(task, '_parent'), "Block not set correctly"
    assert task._parent == block

def test_initialization_with_role_and_block():
    role = 'exampleRole'
    block = {'action': 'shell', 'args': {'cmd': 'echo hello'}}
    task = Task(role=role, block=block)
    assert hasattr(task, '_role'), "Role not set correctly"
    assert hasattr(task, '_parent'), "Block not set correctly"
    assert task._role == role
    assert task._parent == block

def test_initialization_with_role_and_include():
    role = 'exampleRole'
    included_task = Task()
    task = Task(role=role, task_include=included_task)
    assert hasattr(task, '_role'), "Role not set correctly"
    assert hasattr(task, '_parent'), "Included task not set correctly"
    assert task._role == role
    assert task._parent == included_task

def test_initialization_with_only_task_include():
    included_task = Task()
    task = Task(task_include=included_task)
    assert hasattr(task, '_parent'), "Included task not set correctly"
    assert task._parent == included_task
