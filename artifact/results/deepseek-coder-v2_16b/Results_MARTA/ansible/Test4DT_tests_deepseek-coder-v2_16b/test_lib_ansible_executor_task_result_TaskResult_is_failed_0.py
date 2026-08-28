
import pytest
from ansible.executor.task_result import TaskResult
from ansible.parsing.dataloader import DataLoader
import json

# Test for successful instantiation of TaskResult with dictionary return data
def test_successful_instantiation():
    task_result = TaskResult(host='localhost', task='example_task', return_data={'key': 'value'})
    assert isinstance(task_result._result, dict)
    assert task_result._result == {'key': 'value'}

# Test for successful instantiation of TaskResult with string return data
def test_successful_instantiation_with_string():
    return_data = json.dumps({'key': 'value'})
    task_result = TaskResult(host='localhost', task='example_task', return_data=return_data)
    assert isinstance(task_result._result, dict)
    assert task_result._result == {'key': 'value'}

# Test for checking if the task has failed when explicitly marked as failed
def test_is_failed_when_explicitly_marked():
    return_data = {'results': [{'failed': True}]}
    task_result = TaskResult(host='localhost', task='example_task', return_data=return_data)
    assert task_result.is_failed() is True

# Test for checking if the task has failed when not explicitly marked but other conditions indicate failure
def test_is_failed_when_not_explicitly_marked():
    return_data = {'results': [{'failed_when_result': True}]}
    task_result = TaskResult(host='localhost', task='example_task', return_data=return_data)
    assert task_result.is_failed() is True

# Test for checking if the task has failed when no conditions indicate failure
def test_is_failed_when_no_failure():
    return_data = {'results': [{'skipped': False}]}
    task_result = TaskResult(host='localhost', task='example_task', return_data=return_data)
    assert task_result.is_failed() is False
