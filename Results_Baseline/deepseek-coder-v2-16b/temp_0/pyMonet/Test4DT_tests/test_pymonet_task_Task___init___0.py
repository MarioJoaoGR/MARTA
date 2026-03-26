# Module: pymonet.task
# test_pymonet_task.py
from pymonet.task import Task
import pytest

def test_init():
    def my_fork(reject, resolve):
        pass
    
    task = Task(my_fork)
    assert callable(task.fork), "The fork attribute should be a callable function."

def test_of_resolved_task():
    resolved_task = Task.of("example value")
    assert callable(resolved_task.fork), "A resolved task's fork should be a callable function."

def test_reject_rejected_task():
    rejected_task = Task.reject("error message")
    assert callable(rejected_task.fork), "A rejected task's fork should be a callable function."

def test_map_transform():
    resolved_task = Task.of("example value")
    
    def double_value(value):
        return value * 2
    
    mapped_task = resolved_task.map(double_value)
    assert callable(mapped_task.fork), "The transformed task's fork should be a callable function."

def test_bind_chain():
    resolved_task = Task.of("example value")
    
    def chained_operation(value):
        return Task.of(value + 1)
    
    chained_task = resolved_task.bind(chained_operation)
    assert callable(chained_task.fork), "The chained task's fork should be a callable function."
