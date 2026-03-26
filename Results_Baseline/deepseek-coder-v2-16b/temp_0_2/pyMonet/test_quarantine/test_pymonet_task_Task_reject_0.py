
import pytest
from pymonet.task import Task

# Test creating a resolved Task
def test_create_resolved_task():
    def my_fork(reject, resolve):
        resolve("Success!")
    
    task = Task(my_fork)
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

pyMonet/Test4DT_tests/test_pymonet_task_Task_reject_0.py F.              [100%]

=================================== FAILURES ===================================
__________________________ test_create_resolved_task ___________________________

    def test_create_resolved_task():
        def my_fork(reject, resolve):
            resolve("Success!")
    
        task = Task(my_fork)
>       assert task.fork(lambda x: f"Rejected: {x}", lambda x: f"Resolved: {x}") == "Resolved: Success!", "Task should be resolved with 'Success!'"
E       AssertionError: Task should be resolved with 'Success!'
E       assert None == 'Resolved: Success!'
E        +  where None = <function test_create_resolved_task.<locals>.my_fork at 0x7fb95f6b4d60>(<function test_create_resolved_task.<locals>.<lambda> at 0x7fb95f6b4ae0>, <function test_create_resolved_task.<locals>.<lambda> at 0x7fb95f6b5300>)
E        +    where <function test_create_resolved_task.<locals>.my_fork at 0x7fb95f6b4d60> = <pymonet.task.Task object at 0x7fb95f65e610>.fork

pyMonet/Test4DT_tests/test_pymonet_task_Task_reject_0.py:11: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_task_Task_reject_0.py::test_create_resolved_task
========================= 1 failed, 1 passed in 0.06s ==========================
"""