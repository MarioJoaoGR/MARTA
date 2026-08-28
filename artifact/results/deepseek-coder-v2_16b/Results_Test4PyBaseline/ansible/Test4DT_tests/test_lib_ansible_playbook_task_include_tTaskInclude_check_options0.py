# Module: ansible.playbook.task_include
# test_task_include.py
from ansible.playbook.task_include import TaskInclude
import pytest

@pytest.fixture
def task_include():
    return TaskInclude(block={'file': 'example.yml'}, role='example_role', task_include={'action': 'run'})

def test_task_include_initialization(task_include):
    assert task_include.block == {'file': 'example.yml'}
    assert task_include.role == 'example_role'
    assert task_include.task_include == {'action': 'run'}
    assert not task_include.statically_loaded

def test_check_options_valid(task_include):
    # Valid data for a task include
    valid_data = {
        'action': 'run',
        'args': {'arg1': 'value1'},
        '_raw_params': 'example.yml'
    }
    validated_task = task_include.check_options(valid_data, None)
    assert validated_task['action'] == 'run'
    assert validated_task['args']['arg1'] == 'value1'
    assert validated_task['_raw_params'] == 'example.yml'

def test_check_options_invalid_bad_opts(task_include):
    # Invalid options for the task include
    invalid_data = {
        'action': 'run',
        'args': {'arg1': 'value1'},
        '_raw_params': 'example.yml',
        'invalid_key': 'invalid_value'
    }
    with pytest.raises(Exception) as e:
        task_include.check_options(invalid_data, None)
    assert str(e.value) == "Invalid options for run: invalid_key"

def test_check_options_no_file_specified(task_include):
    # No file specified in the data
    no_file_data = {
        'action': 'run',
        'args': {'arg1': 'value1'},
        '_raw_params': None
    }
    with pytest.raises(Exception) as e:
        task_include.check_options(no_file_data, None)
    assert str(e.value) == "No file specified for run"

def test_check_options_invalid_apply(task_include):
    # Invalid apply option for the task include
    invalid_apply_data = {
        'action': 'run',
        'args': {'arg1': 'value1'},
        '_raw_params': 'example.yml',
        'apply': {}
    }
    with pytest.raises(Exception) as e:
        task_include.check_options(invalid_apply_data, None)
    assert str(e.value) == "Invalid options for run: apply"
