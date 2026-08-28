
import pytest
from unittest.mock import Mock
from ansible.executor.task_result import TaskResult, DataLoader

# Test initialization with dictionary return_data
def test_init_with_dict():
    result = TaskResult(host="localhost", task="fetch_data", return_data={"status": "success", "data": {"key1": "value1"}}, task_fields={"user": "admin"})
    assert result._host == "localhost"
    assert result._task == "fetch_data"
    assert result._result == {"status": "success", "data": {"key1": "value1"}}