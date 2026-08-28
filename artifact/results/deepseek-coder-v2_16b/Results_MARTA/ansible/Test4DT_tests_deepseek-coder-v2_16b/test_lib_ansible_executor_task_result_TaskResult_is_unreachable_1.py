
import pytest
from ansible.executor.task_result import TaskResult

# Test case for checking if the task is skipped

# Test case for checking if the task has failed
def test_has_failed():
    task_data = {'results': [{'skipped': False}, {'failed': True}]}
    result = TaskResult(host='example_host', task={'task': 'example_task'}, return_data=task_data)
    
    assert result.is_failed() is True

# Test case for checking if the task is unreachable
def test_is_unreachable():
    task_data = {'results': [{'skipped': False}, {'failed': False, 'unreachable': True}]}
    result = TaskResult(host='example_host', task={'task': 'example_task'}, return_data=task_data)
    
    assert result.is_unreachable() is True