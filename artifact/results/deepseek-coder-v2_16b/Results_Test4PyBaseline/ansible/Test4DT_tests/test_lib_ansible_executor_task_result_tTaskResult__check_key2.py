
import pytest
from unittest.mock import Mock
from ansible.executor.task_result import TaskResult

# Test _check_key method with top-level key in a dictionary
def test_check_key_top_level_dict():
    result = TaskResult(host="localhost", task="fetch_data", return_data={"status": "success", "data": {"key1": "value1"}}, task_fields={"user": "admin"})
    assert result._check_key('status') == "success"
    assert result._check_key('data') == {'key1': 'value1'}

# Test _check_key method with nested key in a dictionary
def test_check_key_nested_dict():
    result = TaskResult(host="localhost", task="fetch_data", return_data={"status": "success", "data": {"key1": "value1"}}, task_fields={"user": "admin"})