
import pytest
from pymonet.task import Task

# Test initialization with a fork function
def test_initialization_with_fork_function():
    def my_fork_function(reject, resolve):
        result = "Success!"
        if result:
            resolve(result)  # Resolve the task with the result
        else:
            reject("Error occurred")  # Reject the task if there's an error
    
    task = Task(my_fork_function)
    assert callable(task.fork) and task.fork is not None

# Test mapping over a task
def test_mapping_over_a_task():
    def fork_function(reject, resolve):
        resolve("Success!")
    
    task = Task(fork_function)
    
    def transform_result(value):
        return value + "!"  # Example transformation

    mapped_task = task.map(transform_result)