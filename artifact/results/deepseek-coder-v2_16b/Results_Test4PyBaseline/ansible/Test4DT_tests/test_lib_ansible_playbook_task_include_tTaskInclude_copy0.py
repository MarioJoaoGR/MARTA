# Module: ansible.playbook.task_include
# test_task_include.py
from ansible.playbook.task_include import TaskInclude
import pytest

@pytest.fixture
def task():
    return TaskInclude(block={'file': 'example.yml'}, role='example_role', task_include={'action': 'run'})

def test_initialization(task):
    assert task.block == {'file': 'example.yml'}
    assert task.role == 'example_role'
    assert task.task_include == {'action': 'run'}
    assert not task.statically_loaded

def test_copying_instance():
    original_task = TaskInclude(block={'file': 'example.yml'}, role='example_role', task_include={'action': 'run'})
    copied_task = original_task.copy()
    assert copied_task.block == {'file': 'example.yml'}
    assert copied_task.role == 'example_role'
    assert copied_task.task_include == {'action': 'run'}
    assert not copied_task.statically_loaded

def test_preprocessing_data():
    data = {
        'action': 'some_action',
        'invalid_key': 'invalid_value',
        'args': {'arg1': 'value1'}
    }
    task = TaskInclude(block={'file': 'example.yml'}, role='example_role', task_include={'action': 'run'})
    processed_data = task.preprocess_data(data)
    assert 'invalid_key' not in processed_data
    assert processed_data['action'] == 'some_action'
    assert processed_data['args'] == {'arg1': 'value1'}

def test_handling_task_inclusion():
    data = {
        'include': True,
        'keywords': ['listen']
    }
    with pytest.raises(NotImplementedError):
        handler = HandlerTaskInclude.load(data)

def test_building_parent_block(task):
    parent_block = task.build_parent_block()
    assert isinstance(parent_block, dict)
    assert 'file' in parent_block or '_raw_params' in parent_block

def test_getting_vars_for_included_tasks(task):
    vars_for_included_tasks = task.get_vars()
    assert isinstance(vars_for_included_tasks, dict)
