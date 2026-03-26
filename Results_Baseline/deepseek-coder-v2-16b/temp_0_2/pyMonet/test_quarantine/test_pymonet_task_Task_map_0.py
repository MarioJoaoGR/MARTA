
import pytest
from pymonet.task import Task

# Test instantiating a Task object with a fork function that resolves successfully
def test_instantiate_task():
    def my_fork(reject, resolve):
        resolve("success")
    
    task = Task(my_fork)
    assert task.fork() == "success"

# Test using the map method to transform the resolved value of a Task
def test_map_method():
    def my_mapper(value):
        return value * 2
    
    task = Task(lambda reject, resolve: resolve(42))
    new_task = task.map(my_mapper)
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pyMonet
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

pyMonet/Test4DT_tests/test_pymonet_task_Task_map_0.py F.                 [100%]

=================================== FAILURES ===================================
____________________________ test_instantiate_task _____________________________

    def test_instantiate_task():
        def my_fork(reject, resolve):
            resolve("success")
    
        task = Task(my_fork)
>       assert task.fork() == "success"
E       TypeError: test_instantiate_task.<locals>.my_fork() missing 2 required positional arguments: 'reject' and 'resolve'

pyMonet/Test4DT_tests/test_pymonet_task_Task_map_0.py:11: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_task_Task_map_0.py::test_instantiate_task
========================= 1 failed, 1 passed in 0.06s ==========================
"""