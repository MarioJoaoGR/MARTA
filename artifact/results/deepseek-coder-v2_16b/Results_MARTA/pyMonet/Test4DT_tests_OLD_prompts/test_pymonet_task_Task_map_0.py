
import pytest
from unittest.mock import patch, MagicMock
from pymonet.task import Task

# Test initialization with a function
def test_initialization_with_function():
    def my_function(reject, resolve):
        resolve(42)
    
    task = Task(my_function)
    assert task is not None

# Test calling the function encapsulated in a Task
def test_calling_the_function_encapsulated_in_a_task():
    def my_function(reject, resolve):
        resolve(42)
    
    task = Task(my_function)
    
    def reject(error):
        assert False, "This should not be called"
    
    def resolve(result):
        assert result == 42
    
    task.fork(reject, resolve)

# Test using the `map` method to transform the Task's value
def test_using_the_map_method_to_transform_the_tasks_value():
    def my_function(reject, resolve):
        resolve(21)
    
    task = Task(my_function)
    
    def double_value(x):
        return x * 2
    
    mapped_task = task.map(double_value)
    
    def reject(error):
        assert False, "This should not be called"
    
    def resolve(result):
        assert result == 42
    
    mapped_task.fork(reject, resolve)

# Test using the `bind` method to chain tasks
def test_using_the_bind_method_to_chain_tasks():
    def my_function(reject, resolve):
        resolve(10)
    
    task = Task(my_function)
    
    def another_function(value):
        return Task.of(value * 2)
    
    chained_task = task.bind(another_function)
    
    def reject(error):
        assert False, "This should not be called"
    
    def resolve(result):
        assert result == 20
    
    chained_task.fork(reject, resolve)

# Test creating a Task that immediately resolves or rejects
def test_creating_a_task_that_immediately_resolves_or_rejects():
    resolved_task = Task.of("Success")
    assert resolved_task is not None
    
    def reject(error):
        assert False, "This should not be called"
    
    def resolve(result):
        assert result == "Success"
    
    resolved_task.fork(reject, resolve)

    rejected_task = Task.reject(Exception("Failure"))
    assert rejected_task is not None
    
    def reject(error):
        assert str(error) == "Failure"
    
    def resolve(result):
        assert False, "This should not be called"
    
    rejected_task.fork(reject, resolve)

# Test combining tasks using `ap` (Apply)
def test_combining_tasks_using_ap():
    def my_function(reject, resolve):
        resolve(10)
    
    task = Task(my_function)
    
    def apply_function(value):
        return value * 2
    
    applied_task = task.map(apply_function)
    
    def reject(error):
        assert False, "This should not be called"
    
    def resolve(result):
        assert result == 20
    
    applied_task.fork(reject, resolve)
