
import pytest
from ansible.executor.task_result import TaskResult


def test_invalid_input():
    return_data = {'results': [{'key1': 'value1'}, {'key2': 'value2'}]}
    task_result = TaskResult(host='localhost', task='example_task', return_data=return_data)
    assert task_result._check_key('nonexistent_key') is False