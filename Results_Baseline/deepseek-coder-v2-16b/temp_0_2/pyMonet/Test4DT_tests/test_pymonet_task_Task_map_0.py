
# Module: pymonet.task
import pytest
from pymonet.task import Task

# Test initialization of Task with a fork function that resolves successfully
def test_task_initialization():
    def my_fork(reject, resolve):
        resolve("success")
    
    task = Task(my_fork)
    assert task.fork == my_fork

# Test map method to transform the resolved value of a Task
def test_map_method():
    def my_mapper(value):
        return value * 2
    
    task = Task(lambda reject, resolve: resolve(42))
    new_task = task.map(my_mapper)
    assert new_task.fork(lambda x: f"Rejected: {x}", lambda x: f"Resolved: {x}") == "Resolved: 84"

# Test bind method to chain tasks
def test_bind_method():
    def my_fork(reject, resolve):
        resolve("success")
    
    task = Task(my_fork)
    
    def next_task(value):
        return Task(lambda reject, resolve: resolve(value + 10))
    
    new_task = task.bind(next_task)