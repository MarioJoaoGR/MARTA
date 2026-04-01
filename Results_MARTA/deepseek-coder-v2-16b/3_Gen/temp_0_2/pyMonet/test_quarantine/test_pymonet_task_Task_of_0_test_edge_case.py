
from pymonet.task import Task
import pytest

def test_edge_case():
    # Create a resolved task with an edge case value
    task = Task.of(0)
    
    # Assert that the task is indeed a Task instance
    assert isinstance(task, Task)
    
    # Since the task is resolved immediately, we can test its value directly
    assert task._Task__fork is not None  # Check if __fork attribute exists and is not None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_task_Task_of_0_test_edge_case
pyMonet/Test4DT_tests/test_pymonet_task_Task_of_0_test_edge_case.py:13:11: E1101: Instance of 'Task' has no '_Task__fork' member (no-member)


"""