
# Module: ansible.playbook.task
# test_task.py
from ansible.playbook.task import Task
import pytest

@pytest.fixture
def blank_task():
    return Task()

@pytest.fixture
def task_with_block():
    block_data = {'action': 'shell', 'args': {'cmd': 'echo hello'}}
    return Task(block=block_data, role='exampleRole')

@pytest.fixture
def task_with_include():
    included_task = Task()
    return Task(task_include=included_task)

@pytest.fixture
def loaded_task():
    datastructure = {'action': 'shell', 'args': {'cmd': 'echo hello'}}
    return Task.load(datastructure)

# Test initialization of a blank task
def test_blank_task_initialization(blank_task):
    assert hasattr(blank_task, '_role'), "Task should have an attribute _role"
    assert blank_task._parent is None, "Blank task should not have a parent by default"

# Test get_vars with no parent or vars
def test_get_vars_no_parent_or_vars(blank_task):
    assert blank_task.get_vars() == {}, "Blank task should return an empty dictionary for variables"

# Test get_vars with a parent that has vars
@pytest.mark.parametrize("role, expected", [('exampleRole', {'action': 'shell', 'args': {'cmd': 'echo hello'}}), ('anotherRole', {})])
def test_get_vars_with_parent(task_with_block, role, expected):
    task_with_block._role = role