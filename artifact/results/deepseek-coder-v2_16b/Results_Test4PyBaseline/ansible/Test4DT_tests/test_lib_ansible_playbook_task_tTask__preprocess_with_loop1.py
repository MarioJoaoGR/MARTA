
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

# Test _preprocess_with_loop with valid loop data
def test_preprocess_with_loop_valid(default_task):
    new_ds = {}
    k = "with_items"
    v = [{"item1": "value1"}, {"item2": "value2"}]
    default_task._preprocess_with_loop(None, new_ds, k, v)
    assert new_ds['loop'] == v
    assert new_ds['loop_with'] == 'items'

# Test _preprocess_with_loop with None value
def test_preprocess_with_loop_none(default_task):
    new_ds = {}
    k = "with_items"
    v = None
    with pytest.raises(AnsibleError) as excinfo:
        default_task._preprocess_with_loop(None, new_ds, k, v)
    assert str(excinfo.value) == "you must specify a value when using %s" % k

# Test _preprocess_with_loop with duplicate loop data
def test_preprocess_with_loop_duplicate(task_with_block):
    new_ds = {'loop': [{"item1": "value1"}, {"item2": "value2"}]}
    k = "with_items"
    v = [{"item3": "value3"}, {"item4": "value4"}]
    with pytest.raises(AnsibleError) as excinfo:
        task_with_block._preprocess_with_loop(None, new_ds, k, v)
    assert str(excinfo.value) == "duplicate loop in task: items"

# Test _preprocess_with_loop with valid loop data and existing loop data
def test_preprocess_with_loop_existing_loop(task_with_block):
    new_ds = {'loop': [{"item1": "value1"}, {"item2": "value2"}]}
    k = "with_items"
    v = [{"item3": "value3"}, {"item4": "value4"}]
    with pytest.raises(AnsibleError) as excinfo:
        task_with_block._preprocess_with_loop(None, new_ds, k, v)
    assert str(excinfo.value) == "duplicate loop in task: items"
