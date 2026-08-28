
import pytest
from pymonet.task import Task
from unittest.mock import patch

def test_calling_the_function_encapsulated_in_a_task():
    def reject(error):
        pytest.fail("Unexpected reject call")
    
    def resolve(result):
        assert result == 'Success'
    
    task = Task(lambda r, j: j('Success'))  # Mock function for testing
    with patch('pymonet.task.Task', return_value=task):
        task.fork(reject, resolve)
