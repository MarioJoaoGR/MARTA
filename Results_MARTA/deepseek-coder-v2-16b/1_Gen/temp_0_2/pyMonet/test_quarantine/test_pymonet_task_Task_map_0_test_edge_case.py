
import pytest
from pymonet.task import Task

def test_edge_case():
    # Create a task with an edge case value
    task = Task(lambda reject, resolve: resolve(42))
    
    # Define a mapper function that adds one to the input
    def add_one(x):
        return x + 1
    
    # Apply the map function and get the new task
    new_task = task.map(add_one)
    
    # Check if the new task's fork function correctly applies the mapper function
    assert new_task.fork(reject=lambda e: None, resolve=print) == 43

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pyMonet
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

pyMonet/Test4DT_tests/test_pymonet_task_Task_map_0_test_edge_case.py F   [100%]

=================================== FAILURES ===================================
________________________________ test_edge_case ________________________________

    def test_edge_case():
        # Create a task with an edge case value
        task = Task(lambda reject, resolve: resolve(42))
    
        # Define a mapper function that adds one to the input
        def add_one(x):
            return x + 1
    
        # Apply the map function and get the new task
        new_task = task.map(add_one)
    
        # Check if the new task's fork function correctly applies the mapper function
>       assert new_task.fork(reject=lambda e: None, resolve=print) == 43
E       assert None == 43
E        +  where None = <function Task.map.<locals>.result at 0x7fa3ba4a5ee0>(reject=<function test_edge_case.<locals>.<lambda> at 0x7fa3ba4a4d60>, resolve=print)
E        +    where <function Task.map.<locals>.result at 0x7fa3ba4a5ee0> = <pymonet.task.Task object at 0x7fa3ba462550>.fork

pyMonet/Test4DT_tests/test_pymonet_task_Task_map_0_test_edge_case.py:17: AssertionError
----------------------------- Captured stdout call -----------------------------
43
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_task_Task_map_0_test_edge_case.py::test_edge_case
============================== 1 failed in 0.07s ===============================
"""