
import pytest
from pymonet.task import Task

def test_valid_input():
    def my_fork(reject, resolve):
        # Example implementation of a fork function
        pass
    
    def my_mapper(value):
        # Example implementation of a mapper function
        return value * 2
    
    task = Task(my_fork)
    mapped_task = task.map(my_mapper)
    
    assert callable(mapped_task.fork)
