
import pytest
from ansible.executor.task_result import TaskResult

# Test case for line 55-56 where 'results' is not in self._result
def test_is_skipped_no_results():
    task_result = TaskResult(host="localhost", task="fetch_data", return_data={"status": "success"})
    assert task_result.is_skipped() == False

# Test case for line 59-60 where results are present but not all items are skipped
def test_is_skipped_some_not_skipped():
    task_result = TaskResult(host="localhost", task="fetch_data", return_data={"status": "success", "results": [{"failed": True}, {"failed": False}]})
    assert task_result.is_skipped() == False

# Test case for line 59-60 where results are present and all items are skipped
def test_is_skipped_all_skipped():
    task_result = TaskResult(host="localhost", task="fetch_data", return_data={"status": "success", "results": [{"skipped": True}, {"skipped": True}]})
    assert task_result.is_skipped() == True

# Test case for line 63 where 'skipped' is directly in self._result
def test_is_skipped_directly_skipped():
    task_result = TaskResult(host="localhost", task="fetch_data", return_data={"status": "success", "skipped": True})
    assert task_result.is_skipped() == True

# Test case for line 63 where 'skipped' is not in self._result but other conditions might apply
def test_is_skipped_no_skipped():
    task_result = TaskResult(host="localhost", task="fetch_data", return_data={"status": "success"})
    assert task_result.is_skipped() == False
