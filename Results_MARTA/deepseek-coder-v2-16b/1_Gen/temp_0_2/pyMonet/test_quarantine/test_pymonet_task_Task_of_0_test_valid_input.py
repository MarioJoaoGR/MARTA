
from unittest.mock import Mock
import pytest
from pymonet.task import Task

def test_valid_input():
    # Create a mock fork function that returns a fixed value
    mock_fork = Mock()
    mock_fork.return_value = "resolved"
    
    # Create a task with the mock fork function
    task = Task.of("test_value")
    
    # Call the fork method of the task
    result = task.fork(lambda _: None, lambda x: x)
    
    # Assert that the result is as expected
    assert result == "resolved"

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
        # Create a mock fork function that returns a fixed value
        mock_fork = Mock()
        mock_fork.return_value = "resolved"
    
        # Create a task with the mock fork function
        task = Task.of("test_value")
    
        # Call the fork method of the task
        result = task.fork(lambda _: None, lambda x: x)
    
        # Assert that the result is as expected
>       assert result == "resolved"
E       AssertionError: assert 'test_value' == 'resolved'
E         
E         - resolved
E         + test_value

pyMonet/Test4DT_tests/test_pymonet_task_Task_of_0_test_valid_input.py:18: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_task_Task_of_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.06s ===============================
"""