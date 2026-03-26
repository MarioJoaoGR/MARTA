
import pytest
from flutes.exception import exception_wrapper, log_exception

def test_edge_cases():
    # Test None handler function
    @exception_wrapper(None)
    def func_none(*args):
        raise ValueError("Test exception")
    
    with pytest.raises(ValueError):
        func_none()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_exception_exception_wrapper_1_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        # Test None handler function
        @exception_wrapper(None)
        def func_none(*args):
            raise ValueError("Test exception")
    
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

flutes/Test4DT_tests/test_flutes_exception_exception_wrapper_1_test_edge_cases.py:11: Failed
----------------------------- Captured stdout call -----------------------------
[2026-03-24 18:37:00] Traceback (most recent call last):
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/exception.py", line 152, in wrapped
    result = func(*args, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^
  File "/projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_exception_exception_wrapper_1_test_edge_cases.py", line 9, in func_none
    raise ValueError("Test exception")
ValueError: Test exception

[2026-03-24 18:37:00] <ValueError> Test exception
------------------------------ Captured log call -------------------------------
ERROR    flutes.log:log.py:182 Traceback (most recent call last):
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/exception.py", line 152, in wrapped
    result = func(*args, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^
  File "/projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_exception_exception_wrapper_1_test_edge_cases.py", line 9, in func_none
    raise ValueError("Test exception")
ValueError: Test exception

ERROR    flutes.log:log.py:182 <ValueError> Test exception
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_exception_exception_wrapper_1_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.09s ===============================
"""