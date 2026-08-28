
# Module: ansible.playbook.task
# test_task.py
from ansible.playbook.task import Task
import pytest

@pytest.fixture
def default_task():
    return Task()

@pytest.fixture
def task_with_role():
    return Task(role='deploy')

@pytest.fixture
def task_with_block():
    block_data = {'action': 'shell', 'args': {'cmd': 'echo hello'}}
    return Task(block=block_data, role='deploy')

@pytest.fixture
def task_including_another_task():
    included_task = Task()
    return Task(task_include=included_task)

# Test cases for Task initialization with default values
def test_default_task_initialization(default_task):
    assert hasattr(default_task, '_role') and default_task._role is None
    assert hasattr(default_task, '_parent') and default_task._parent is None
    assert hasattr(default_task, 'implicit') and not default_task.implicit
    assert hasattr(default_task, 'resolved_action') and default_task.resolved_action is None

# Test cases for Task initialization with specific role
def test_task_with_role_initialization(task_with_role):
    assert task_with_role._role == 'deploy'
    assert hasattr(task_with_role, '_parent') and task_with_role._parent is None
    assert hasattr(task_with_role, 'implicit') and not task_with_role.implicit
    assert hasattr(task_with_role, 'resolved_action') and task_with_role.resolved_action is None

# Test cases for Task initialization with block and role
def test_task_with_block_initialization(task_with_block):
    assert task_with_block._role == 'deploy'
    assert hasattr(task_with_block, '_parent') and isinstance(task_with_block._parent, dict)
    assert task_with_block._parent['action'] == 'shell'
    assert task_with_block._parent['args']['cmd'] == 'echo hello'
    assert hasattr(task_with_block, 'implicit') and not task_with_block.implicit