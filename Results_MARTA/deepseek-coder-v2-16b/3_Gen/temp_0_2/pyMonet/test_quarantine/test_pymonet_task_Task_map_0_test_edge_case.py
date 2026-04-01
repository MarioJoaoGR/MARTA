
import pytest
from pymonet.task import Task

def test_edge_case():
    # Test edge case with None input for fork function and empty map function
    task = Task(lambda reject, resolve: reject("Error"))  # Initialize a rejected task
    
    # Attempt to map an empty function (should not change the task)
    mapped_task = task.map(lambda x: x)
    
    # Execute the original task and assert it is in the rejected state
    with pytest.raises(Exception):
        task.fork(lambda err: print(f"Rejected: {err}"), lambda res: print(f"Resolved: {res}"))
    
    # Execute the mapped task and assert it remains in the rejected state
    with pytest.raises(Exception):
        mapped_task.fork(lambda err: print(f"Rejected: {err}"), lambda res: print(f"Resolved: {res}"))

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

pyMonet/Test4DT_tests/test_pymonet_task_Task_map_0_test_edge_case.py F   [100%]

=================================== FAILURES ===================================
________________________________ test_edge_case ________________________________

    def test_edge_case():
        # Test edge case with None input for fork function and empty map function
        task = Task(lambda reject, resolve: reject("Error"))  # Initialize a rejected task
    
        # Attempt to map an empty function (should not change the task)
        mapped_task = task.map(lambda x: x)
    
        # Execute the original task and assert it is in the rejected state
>       with pytest.raises(Exception):
E       Failed: DID NOT RAISE <class 'Exception'>

pyMonet/Test4DT_tests/test_pymonet_task_Task_map_0_test_edge_case.py:13: Failed
----------------------------- Captured stdout call -----------------------------
Rejected: Error
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_task_Task_map_0_test_edge_case.py::test_edge_case
============================== 1 failed in 0.08s ===============================
"""