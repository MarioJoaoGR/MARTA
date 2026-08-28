
import pytest
from pymonet import Task

# Test initialization with a function
def test_task_initialization():
    def my_function(reject, resolve):
        resolve(42)
    
    task = Task(my_function)
    assert task is not None

# Test using fork method to handle the result
def test_fork_method():
    def my_function(reject, resolve):
        resolve(42)
    
    task = Task(my_function)
    task.fork(lambda e: pytest.fail("Unexpected error"), lambda r: assert r == 42)

# Test using of class method to create a resolved task
def test_of_class_method():
    value = 42
    resolved_task = Task.of(value)
    assert resolved_task is not None
    resolved_task.fork(lambda e: pytest.fail("Unexpected error"), lambda r: assert r == value)

# Test using map method to transform the result
def test_map_method():
    def my_function(reject, resolve):
        resolve(21)
    
    task = Task(my_function)
    transformed_task = task.map(lambda x: x * 2)
    assert transformed_task is not None
    transformed_task.fork(lambda e: pytest.fail("Unexpected error"), lambda r: assert r == 42)

# Test using bind method to chain tasks
def test_bind_method():
    def my_function(reject, resolve):
        resolve(21)
    
    task = Task(my_function)
    def bind_function():
        return Task.of(42)
    
    bound_task = task.bind(bind_function)
    assert bound_task is not None
    bound_task.fork(lambda e: pytest.fail("Unexpected error"), lambda r: assert r == 42)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
SyntaxError: invalid syntax (line 19, col 68)
    task.fork(lambda e: pytest.fail("Unexpected error"), lambda r: assert r == 42)
"""