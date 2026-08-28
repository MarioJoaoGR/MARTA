# Module: ansible.executor.task_result
import pytest
from ansible.executor.task_result import TaskResult, DataLoader

# Test Case 1: Basic Usage
def test_basic_usage():
    result = TaskResult(host="localhost", task="fetch_data", return_data={"status": "success", "data": {"key1": "value1"}}, task_fields={"user": "admin"})
    
    assert result._host == "localhost"
    assert result._task == "fetch_data"
    assert result._result == {"status": "success", "data": {"key1": "value1"}}
    assert result._task_fields == {"user": "admin"}

# Test Case 2: Using a String for Return Data
def test_string_return_data():
    result = TaskResult(host="localhost", task="fetch_data", return_data='{"status": "success", "data": {"key1": "value1"}}', task_fields={"user": "admin"})
    
    assert result._host == "localhost"
    assert result._task == "fetch_data"
    assert result._result == {"status": "success", "data": {"key1": "value1"}}
    assert result._task_fields == {"user": "admin"}

# Test Case 3: Without Task Fields
def test_without_task_fields():
    result = TaskResult(host="localhost", task="fetch_data", return_data={"status": "success", "data": {"key1": "value1"}})
    
    assert result._host == "localhost"
    assert result._task == "fetch_data"
    assert result._result == {"status": "success", "data": {"key1": "value1"}}
    assert result._task_fields == {}

# Test Case 4: Using Default Values for Task Fields
def test_default_task_fields():
    result = TaskResult(host="localhost", task="fetch_data", return_data={"status": "success", "data": {"key1": "value1"}})
    
    assert result._host == "localhost"
    assert result._task == "fetch_data"
    assert result._result == {"status": "success", "data": {"key1": "value1"}}
    assert result._task_fields == {}
