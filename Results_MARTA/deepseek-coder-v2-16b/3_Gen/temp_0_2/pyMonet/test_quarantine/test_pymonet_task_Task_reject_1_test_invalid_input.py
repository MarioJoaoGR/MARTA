
import pytest
from pymonet.task import Task

def test_reject_invalid_input():
    # Test rejecting with None as value
    task = Task.reject(None)
    assert isinstance(task, Task)
    assert callable(task._fork)
    
    # Call the fork function to trigger rejection
    with pytest.raises(TypeError):
        task._fork(lambda x: x, lambda y: y)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_task_Task_reject_1_test_invalid_input
pyMonet/Test4DT_tests/test_pymonet_task_Task_reject_1_test_invalid_input.py:9:20: E1101: Instance of 'Task' has no '_fork' member; maybe 'fork'? (no-member)
pyMonet/Test4DT_tests/test_pymonet_task_Task_reject_1_test_invalid_input.py:13:8: E1101: Instance of 'Task' has no '_fork' member; maybe 'fork'? (no-member)


"""