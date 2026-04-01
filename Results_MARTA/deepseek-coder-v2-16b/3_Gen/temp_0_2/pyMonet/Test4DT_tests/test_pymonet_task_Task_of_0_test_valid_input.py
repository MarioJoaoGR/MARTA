
import pytest
from unittest.mock import MagicMock
from pymonet.task import Task

def test_valid_input():
    # Create a mock function to be used as fork
    mock_fork = MagicMock()
    
    # Instantiate the Task with the mock function
    task = Task(mock_fork)
    
    # Call the of method on the Task class and check if it returns an instance of Task
    resolved_task = Task.of(42)  # Assuming 'of' is a class method in Task
    
    # Assert that the returned task is indeed an instance of Task
    assert isinstance(resolved_task, Task)
    
    # Optionally, you can add more assertions to check the behavior or properties of the resolved task
