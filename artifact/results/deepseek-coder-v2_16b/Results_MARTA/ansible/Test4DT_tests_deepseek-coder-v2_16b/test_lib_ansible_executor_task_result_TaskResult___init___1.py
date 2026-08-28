
import pytest
from ansible.executor.task_result import TaskResult
from ansible.parsing.dataloader import DataLoader

# Example 1: Using a Dictionary as Return Data
def test_TaskResult_with_dict_return_data():
    return_data = {'results': [{'skipped': True}, {'skipped': False}]}
    task_fields = {'additional_field': 'value'}
    result = TaskResult(host='localhost', task='update_packages', return_data=return_data, task_fields=task_fields)
    
    assert result._host == 'localhost'
    assert result._task == 'update_packages'
    assert result._result == {'results': [{'skipped': True}, {'skipped': False}]}
    assert result._task_fields == {'additional_field': 'value'}

# Example 2: Using a String as Return Data
def test_TaskResult_with_string_return_data():
    return_data = '{"results": [{"skipped": True}, {"skipped": False}]}'
    task_fields = {'additional_field': 'value'}
    result = TaskResult(host='localhost', task='update_packages', return_data=return_data, task_fields=task_fields)
    
    assert result._host == 'localhost'
    assert result._task == 'update_packages'
    assert result._result == {'results': [{'skipped': True}, {'skipped': False}]}
    assert result._task_fields == {'additional_field': 'value'}

# Example 3: Without Additional Task Fields
def test_TaskResult_without_task_fields():
    return_data = {'results': [{'skipped': True}, {'skipped': False}]}
    result = TaskResult(host='localhost', task='update_packages', return_data=return_data)
    
    assert result._host == 'localhost'
    assert result._task == 'update_packages'
    assert result._result == {'results': [{'skipped': True}, {'skipped': False}]}
    assert result._task_fields == {}

# Example 4: Using None for Optional Task Fields
def test_TaskResult_with_none_for_task_fields():
    return_data = {'results': [{'skipped': True}, {'skipped': False}]}
    result = TaskResult(host='localhost', task='update_packages', return_data=return_data, task_fields=None)
    
    assert result._host == 'localhost'
    assert result._task == 'update_packages'
    assert result._result == {'results': [{'skipped': True}, {'skipped': False}]}
    assert result._task_fields == {}
