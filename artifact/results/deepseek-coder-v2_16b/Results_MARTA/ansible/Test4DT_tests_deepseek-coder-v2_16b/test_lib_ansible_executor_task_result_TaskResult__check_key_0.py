
import pytest
from ansible.executor.task_result import TaskResult

# Test initialization of TaskResult class
def test_task_result_initialization():
    task_result = TaskResult(host='localhost', task='update_packages', return_data={'results': [{'skipped': True}, {'skipped': False}]})
    assert hasattr(task_result, '_host') and task_result._host == 'localhost'
    assert hasattr(task_result, '_task') and task_result._task == 'update_packages'
    assert isinstance(task_result._result, dict)
    assert len(task_result._result.get('results', [])) > 0

# Test _check_key method when key exists in result
def test_check_key_exists():
    task_result = TaskResult(host='localhost', task='update_packages', return_data={'results': [{'skipped': True}, {'skipped': False}]})
    assert task_result._check_key('skipped') is True

# Test _check_key method when key does not exist in result
def test_check_key_does_not_exist():
    task_result = TaskResult(host='localhost', task='update_packages', return_data={'results': [{'skipped': True}, {'skipped': False}]})
    assert task_result._check_key('failed') is False

# Test _check_key method when key exists in nested dictionary
def test_check_key_nested():
    task_result = TaskResult(host='localhost', task='update_packages', return_data={'results': [{'status': {'code': 0}}, {'status': {'code': 1}}]})
    assert task_result._check_key('status.code') == 0

# Test _check_key method when key does not exist in nested dictionary
def test_check_key_nested_does_not_exist():
    task_result = TaskResult(host='localhost', task='update_packages', return_data={'results': [{'status': {'code': 0}}, {'status': {'code': 1}}]})
    assert task_result._check_key('status.name') is False
