
from pymonet.task import Task

def test_valid_input():
    def mock_fork(reject, resolve):
        # Mock implementation of fork function
        resolve("initial value")
    
    def valid_mapper(value):
        return value + 10
    
    task = Task(mock_fork)
    mapped_task = task.map(valid_mapper)
    
    # Expected result after mapping
    expected_result = "initial value" + str(10)
    assert mapped_task.fork == expected_result

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
        def mock_fork(reject, resolve):
            # Mock implementation of fork function
            resolve("initial value")
    
        def valid_mapper(value):
            return value + 10
    
        task = Task(mock_fork)
        mapped_task = task.map(valid_mapper)
    
        # Expected result after mapping
        expected_result = "initial value" + str(10)
>       assert mapped_task.fork == expected_result
E       AssertionError: assert <function Task.map.<locals>.result at 0x7f0faa3b9580> == 'initial value10'
E        +  where <function Task.map.<locals>.result at 0x7f0faa3b9580> = <pymonet.task.Task object at 0x7f0faa3acd90>.fork

pyMonet/Test4DT_tests/test_pymonet_task_Task_map_0_test_valid_input.py:17: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_task_Task_map_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.06s ===============================
"""