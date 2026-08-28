# Module: pymonet.task
import pytest
from pymonet.task import Task

# Test initialization of a Task with a successful fork function
def test_task_initialization():
    def my_fork_function(reject, resolve):
        resolve("Success")
    
    task = Task(my_fork_function)
    assert task is not None

# Test creating a resolved Task
def test_resolved_task():
    resolved_task = Task.of(10)
    assert isinstance(resolved_task, Task)

# Test creating a rejected Task
def test_rejected_task():
    rejected_task = Task.reject("Task failed")
    assert isinstance(rejected_task, Task)

# Test mapping over a Task
def test_map_over_task():
    def transform_result(value):
        return value * 2
    
    task = Task(lambda reject, resolve: resolve(10))
    mapped_task = task.bind(transform_result)
    assert mapped_task is not None

# Test binding to another Task
def test_binding_to_another_task():
    def another_fork_function(reject, resolve):
        resolve("Success")
    
    another_task = Task(another_fork_function)

    task = Task(lambda reject, resolve: resolve(10))
    bound_task = task.bind(lambda value: another_task if value else Task.reject("Binding error"))
    assert bound_task is not None

# Test binding to a rejected Task
def test_binding_to_rejected_task():
    def another_fork_function(reject, resolve):
        reject("Error")
    
    another_task = Task(another_fork_function)

    task = Task(lambda reject, resolve: reject("Error"))
    bound_task = task.bind(lambda value: another_task if value else Task.reject("Binding error"))
    assert bound_task is not None
