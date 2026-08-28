
import pytest
from ansible.executor.task_result import TaskResult

# Test case for when 'failed_when_result' is in self._result or its nested results
def test_is_failed_with_failed_when_result():
    result = TaskResult(host="localhost", task="fetch_data", return_data={"status": "success", "failed_when_result": True}, task_fields={})
    assert result.is_failed() is True

def test_is_failed_with_nested_failed_when_result():
    result = TaskResult(host="localhost", task="fetch_data", return_data={"status": "success", "results": [{"failed_when_result": True}, {"failed_when_result": False}]}, task_fields={})
    assert result.is_failed() is True

def test_is_failed_without_failures():
    result = TaskResult(host="localhost", task="fetch_data", return_data={"status": "success"}, task_fields={})
    assert result.is_failed() is False

# Test case for when 'failed' is present in self._result but not 'failed_when_result'
def test_is_failed_with_only_failed():
    result = TaskResult(host="localhost", task="fetch_data", return_data={"status": "success", "failed": True}, task_fields={})
    assert result.is_failed() is True
