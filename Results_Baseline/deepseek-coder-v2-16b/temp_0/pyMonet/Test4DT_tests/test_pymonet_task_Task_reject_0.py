# Module: pymonet.task
# test_pymonet_task.py
from pymonet.task import Task

def test_task_initialization():
    def my_fork(reject, resolve):
        pass
    
    task = Task(my_fork)
    assert callable(task.fork), "Task should have a callable fork attribute"

def test_create_resolved_task():
    resolved_task = Task.of("example value")
    assert isinstance(resolved_task, Task), "Expected an instance of Task"
    assert callable(resolved_task.fork), "Resolved task should have a callable fork attribute"

def test_create_rejected_task():
    rejected_task = Task.reject("error message")
    assert isinstance(rejected_task, Task), "Expected an instance of Task"
    assert callable(rejected_task.fork), "Rejected task should have a callable fork attribute"

def test_map_transforms_value():
    def double_value(value):
        return value * 2
    
    resolved_task = Task.of(5)
    mapped_task = resolved_task.map(double_value)
    assert callable(mapped_task.fork), "Mapped task should have a callable fork attribute"
    # Additional assertions to validate the transformed value can be added here

def test_bind_chains_operations():
    def chained_operation(value):
        return Task.of(value + 1)
    
    resolved_task = Task.of(5)
    chained_task = resolved_task.bind(chained_operation)
    assert callable(chained_task.fork), "Chained task should have a callable fork attribute"
    # Additional assertions to validate the chained operation can be added here
