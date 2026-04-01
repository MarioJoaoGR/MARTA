
import pytest
from pymonet.task import Task

def test_edge_case():
    # Define a mock fork function
    def my_fork(reject, resolve):
        return resolve("test")
    
    # Create an instance of Task with the mock fork function
    task = Task.of(None)  # Passing None as value since it's not used in the mock fork function
    
    # Assert that the task has a fork attribute and it is callable
    assert hasattr(task, 'fork')
    assert callable(task.fork)
