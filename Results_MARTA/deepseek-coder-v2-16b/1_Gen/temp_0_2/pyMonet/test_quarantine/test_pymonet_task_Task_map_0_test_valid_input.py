
import pytest
from pymonet.task import Task

def test_valid_input():
    task = Task(lambda reject, resolve: resolve(42))
    new_task = task.map(lambda x: x + 1)
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

pyMonet/Test4DT_tests/test_pymonet_task_Task_map_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        task = Task(lambda reject, resolve: resolve(42))
        new_task = task.map(lambda x: x + 1)
>       assert new_task.fork(reject=lambda e: None, resolve=print) == 43
E       assert None == 43
E        +  where None = <function Task.map.<locals>.result at 0x7f5d71788c20>(reject=<function test_valid_input.<locals>.<lambda> at 0x7f5d717899e0>, resolve=print)
E        +    where <function Task.map.<locals>.result at 0x7f5d71788c20> = <pymonet.task.Task object at 0x7f5d71ca6210>.fork

pyMonet/Test4DT_tests/test_pymonet_task_Task_map_0_test_valid_input.py:8: AssertionError
----------------------------- Captured stdout call -----------------------------
43
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_task_Task_map_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.06s ===============================
"""