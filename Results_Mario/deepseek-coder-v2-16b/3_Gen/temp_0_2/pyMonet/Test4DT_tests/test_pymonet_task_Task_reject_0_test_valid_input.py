
import pytest
from pymonet.task import Task

def test_valid_input():
    def my_function(reject, resolve):
        return 'success'
    
    task = Task(my_function)
    assert task.fork is not None
