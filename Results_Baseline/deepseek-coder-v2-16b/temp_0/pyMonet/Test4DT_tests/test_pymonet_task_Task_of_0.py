# Module: pymonet.task
import pytest
from pymonet.task import Task

# Test creating an instance of Task with a custom fork function
def test_create_instance_with_custom_fork():
    def my_fork(reject, resolve):
        # Example implementation of a fork function
        pass
    
    task = Task(my_fork)
    assert callable(task.fork), "The 'fork' attribute should be a callable function."

# Test creating a resolved Task with a value
def test_create_resolved_task():
    value = "example value"
    resolved_task = Task.of(value)
    assert isinstance(resolved_task, Task), "Expected an instance of Task but got something else."
    assert callable(resolved_task.fork), "The 'fork' attribute should be a callable function."

# Test creating a rejected Task encapsulating an error message (not implemented in this test)
# def test_create_rejected_task():
#     with pytest.raises(NotImplementedError):
#         rejected_task = Task.reject("error message")

# Test using map to transform the value of a resolved task
def test_map_transform_resolved_task():
    value = 5
    resolved_task = Task.of(value)
    
    def double_value(value):
        return value * 2
    
    mapped_task = resolved_task.map(double_value)
    assert isinstance(mapped_task, Task), "Expected an instance of Task but got something else."
    assert callable(mapped_task.fork), "The 'fork' attribute should be a callable function."

# Test using bind to chain another asynchronous operation (not implemented in this test)
# def test_bind_chained_operation():
#     with pytest.raises(NotImplementedError):
#         chained_task = resolved_task.bind(chained_operation)
