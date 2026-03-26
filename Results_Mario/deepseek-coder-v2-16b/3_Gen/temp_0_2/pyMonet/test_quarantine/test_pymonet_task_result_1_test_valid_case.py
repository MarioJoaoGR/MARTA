
import pytest
from pymonet.task import Task

def test_valid_case():
    def handle_success(result):
        assert result == "Success"
    
    def handle_failure(error):
        pytest.fail("Unexpected failure: {}".format(error))
    
    # Mocking a successful computation
    success_task = Task(lambda resolve, reject: resolve("Success"))
    
    # Using the result function to handle the task
    success_task.fork(handle_failure, handle_success)

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

pyMonet/Test4DT_tests/test_pymonet_task_result_1_test_valid_case.py F    [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_case ________________________________

    def test_valid_case():
        def handle_success(result):
            assert result == "Success"
    
        def handle_failure(error):
            pytest.fail("Unexpected failure: {}".format(error))
    
        # Mocking a successful computation
        success_task = Task(lambda resolve, reject: resolve("Success"))
    
        # Using the result function to handle the task
>       success_task.fork(handle_failure, handle_success)

pyMonet/Test4DT_tests/test_pymonet_task_result_1_test_valid_case.py:16: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pyMonet/Test4DT_tests/test_pymonet_task_result_1_test_valid_case.py:13: in <lambda>
    success_task = Task(lambda resolve, reject: resolve("Success"))
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

error = 'Success'

    def handle_failure(error):
>       pytest.fail("Unexpected failure: {}".format(error))
E       Failed: Unexpected failure: Success

pyMonet/Test4DT_tests/test_pymonet_task_result_1_test_valid_case.py:10: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_task_result_1_test_valid_case.py::test_valid_case
============================== 1 failed in 0.08s ===============================
"""