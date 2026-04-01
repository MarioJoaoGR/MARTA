
from pymonet.task import Task
import pytest

def test_reject():
    # Test if a rejected task is created correctly with the provided value
    value = "error"
    rejected_task = Task.reject(value)
    
    # Check that the task is indeed rejected by asserting the type of the result when calling it
    with pytest.raises(Exception):
        rejected_task._Task__fork("unexpected reject call", lambda x: x)  # This should raise an error because we're not resolving anything

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_task_Task_reject_1_test_edge_case
pyMonet/Test4DT_tests/test_pymonet_task_Task_reject_1_test_edge_case.py:12:8: E1101: Instance of 'Task' has no '_Task__fork' member (no-member)


"""