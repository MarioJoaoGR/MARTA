
import pytest
from pymonet.task import Task

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_task_Task_map_0.py F [100%]

=================================== FAILURES ===================================
________________________________ test_task_map _________________________________

    def test_task_map():
        def my_function(reject, resolve):
            resolve("Success")
    
        task = Task(my_function)
    
        def double_value(x):
            return x * 2
    
        mapped_task = task.map(double_value)
        result = None
        error = None
    
        def reject(err):
            nonlocal error
            error = err
    
        def resolve(res):
            nonlocal result
            result = res
    
        mapped_task.fork(reject, resolve)
>       assert result == "Success", "Task should call the function and resolve with 'Success'"
E       AssertionError: Task should call the function and resolve with 'Success'
E       assert 'SuccessSuccess' == 'Success'
E         
E         - Success
E         + SuccessSuccess

/opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_task_Task_map_0.py:27: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_task_Task_map_0.py::test_task_map
============================== 1 failed in 0.05s ===============================
"""