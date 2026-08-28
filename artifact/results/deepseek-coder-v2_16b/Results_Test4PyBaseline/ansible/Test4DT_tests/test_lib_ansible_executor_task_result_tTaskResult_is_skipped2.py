
import pytest
from ansible.executor.task_result import TaskResult

# Test initialization with non-dictionary return_data, should raise TypeError
def test_task_result_initialization_with_non_dict():
    with pytest.raises(TypeError):
        TaskResult('localhost', 'update_packages', 12345)

# Test is_skipped method when results are present and all items are skipped
def test_is_skipped_all_items_skipped():
    result = TaskResult(host="localhost", task="fetch_data", return_data={"status": "success", "results": [{"skipped": True}, {"skipped": True}]})
    assert result.is_skipped() is True

# Test is_skipped method when results are present but not all items are skipped
def test_is_skipped_not_all_items_skipped():
    result = TaskResult(host="localhost", task="fetch_data", return_data={"status": "success", "results": [{"skipped": True}, {"skipped": False}]})
    assert result.is_skipped() is False

# Test is_skipped method when results are not present
def test_is_skipped_no_results():
    result = TaskResult(host="localhost", task="fetch_data", return_data={"status": "success"})
    assert result.is_skipped() is False

# Test is_skipped method when skipped key is directly in the main result dict
def test_is_skipped_directly_in_main_dict():
    result = TaskResult(host="localhost", task="fetch_data", return_data={"status": "success", "skipped": True})
    assert result.is_skipped() is True

# Test is_skipped method when skipped key is not present in the main dict or results
def test_is_skipped_not_present():
    result = TaskResult(host="localhost", task="fetch_data", return_data={"status": "success"})
    assert result.is_skipped() is False
