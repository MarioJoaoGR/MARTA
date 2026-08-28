
import pytest
from ansible.executor.task_result import TaskResult

# Test initialization with dictionary return_data
def test_init_with_dict():
    result = TaskResult(host="localhost", task="fetch_data", return_data={"status": "success", "data": {"key1": "value1"}}, task_fields={"user": "admin"})
    assert result._host == "localhost"
    assert result._task == "fetch_data"
    assert result._result == {"status": "success", "data": {"key1": "value1"}}

# Test is_unreachable method with 'unreachable' key present
def test_is_unreachable_true():
    result = TaskResult(host="localhost", task="fetch_data", return_data={"status": "failure", "unreachable": True, "data": {"key1": "value1"}}, task_fields={"user": "admin"})
    assert result.is_unreachable() is True

# Test is_unreachable method with 'unreachable' key absent
def test_is_unreachable_false():
    result = TaskResult(host="localhost", task="fetch_data", return_data={"status": "failure", "data": {"key1": "value1"}}, task_fields={"user": "admin"})