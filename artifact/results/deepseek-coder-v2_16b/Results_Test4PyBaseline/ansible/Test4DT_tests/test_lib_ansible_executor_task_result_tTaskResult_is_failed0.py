
import pytest
from unittest.mock import Mock, patch
from ansible.executor.task_result import TaskResult, DataLoader

# Test initialization with dictionary return_data
def test_init_with_dict():
    result = TaskResult(host="localhost", task="fetch_data", return_data={"status": "success", "data": {"key1": "value1"}}, task_fields={"user": "admin"})
    assert result._host == "localhost"
    assert result._task == "fetch_data"
    assert result._result == {"status": "success", "data": {"key1": "value1"}}
    assert result._task_fields == {"user": "admin"}

# Test initialization with string return_data (mocked DataLoader)
@patch('ansible.executor.task_result.DataLoader')
def test_init_with_string(MockDataLoader):
    mock_loader = Mock()
    mock_loader.load.return_value = {"status": "success", "data": {"key1": "value1"}}
    MockDataLoader.return_value = mock_loader
    
    result = TaskResult(host="localhost", task="fetch_data", return_data="some_key", task_fields={"user": "admin"})
    assert result._host == "localhost"
    assert result._task == "fetch_data"
    assert result._result == {"status": "success", "data": {"key1": "value1"}}
    assert result._task_fields == {"user": "admin"}

# Test checking if the task was skipped
def test_is_skipped():
    result = TaskResult(host="localhost", task="fetch_data", return_data={"status": "skipped"}, task_fields={})