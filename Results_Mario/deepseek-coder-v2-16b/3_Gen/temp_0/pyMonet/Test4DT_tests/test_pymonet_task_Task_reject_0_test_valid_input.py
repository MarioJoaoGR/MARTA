
import pytest
from pymonet.task import Task

def test_valid_input():
    def my_fork(reject, resolve):
        return 'success'
    
    task = Task(my_fork)
    assert task.fork is not None
