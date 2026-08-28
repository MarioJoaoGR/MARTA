
import pytest
from lib.ansible.executor.task_result import TaskResult, DataLoader





def test_is_changed():
    task_result = TaskResult(host='localhost', task='update_packages', return_data={'results': [{'changed': True}, {'changed': False}]})
    assert task_result.is_changed() is True

def test_is_not_changed():
    task_result = TaskResult(host='localhost', task='update_packages', return_data={'results': [{'skipped': True}, {'skipped': False}]})
    assert task_result.is_changed() is False