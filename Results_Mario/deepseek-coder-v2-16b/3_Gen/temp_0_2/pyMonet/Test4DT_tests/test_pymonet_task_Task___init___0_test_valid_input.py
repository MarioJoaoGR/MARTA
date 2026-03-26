
import pytest
from pymonet.task import Task

def test_valid_input():
    def my_function(reject, resolve):
        pass
    
    task = Task(my_function)
    assert isinstance(task, Task)
    assert task.fork == my_function
