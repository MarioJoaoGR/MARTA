
# Module: ansible.executor.task_result
# test_task_result.py
from ansible.executor.task_result import TaskResult
import pytest
from unittest.mock import patch, MagicMock

@pytest.fixture
def task_result():
    return TaskResult(host="localhost", task="fetch_data", return_data={"status": "success", "data": {"key1": "value1"}}, task_fields={"user": "admin"})

def test_task_result_initialization_with_dict(task_result):
    assert task_result._host == "localhost"
    assert task_result._task == "fetch_data"
    assert task_result._result == {"status": "success", "data": {"key1": "value1"}}
    assert task_result._task_fields == {"user": "admin"}

def test_task_result_initialization_with_string():
    with patch('ansible.executor.task_result.DataLoader') as mock_dataloader:
        mock_dataloader.return_value.load.return_value = {"status": "success", "data": {"key1": "value1"}}
        result = TaskResult(host="localhost", task="fetch_data", return_data="some_string", task_fields={"user": "admin"})
        assert result._host == "localhost"
        assert result._task == "fetch_data"
        assert result._result == {"status": "success", "data": {"key1": "value1"}}