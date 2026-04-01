
import pytest
from flutes.exception import exception_wrapper

def test_invalid_input():
    @exception_wrapper()
    def foo(one, two, *args, three=None, **kwargs):
        raise ValueError("Test error")
    
    with pytest.raises(ValueError) as excinfo:
        foo(1, "2", "arg1", "arg2", four=4)
    
    assert str(excinfo.value) == "Test error"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_exception_exception_wrapper_0_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        @exception_wrapper()
        def foo(one, two, *args, three=None, **kwargs):
            raise ValueError("Test error")
    
>       with pytest.raises(ValueError) as excinfo:
E       Failed: DID NOT RAISE <class 'ValueError'>

flutes/Test4DT_tests/test_flutes_exception_exception_wrapper_0_test_invalid_input.py:10: Failed
----------------------------- Captured stdout call -----------------------------
[2026-03-19 18:30:41] Traceback (most recent call last):
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/exception.py", line 152, in wrapped
    result = func(*args, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^
  File "/projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_exception_exception_wrapper_0_test_invalid_input.py", line 8, in foo
    raise ValueError("Test error")
ValueError: Test error

[2026-03-19 18:30:41] <ValueError> Test error
------------------------------ Captured log call -------------------------------
ERROR    flutes.log:log.py:182 Traceback (most recent call last):
  File "/projects/F202407648IACDCF2/mario/flutes/flutes/exception.py", line 152, in wrapped
    result = func(*args, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^
  File "/projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_exception_exception_wrapper_0_test_invalid_input.py", line 8, in foo
    raise ValueError("Test error")
ValueError: Test error

ERROR    flutes.log:log.py:182 <ValueError> Test error
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_exception_exception_wrapper_0_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.08s ===============================

"""