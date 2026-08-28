
import pytest
from unittest.mock import Mock
from ansible.executor.task_result import TaskResult, DataLoader

@pytest.fixture
def task_result():
    return TaskResult(host="localhost", task="fetch_data", return_data={"status": "success", "data": {"key1": "value1"}}, task_fields={"user": "admin"})

def test_task_result_with_dict_return_data(task_result):
    assert task_result._host == "localhost"
    assert task_result._task == "fetch_data"
    assert task_result._result == {"status": "success", "data": {"key1": "value1"}}
    assert task_result._task_fields == {"user": "admin"}

def test_task_result_with_string_return_data(monkeypatch):
    # Mocking DataLoader to simulate loading data from a string
    def mock_load(self, data):
        return {"status": "success", "data": {"key1": "value1"}}
    
    monkeypatch.setattr(DataLoader, 'load', mock_load)
    
    task_result = TaskResult(host="localhost", task="fetch_data", return_data='{"status": "success", "data": {"key1": "value1"}}')
    
    assert task_result._host == "localhost"
    assert task_result._task == "fetch_data"
    assert task_result._result == {"status": "success", "data": {"key1": "value1"}}
    assert task_result._task_fields == {}

def test_task_result_with_default_task_fields(task_result):
    task_result = TaskResult(host="localhost", task="fetch_data", return_data={"status": "success", "data": {"key1": "value1"}})
    
    assert task_result._host == "localhost"
    assert task_result._task == "fetch_data"
    assert task_result._result == {"status": "success", "data": {"key1": "value1"}}