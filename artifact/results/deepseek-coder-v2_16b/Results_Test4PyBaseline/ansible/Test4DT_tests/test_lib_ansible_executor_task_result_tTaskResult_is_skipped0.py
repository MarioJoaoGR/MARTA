
import pytest
from ansible.executor.task_result import TaskResult, DataLoader

# Test initialization with dictionary return_data
def test_task_result_initialization_with_dict():
    result = TaskResult(host="localhost", task="fetch_data", return_data={"status": "success", "data": {"key1": "value1"}}, task_fields={"user": "admin"})
    assert result._host == "localhost"
    assert result._task == "fetch_data"
    assert result._result == {"status": "success", "data": {"key1": "value1"}}
    assert result._task_fields == {"user": "admin"}

# Test initialization with string return_data
def test_task_result_initialization_with_string():
    task_result = TaskResult('localhost', 'update_packages', "some data that can't be directly used")