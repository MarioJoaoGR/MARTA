
# Module: pymonet.task
# test_pymonet_task.py
from pymonet.task import Task
import pytest

# Test instantiating a Task with a fork function
def test_instantiate_task_with_fork_function():
    def my_fork_function(reject, resolve):
        resolve("Success")  # Resolve the task with "Success"
    
    task = Task(my_fork_function)
    assert hasattr(task, 'fork'), "Task should have a fork method"

# Test creating a resolved Task using of class method
def test_create_resolved_task():
    resolved_task = Task.of(42)
    assert isinstance(resolved_task, Task), "Expected a Task instance"