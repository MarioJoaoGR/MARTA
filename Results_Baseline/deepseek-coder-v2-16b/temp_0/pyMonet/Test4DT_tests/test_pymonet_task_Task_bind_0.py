# Module: pymonet.task
import pytest
from pymonet.task import Task

# Helper functions for creating tasks
def my_fork(reject, resolve):
    # Example implementation of a fork function
    pass

def double_value(value):
    return value * 2

def chained_operation(value):
    return Task.of(value + 1)

# Test cases for initializing a Task object
def test_task_initialization():
    task = Task(my_fork)
    assert callable(task.fork), "Task fork should be a callable function"

# Test cases for creating resolved and rejected tasks
def test_create_resolved_task():
    resolved_task = Task.of("example value")
    assert isinstance(resolved_task, Task), "Resolved task should be an instance of Task"

def test_create_rejected_task():
    rejected_task = Task.reject("error message")
    assert isinstance(rejected_task, Task), "Rejected task should be an instance of Task"

# Test cases for using the map method
def test_map_method_on_resolved_task():
    resolved_task = Task.of("example value")
    mapped_task = resolved_task.map(double_value)
    assert isinstance(mapped_task, Task), "Mapped task should be an instance of Task"

# Test cases for using the bind method
def test_bind_method_on_resolved_task():
    resolved_task = Task.of("example value")
    chained_task = resolved_task.bind(chained_operation)
    assert isinstance(chained_task, Task), "Chained task should be an instance of Task"

# Additional test cases for edge cases and error handling (if necessary)
def test_bind_method_on_rejected_task():
    rejected_task = Task.reject("error message")
    chained_task = rejected_task.bind(chained_operation)
    assert isinstance(chained_task, Task), "Chained task should be an instance of Task"
