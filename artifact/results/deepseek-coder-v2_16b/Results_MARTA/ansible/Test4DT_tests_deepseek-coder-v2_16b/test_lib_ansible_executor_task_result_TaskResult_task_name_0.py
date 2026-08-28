
import pytest
from ansible.executor.task_result import TaskResult

# Test Scenario 1: Test standard input with dictionary return data
def test_valid_case_with_dict_data():
    host = 'localhost'
    task = None
    return_data = {'results': [{'skipped': True}, {'skipped': False}]}
    result = TaskResult(host, task, return_data)
    
    assert result._host == host
    assert result._task is None
    assert result._result == return_data
    assert result._task_fields == {}

# Test Scenario 2: Test edge case with empty task fields
def test_edge_case_with_empty_task_fields():
    host = 'localhost'
    task = None
    return_data = {'results': [{'skipped': True}, {'skipped': False}]}
    result = TaskResult(host, task, return_data)
    
    assert result._host == host
    assert result._task is None
    assert result._result == return_data
    assert result._task_fields == {}

# Test Scenario 3: Test invalid input with None task
def test_invalid_input_with_none_task():
    host = 'localhost'
    task = None
    return_data = {'results': [{'skipped': True}, {'skipped': False}]}
    result = TaskResult(host, task, return_data)
    
    assert result._host == host
    assert result._task is None
    assert result._result == return_data
    assert result._task_fields == {}
