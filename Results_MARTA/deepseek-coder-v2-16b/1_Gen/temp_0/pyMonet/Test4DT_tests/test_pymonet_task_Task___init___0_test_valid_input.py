
import pytest
from pymonet.task import Task

def test_valid_input():
    def my_fork(reject, resolve):
        return "resolved"
    
    task = Task(my_fork)
    assert callable(task.fork)
    result = task.fork(lambda: None, lambda: None)
    assert result == "resolved"
