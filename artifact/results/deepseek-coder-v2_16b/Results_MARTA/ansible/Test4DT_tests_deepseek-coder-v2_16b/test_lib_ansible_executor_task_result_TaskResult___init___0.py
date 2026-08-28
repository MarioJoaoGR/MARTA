
import pytest
from ansible.executor.task_result import TaskResult
from ansible.parsing.dataloader import DataLoader

def test_valid_return_data():
    return_data = {'results': [{'skipped': True}, {'skipped': False}]}
    task_fields = {'additional_field': 'value'}
    result = TaskResult(host='localhost', task='update_packages', return_data=return_data, task_fields=task_fields)
    assert isinstance(result._result, dict), "Expected _result to be a dictionary"
    assert result._result == return_data, "Expected _result to match the provided return_data"

def test_invalid_return_data():
    with pytest.raises(TypeError):
        TaskResult(host='localhost', task='update_packages', return_data=None)

def test_none_task_fields():
    return_data = {'results': [{'skipped': True}, {'skipped': False}]}
    result = TaskResult(host='localhost', task='update_packages', return_data=return_data, task_fields=None)
    assert isinstance(result._task_fields, dict), "Expected _task_fields to be a dictionary"
    assert not result._task_fields, "Expected _task_fields to be an empty dictionary when None is provided"
