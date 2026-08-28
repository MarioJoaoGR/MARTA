
import pytest
from unittest.mock import Mock
from ansible.executor.task_result import TaskResult, DataLoader

# Test initialization with dictionary return_data
def test_task_result_initialization_with_dict():
    result = TaskResult(host="localhost", task="fetch_data", return_data={"status": "success", "data": {"key1": "value1"}}, task_fields={"user": "admin"})
    assert result._host == "localhost"
    assert result._task == "fetch_data"
    assert result._result == {"status": "success", "data": {"key1": "value1"}}
    assert result._task_fields == {"user": "admin"}

# Test initialization with string return_data and DataLoader mock
def test_task_result_initialization_with_string():
    data_loader_mock = Mock()
    data_loader_mock.load.return_value = [{'results': [{'key': 'nested_value'}]}]
    result = TaskResult('localhost', 'fetch_data', data_loader_mock, {'task_specific': 'field'})
    assert result._check_key('key') is False
    assert result._check_key('nested_value') is True

# Test _check_key method with top-level key
def test_check_key_top_level():
    result = TaskResult(host="localhost", task="fetch_data", return_data={"status": "success", "data": {"key1": "value1"}}, task_fields={"user": "admin"})
    assert result._check_key('status') == "success"
    assert result._check_key('data') == {'key1': 'value1'}

# Test _check_key method with nested key
def test_check_key_nested():
    data_loader_mock = Mock()
    data_loader_mock.load.return_value = [{'results': [{'key': 'nested_value'}]}]
    result = TaskResult('localhost', 'fetch_data', data_loader_mock, {'task_specific': 'field'})
    assert result._check_key('key') is False
    assert result._check_key('nested_value') is True

# Test _check_key method with non-existent key
def test_check_key_non_existent():
    result = TaskResult(host="localhost", task="fetch_data", return_data={"status": "success", "data": {"key1": "value1"}}, task_fields={"user": "admin"})
    assert result._check_key('nonexistent') is False
