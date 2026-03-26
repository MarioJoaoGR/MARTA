
# Module: pymonet.task
import pytest
from pymonet.task import Task

# Test basic task creation
def test_basic_task_creation():
    def my_fork(reject, resolve):
        resolve("success")
    
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

pyMonet/Test4DT_tests/test_pymonet_task_Task___init___0.py F.            [100%]

=================================== FAILURES ===================================
___________________________ test_basic_task_creation ___________________________

    def test_basic_task_creation():
        def my_fork(reject, resolve):
            resolve("success")
    
        task = Task(my_fork)
>       assert task.fork(lambda x: f"Rejected: {x}", lambda x: f"Resolved: {x}") == "Resolved: success"
E       AssertionError: assert None == 'Resolved: success'
E        +  where None = <function test_basic_task_creation.<locals>.my_fork at 0x7f674d650d60>(<function test_basic_task_creation.<locals>.<lambda> at 0x7f674d650ae0>, <function test_basic_task_creation.<locals>.<lambda> at 0x7f674d651300>)
E        +    where <function test_basic_task_creation.<locals>.my_fork at 0x7f674d650d60> = <pymonet.task.Task object at 0x7f674d9b53d0>.fork

pyMonet/Test4DT_tests/test_pymonet_task_Task___init___0.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_task_Task___init___0.py::test_basic_task_creation
========================= 1 failed, 1 passed in 0.06s ==========================
"""