
import pytest
from unittest.mock import Mock, patch
from ansible.executor.task_result import TaskResult, DataLoader

# Test initialization with dictionary return_data
def test_init_with_dict():
    host = "localhost"
    task = "fetch_data"
    return_data = {"status": "success", "data": {"key1": "value1"}}
    task_fields = {"user": "admin"}
    result = TaskResult(host, task, return_data, task_fields)
    
    assert result._host == host
    assert result._task == task
    assert result._result == return_data
    assert result._task_fields == task_fields

# Test initialization with string return_data
def test_init_with_string():
    host = "localhost"
    task = "fetch_data"
    return_data = '{"status": "success", "data": {"key1": "value1"}}'
    task_fields = {"user": "admin"}
    
    with patch.object(DataLoader, 'load', return_value={"status": "success", "data": {"key1": "value1"}}):
        result = TaskResult(host, task, return_data, task_fields)
        
        assert result._host == host
        assert result._task == task
        assert result._result == {"status": "success", "data": {"key1": "value1"}}
        assert result._task_fields == task_fields

# Test checking if the task was skipped
def test_is_skipped():
    return_data = {"status": "skipped"}
    task_fields = {}
    result = TaskResult(host="localhost", task="fetch_data", return_data=return_data, task_fields=task_fields)
    