
# Module: ansible.playbook.task
# test_task.py
from ansible.errors import AnsibleParserError
import pytest
from ansible.playbook.task import Task

@pytest.fixture
def default_task():
    return Task()

@pytest.fixture
def task_with_role():
    return Task(role='exampleRole')

@pytest.fixture
def task_with_block():
    block_data = {'action': 'shell', 'args': {'cmd': 'echo hello'}}
    return Task(block=block_data, role='exampleRole')

@pytest.fixture
def included_task():
    return Task()

def test_default_task(default_task):
    assert default_task._role is None
    assert default_task._parent is None
    assert not default_task.implicit
    assert default_task.resolved_action is None

def test_task_with_role(task_with_role):
    assert task_with_role._role == 'exampleRole'
    assert task_with_role._parent is None
    assert not task_with_role.implicit
    assert task_with_role.resolved_action is None

def test_task_include(default_task, included_task):
    default_task = Task(task_include=included_task)
    assert default_task._parent == included_task
    assert not default_task.implicit
    assert default_task.resolved_action is None

def test_task_with_block(task_with_block):
    assert task_with_block._role == 'exampleRole'
    assert isinstance(task_with_block._parent, dict)
    assert not task_with_block.implicit
    assert task_with_block.resolved_action is None

def test_get_name(task_with_role):
    task_with_role.resolved_action = 'shell'
    assert task_with_role.get_name() == 'exampleRole and shell'

def test_repr(task_with_role):
    task_with_role.resolved_action = 'shell'
    expected_repr = "Task(role='exampleRole', parent=None, implicit=False, resolved_action='shell')"
    assert repr(task_with_role) == expected_repr

def test_preprocess_data(default_task):
    ds = {'key': 'value'}
    default_task.preprocess_data(ds)
    assert default_task._parent == ds

def test_post_validate(default_task):
    templar = None  # Assuming you have a templar object
    with pytest.raises(AnsibleParserError, match=r'.*This error can be suppressed as a warning using the "invalid_task_attribute_failed" configuration'):
        default_task.post_validate(templar)

def test_set_loader(default_task):
    loader = None  # Assuming you have a loader object
    default_task.set_loader(loader)
    assert default_task._loader == loader

def test_all_parents_static(included_task):
    included_task._parent = Task()
    assert not included_task.all_parents_static()
    included_task._parent = None
    assert included_task.all_parents_static()

def test_get_first_parent_include(default_task, included_task):
    default_task = Task(task_include=included_task)
    first_parent = default_task.get_first_parent_include()
    assert first_parent == included_task
