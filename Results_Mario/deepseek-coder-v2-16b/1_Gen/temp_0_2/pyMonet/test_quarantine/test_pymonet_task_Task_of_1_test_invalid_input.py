
import pytest
from pymonet.task import Task

def test_invalid_input():
    with pytest.raises(TypeError):
        Task.of()  # This should raise TypeError because of missing argument 'value'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pymonet_task_Task_of_1_test_invalid_input
pyMonet/Test4DT_tests/test_pymonet_task_Task_of_1_test_invalid_input.py:7:8: E1120: No value for argument 'value' in classmethod call (no-value-for-parameter)


"""