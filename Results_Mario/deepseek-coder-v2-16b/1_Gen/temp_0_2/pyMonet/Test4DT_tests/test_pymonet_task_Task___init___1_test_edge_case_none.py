
import pytest
from pymonet.task import Task

def test_edge_case_none():
    def my_fork(reject, resolve):
        # Example implementation of a fork function
        pass
    
    task = Task(my_fork)
    assert callable(task.fork)
