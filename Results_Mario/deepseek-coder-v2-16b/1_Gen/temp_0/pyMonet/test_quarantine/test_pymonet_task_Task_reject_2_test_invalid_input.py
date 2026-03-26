
from pymonet.task import Task

class TestTaskReject:
    def test_reject_invalid_input(self):
        # Test that reject method raises a TypeError when given an invalid input type
        try:
            rejected_task = Task.reject("invalid input")
            assert False, "Expected TypeError but no exception was raised"
        except TypeError as e:
            assert str(e) == "__init__() missing 1 required positional argument: 'fork'", f"Unexpected error: {str(e)}"

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

pyMonet/Test4DT_tests/test_pymonet_task_Task_reject_2_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
___________________ TestTaskReject.test_reject_invalid_input ___________________

self = <Test4DT_tests.test_pymonet_task_Task_reject_2_test_invalid_input.TestTaskReject object at 0x7f82b981b910>

    def test_reject_invalid_input(self):
        # Test that reject method raises a TypeError when given an invalid input type
        try:
            rejected_task = Task.reject("invalid input")
>           assert False, "Expected TypeError but no exception was raised"
E           AssertionError: Expected TypeError but no exception was raised
E           assert False

pyMonet/Test4DT_tests/test_pymonet_task_Task_reject_2_test_invalid_input.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_task_Task_reject_2_test_invalid_input.py::TestTaskReject::test_reject_invalid_input
============================== 1 failed in 0.07s ===============================
"""