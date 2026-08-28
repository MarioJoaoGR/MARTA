
import pytest
from pymonet.task import Task

# Test initialization of Task class with a function that handles errors and successful results
def test_task_initialization():
    def my_function(reject, resolve):
        try:
            result = 42  # Example value
            resolve(result)
        except Exception as e:
            reject(e)
    
    task = Task(my_function)
    assert callable(task.fork)

# Test calling fork method to execute the function encapsulated in the Task
def test_calling_fork():
    def my_function(reject, resolve):
        try:
            result = 42  # Example value
            resolve(result)
        except Exception as e:
            reject(e)
    
    task = Task(my_function)
    
    def reject(error):
        assert False, "This should not be called"
    
    def resolve(result):
        assert result == 42
    
    task.fork(reject, resolve)

# Test using map method to transform the value of the Task
def test_using_map():
    def my_function(reject, resolve):
        try:
            result = 42  # Example value
            resolve(result)
        except Exception as e:
            reject(e)
    
    task = Task(my_function)
    
    def double_value(x):
        return x * 2
    
    mapped_task = task.map(double_value)
    
    def reject(error):
        assert False, "This should not be called"
    
    def resolve(result):
        assert result == 84
    
    mapped_task.fork(reject, resolve)

# Test using bind method to chain operations using functions that return new Tasks
def test_using_bind():
    def my_function(reject, resolve):
        try:
            result = 42  # Example value
            resolve(result)
        except Exception as e:
            reject(e)
    
    task = Task(my_function)
    
    def double_value(x):
        return Task.of(x * 2)
    
    bound_task = task.bind(double_value)
    
    def reject(error):
        assert False, "This should not be called"
    
    def resolve(result):
        assert result == 84
    
    bound_task.fork(reject, resolve)
