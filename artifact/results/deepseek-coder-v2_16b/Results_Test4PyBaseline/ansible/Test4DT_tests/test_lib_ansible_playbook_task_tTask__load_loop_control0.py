# Module: ansible.playbook.task
# test_task.py
from ansible.playbook.task import Task
import pytest

@pytest.fixture
def task():
    return Task()

def test_initialization(task):
    assert task is not None, "Task instance should be created"

def test_role_assignment(task):
    role = 'exampleRole'
    task = Task(role=role)
    assert task._role == role, f"Expected role to be {role}, but got {task._role}"

def test_parent_assignment():
    block_data = {'key': 'value'}
    task = Task(block=block_data)
    assert isinstance(task._parent, dict), "Parent should be a dictionary"

def test_include_task_as_parent(task):
    included_task = Task()
    task = Task(task_include=included_task)
    assert task._parent is not None and task._parent == included_task, "Task include as parent failed"

def test_load_loop_control():
    ds = {'key': 'value'}
    with pytest.raises(AnsibleParserError):
        Task()._load_loop_control('attr', ds)

    ds = {}
    loop_control = Task()._load_loop_control('attr', ds)
    assert isinstance(loop_control, LoopControl), "Expected a LoopControl instance"
