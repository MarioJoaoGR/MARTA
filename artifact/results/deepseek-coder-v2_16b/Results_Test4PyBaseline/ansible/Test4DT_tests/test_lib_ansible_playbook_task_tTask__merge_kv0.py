
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
    assert hasattr(task_with_block, 'resolved_action') and task_with_block.resolved_action is None

# Test cases for Task initialization including another task as parent
def test_task_including_another_task_initialization(task_including_another_task):
    assert hasattr(task_including_another_task, '_parent') and isinstance(task_including_another_task._parent, dict)
    assert not hasattr(task_including_another_task, '_role')  # Role should be inherited from parent if not provided
    assert hasattr(task_including_another_task, 'implicit') and not task_including_another_task.implicit
    assert hasattr(task_including_another_task, 'resolved_action') and task_including_another_task.resolved_action is None

# Additional test cases for _merge_kv method
def test_merge_kv_with_none():
    task = Task()
    assert task._merge_kv(None) == ""

def test_merge_kv_with_string():
    task = Task()
    ds = "some string"
    assert task._merge_kv(ds) == ds

def test_merge_kv_with_dict():
    task = Task()
    ds = {'key1': 'value1', 'key2': 'value2'}
    expected_output = "key1=value1 key2=value2"
    assert task._merge_kv(ds) == expected_output
