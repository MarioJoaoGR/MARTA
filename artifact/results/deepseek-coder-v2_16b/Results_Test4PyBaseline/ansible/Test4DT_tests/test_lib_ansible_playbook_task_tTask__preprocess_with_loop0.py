
# Module: ansible.playbook.task
# test_task.py
from ansible.errors import AnsibleError  # Corrected import statement for AnsibleError
from ansible.playbook.task import Task
import pytest

@pytest.fixture
def default_task():
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
def task_with_both():
    block_data = {'action': 'shell', 'args': {'cmd': 'echo hello'}}
    return Task(block=block_data, role='exampleRole')

# Test creating a default Task instance
def test_default_task(default_task):
    assert isinstance(default_task, Task)