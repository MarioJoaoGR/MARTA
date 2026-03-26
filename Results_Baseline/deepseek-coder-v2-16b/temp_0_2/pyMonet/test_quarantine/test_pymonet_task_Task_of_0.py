
# Module: pymonet.task
import pytest
from pymonet.task import Task

# Test creating a Task instance with a custom fork function
def test_create_task_with_custom_fork():
    def my_fork(reject, resolve):
        resolve("Success!")
    
    task = Task(my_fork)
    assert task.fork == "Success!"

# Test creating a resolved Task with a value
def test_create_resolved_task():
    resolved_task = Task.of("Hello, World!")
    result = resolved_task.fork(lambda err: f"Error: {err}", lambda res: f"Result: {res}")
    assert result == "Result: Hello, World!"

# Test mapping over a Task
def test_map_over_task():
    def double_value(value):
        return value * 2
    
    task = Task.of(5)
    mapped_task = task.map(double_value)
    result = mapped_task.fork(lambda err: f"Error: {err}", lambda res: f"Result: {res}")
    assert result == "Result: 10"

# Test chaining tasks with bind
def test_chaining_tasks_with_bind():
    def add_one(value):
        return Task.of(value + 1)
    
    task = Task.of(5)
    chained_task = task.bind(add_one)
    result = chained_task.fork(lambda err: f"Error: {err}", lambda res: f"Result: {res}")
    assert result == "Result: 6"

# Test handling rejection in fork function
def test_handle_rejection_in_fork():
    task = Task(lambda reject, resolve: reject("An error occurred"))
    result = task.fork(lambda err: f"Error: {err}", lambda res: f"Result: {res}")
    assert result == "Error: An error occurred"

# Test handling multiple tasks in sequence with bind
def test_multiple_tasks_in_sequence():
    def add_two(value):
        return Task.of(value + 2)
    
    task = Task.of(5)
    chained_task = task.bind(lambda x: add_two(x)).bind(add_one)
    result = chained_task.fork(lambda err: f"Error: {err}", lambda res: f"Result: {res}")
    assert result == "Result: 8"

if __name__ == "__main__":
    pytest.main()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_task_Task_of_0
pyMonet/Test4DT_tests/test_pymonet_task_Task_of_0.py:52:56: E0602: Undefined variable 'add_one' (undefined-variable)


"""