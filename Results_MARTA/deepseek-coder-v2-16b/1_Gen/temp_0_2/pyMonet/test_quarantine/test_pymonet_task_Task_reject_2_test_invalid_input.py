
import pytest
from pymonet.task import Task

def test_reject():
    value = "error"
    rejected_task = Task.reject(value)
    assert isinstance(rejected_task, Task)
    assert rejected_task._Task__fork("mock_reject", "mock_resolve") == value

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_task_Task_reject_2_test_invalid_input
pyMonet/Test4DT_tests/test_pymonet_task_Task_reject_2_test_invalid_input.py:9:11: E1101: Instance of 'Task' has no '_Task__fork' member (no-member)


"""