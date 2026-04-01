
from pymonet.task import Task

def test_valid_input():
    def my_function(reject, resolve):
        resolve(5)
    
    task = Task(my_function)
    mapped_task = task.map(lambda x: x * 2)
    
    # Execute the original task to get its result
    result = task.fork(lambda err: None, lambda res: res)
    assert result == 5

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
        def my_function(reject, resolve):
            resolve(5)
    
        task = Task(my_function)
        mapped_task = task.map(lambda x: x * 2)
    
        # Execute the original task to get its result
        result = task.fork(lambda err: None, lambda res: res)
>       assert result == 5
E       assert None == 5

pyMonet/Test4DT_tests/test_pymonet_task_Task_map_0_test_valid_input.py:13: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_task_Task_map_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.07s ===============================
"""