
import pytest
from ansible.executor.task_result import TaskResult
from unittest.mock import patch, MagicMock

# Fixture to create a TaskResult instance for testing
@pytest.fixture
def task_result():
    return TaskResult(host='localhost', task='update_packages', return_data={'results': [{'skipped': True}, {'skipped': False}]})

# Test scenario 1: Creating a TaskResult with dictionary as return data
def test_task_result_with_dict():
    return_data = {'results': [{'skipped': True}, {'skipped': False}]}
    task_fields = {'additional_field': 'value'}
    result = TaskResult(host='localhost', task='update_packages', return_data=return_data, task_fields=task_fields)
    
    assert result._host == 'localhost'
    assert result._task == 'update_packages'
    assert result._result == return_data
    assert result._task_fields == task_fields

# Test scenario 2: Creating a TaskResult with string as return data
def test_task_result_with_string():
    return_data = '{"results": [{"skipped": True}, {"skipped': False}]}'
    task_fields = {'additional_field': 'value'}
    
    # Mock DataLoader to simulate loading from string
    with patch('ansible.executor.task_result.DataLoader') as mock_dataloader:
        instance = MagicMock()
        instance.load.return_value = return_data
        mock_dataloader.return_value = instance
        
        result = TaskResult(host='localhost', task='update_packages', return_data=return_data, task_fields=task_fields)
        
        assert result._host == 'localhost'
        assert result._task == 'update_packages'
        assert result._result == {'results': [{'skipped': True}, {'skipped': False}]}
        assert result._task_fields == task_fields

# Test scenario 3: Creating a TaskResult without additional task fields
def test_task_result_without_task_fields():
    return_data = {'results': [{'skipped': True}, {'skipped': False}]}
    
    result = TaskResult(host='localhost', task='update_packages', return_data=return_data)
    
    assert result._host == 'localhost'
    assert result._task == 'update_packages'
    assert result._result == return_data
    assert result._task_fields == {}

# Test scenario 4: Creating a TaskResult with None for task fields
def test_task_result_with_none_for_task_fields():
    return_data = {'results': [{'skipped': True}, {'skipped': False}]}
    
    result = TaskResult(host='localhost', task='update_packages', return_data=return_data, task_fields=None)
    
    assert result._host == 'localhost'
    assert result._task == 'update_packages'
    assert result._result == return_data
    assert result._task_fields == {}

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
SyntaxError: unmatched '}' (line 24, col 69)
    return_data = '{"results": [{"skipped": True}, {"skipped': False}]}'
"""