
import pytest
from ansible.executor.task_result import TaskResult, DataLoader
from unittest.mock import patch

# Mocking DataLoader for testing purposes
class MockDataLoader:
    def load(self, data):
        return data

@pytest.fixture
def task_result():
    return TaskResult(host="localhost", task="fetch_data", return_data={"status": "success", "data": {"key1": "value1"}}, task_fields={"user": "admin"})

# Test cases for TaskResult class
def test_task_result_initialization():
    result = TaskResult(host="localhost", task="fetch_data", return_data={"status": "success", "data": {"key1": "value1"}}, task_fields={"user": "admin"})
    assert result._host == "localhost"
    assert result._task == "fetch_data"
    assert result._result == {"status": "success", "data": {"key1": "value1"}}
    assert result._task_fields == {"user": "admin"}

def test_needs_debugger_default(task_result):
    with patch('ansible.executor.task_result.C', {'TASK_DEBUGGER_IGNORE_ERRORS': False}):
        assert not task_result.needs_debugger()
        assert not task_result.needs_debugger(globally_enabled=True)

def test_needs_debugger_on_failed(task_result):
    with patch('ansible.executor.task_result.C', {'TASK_DEBUGGER_IGNORE_ERRORS': False}):
        task_result._result = {"status": "failed"}
        assert task_result.needs_debugger()
        assert not task_result.needs_debugger(globally_enabled=True)

def test_needs_debugger_on_unreachable(task_result):
    with patch('ansible.executor.task_result.C', {'TASK_DEBUGGER_IGNORE_ERRORS': False}):
        task_result._result = {"status": "unreachable"}
        assert task_result.needs_debugger()
        assert not task_result.needs_debugger(globally_enabled=True)

def test_needs_debugger_always_enabled(task_result):
    with patch('ansible.executor.task_result.C', {'TASK_DEBUGGER_IGNORE_ERRORS': False}):
        task_result._task_fields = {"debugger": "always"}
        assert task_result.needs_debugger()
        assert not task_result.needs_debugger(globally_enabled=True)

def test_needs_debugger_never_enabled(task_result):
    with patch('ansible.executor.task_result.C', {'TASK_DEBUGGER_IGNORE_ERRORS': False}):
        task_result._task_fields = {"debugger": "never"}
        assert not task_result.needs_debugger()
        assert not task_result.needs_debugger(globally_enabled=True)

def test_needs_debugger_on_failed_ignore_errors(task_result):
    with patch('ansible.executor.task_result.C', {'TASK_DEBUGGER_IGNORE_ERRORS': True}):
        task_result._result = {"status": "failed"}
        assert not task_result.needs_debugger()
        assert not task_result.needs_debugger(globally_enabled=True)

def test_needs_debugger_on_skipped(task_result):
    with patch('ansible.executor.task_result.C', {'TASK_DEBUGGER_IGNORE_ERRORS': False}):
        task_result._result = {"status": "skipped"}
        assert not task_result.needs_debugger()
        assert not task_result.needs_debugger(globally_enabled=True)
