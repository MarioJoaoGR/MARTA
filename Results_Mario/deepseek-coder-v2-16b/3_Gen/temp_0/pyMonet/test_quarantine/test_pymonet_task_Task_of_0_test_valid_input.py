
import pytest
from pymonet.task import Task

def test_valid_input():
    task = Task.of(42)
    assert task is not None
    assert task.fork({"reject": lambda x: False, "resolve": lambda y: True}) == True

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

pyMonet/Test4DT_tests/test_pymonet_task_Task_of_0_test_valid_input.py F  [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        task = Task.of(42)
        assert task is not None
>       assert task.fork({"reject": lambda x: False, "resolve": lambda y: True}) == True
E       TypeError: Task.of.<locals>.<lambda>() missing 1 required positional argument: 'resolve'

pyMonet/Test4DT_tests/test_pymonet_task_Task_of_0_test_valid_input.py:8: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_task_Task_of_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.06s ===============================
"""