
# Module: ansible.playbook.task_include
# test_task_include.py
from ansible.errors import AnsibleParserError  # Corrected import statement for AnsibleParserError
import pytest
from ansible.playbook.task_include import TaskInclude

@pytest.fixture
def task_include():
    return TaskInclude(block={'file': 'example.yml'}, role='example_role', task_include={'action': 'run'})

def test_initialization(task_include):
    assert hasattr(task_include, 'block') and task_include.block == {'file': 'example.yml'}
    assert hasattr(task_include, 'role') and task_include.role == 'example_role'
    assert hasattr(task_include, 'task_include') and task_include.task_include == {'action': 'run'}
    assert not task_include.statically_loaded

def test_preprocess_data(task_include):
    # Valid data
    valid_data = {
        'action': 'some_action',
        'args': {'arg1': 'value1'},
        'name': 'example_name'
    }
    preprocessed_valid_data = task_include.preprocess_data(valid_data)
    assert preprocessed_valid_data == valid_data

    # Invalid data with extra keys
    invalid_data = {
        'action': 'some_action',
        'invalid_key': 'invalid_value',  # Invalid key
        'args': {'arg1': 'value1'}
    }
    preprocessed_invalid_data = task_include.preprocess_data(invalid_data)
    assert 'invalid_key' not in preprocessed_invalid_data
    assert len(preprocessed_invalid_data) == 2  # Only action and args should be present

def test_invalid_attribute_handling():
    task = TaskInclude()
    
    # Test with invalid attribute that should raise an error
    data_with_invalid_key = {
        'action': 'some_action',
        'invalid_key': 'invalid_value'  # Invalid key
    }
    with pytest.raises(AnsibleParserError):
        task.preprocess_data(data_with_invalid_key)
    
    # Test with invalid attribute that should be ignored
    data_with_invalid_key = {
        'action': 'some_action',
        'invalid_key': 'invalid_value'  # Invalid key
    }
    task.INVALID_TASK_ATTRIBUTE_FAILED = False
    preprocessed_data = task.preprocess_data(data_with_invalid_key)
    assert 'invalid_key' not in preprocessed_data
    assert len(preprocessed_data) == 1  # Only action should be present
