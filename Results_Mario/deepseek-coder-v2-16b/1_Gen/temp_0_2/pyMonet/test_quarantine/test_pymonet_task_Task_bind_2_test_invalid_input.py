
from pymonet.task import Task

class TestTaskBindInvalidInput:
    def test_invalid_input(self):
        # Create an invalid task by passing None as the fork function
        task = Task(None)
    
        # Attempt to bind a function to the invalid task
        new_task = task.bind(lambda x: Task(lambda _, __: x))
    
        # Check that the new task is still invalid (i.e., it hasn't been bound correctly)
        assert isinstance(new_task, Task)
        assert new_task.fork is None

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

pyMonet/Test4DT_tests/test_pymonet_task_Task_bind_2_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
_________________ TestTaskBindInvalidInput.test_invalid_input __________________

self = <Test4DT_tests.test_pymonet_task_Task_bind_2_test_invalid_input.TestTaskBindInvalidInput object at 0x7f948c093250>

    def test_invalid_input(self):
        # Create an invalid task by passing None as the fork function
        task = Task(None)
    
        # Attempt to bind a function to the invalid task
        new_task = task.bind(lambda x: Task(lambda _, __: x))
    
        # Check that the new task is still invalid (i.e., it hasn't been bound correctly)
        assert isinstance(new_task, Task)
>       assert new_task.fork is None
E       assert <function Task.bind.<locals>.result at 0x7f948c0c0720> is None
E        +  where <function Task.bind.<locals>.result at 0x7f948c0c0720> = <pymonet.task.Task object at 0x7f948c076810>.fork

pyMonet/Test4DT_tests/test_pymonet_task_Task_bind_2_test_invalid_input.py:14: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_task_Task_bind_2_test_invalid_input.py::TestTaskBindInvalidInput::test_invalid_input
============================== 1 failed in 0.06s ===============================
"""