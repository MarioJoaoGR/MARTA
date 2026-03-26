
import pytest
from pymonet.task import Task

# Helper function to create a mock fork function for testing
def my_fork(reject, resolve):
    # Example implementation of a fork function
    pass

# Test initialization of Task class with a custom fork function
def test_task_initialization():
    task = Task(my_fork)
    assert task.fork == my_fork

# Helper function to create a mock mapper function for testing
def double_value(value):
    return value * 2

# Test bind method with a simple mapper function
def test_bind_method():
    task = Task(my_fork)
    chained_task = task.bind(lambda x: Task.of(double_value(x)))
    assert isinstance(chained_task, Task)

# Helper function to create a mock rejected task for testing
def handle_reject(error):
    return f"Rejected with error: {error}"

# Test fork method with a resolved and rejected tasks
def test_fork_method():
    resolved_task = Task.of(42)
    rejected_task = Task.reject('Error')
    
    assert resolved_task.fork(handle_reject, lambda x: f"Resolved: {x}") == "Resolved: 42"
    assert rejected_task.fork(handle_reject, lambda x: f"Resolved: {x}") == "Rejected with error: Error"

# Test complex transformations using bind and map
def test_complex_transformations():
    task = Task(my_fork)
    
    def square_and_double(value):
        return Task.of(value * value).bind(lambda x: Task.of(x * 2))
    
    complex_task = task.bind(square_and_double)
    assert isinstance(complex_task, Task)