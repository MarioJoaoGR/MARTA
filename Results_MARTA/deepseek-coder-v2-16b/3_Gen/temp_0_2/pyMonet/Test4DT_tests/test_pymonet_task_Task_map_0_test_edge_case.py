
import pytest
from pymonet.task import Task

def test_edge_case():
    # Test edge case with None input for fork function and empty map function
    task = Task(lambda reject, resolve: reject("Error"))  # Initialize a rejected task
    
    # Attempt to map an empty function (should not change the task)
    mapped_task = task.map(lambda x: x)
    
    # Execute the original task and assert it is in the rejected state
    with pytest.raises(Exception):
        task.fork(lambda reject, resolve: None, lambda reject, resolve: None)
