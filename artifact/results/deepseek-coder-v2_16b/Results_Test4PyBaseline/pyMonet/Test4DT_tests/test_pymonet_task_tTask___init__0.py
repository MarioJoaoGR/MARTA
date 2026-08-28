
import pytest
from pymonet.task import Task

# Test initialization of a Task with a basic fork function
def test_init_with_basic_fork():
    def my_fork_function(reject, resolve):
        resolve("Success")
    
    task = Task(my_fork_function)
    assert hasattr(task, 'fork')

# Test initialization of a Task with the reject class method
def test_init_with_reject():
    task = Task.reject("An error occurred")
    assert hasattr(task, 'fork')