
import pytest
from pymonet.task import Task

@pytest.fixture
def task():
    def my_fork(reject, resolve):
        pass
    return Task(my_fork)

def test_valid_inputs(task):
    rejected_task = task.reject("Error message")
    assert isinstance(rejected_task, Task)
    assert rejected_task.fork.__name__ == "reject"

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

pyMonet/Test4DT_tests/test_pymonet_task_Task_reject_2_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

task = <pymonet.task.Task object at 0x7f135770fa50>

    def test_valid_inputs(task):
        rejected_task = task.reject("Error message")
        assert isinstance(rejected_task, Task)
>       assert rejected_task.fork.__name__ == "reject"
E       AssertionError: assert '<lambda>' == 'reject'
E         
E         - reject
E         + <lambda>

pyMonet/Test4DT_tests/test_pymonet_task_Task_reject_2_test_valid_inputs.py:14: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_task_Task_reject_2_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.08s ===============================
"""