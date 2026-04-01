
import pytest
from flutes.exception import exception_wrapper

def handler_fn(e, three, one, args, my_arg=None, **kw):
    pass

@pytest.fixture
def wrapper():
    return exception_wrapper(handler_fn)

def test_valid_case(wrapper):
    @wrapper
    def foo(one, two, *args, three=None, **kwargs):
        raise ValueError("Test error")
    
    with pytest.raises(ValueError):
        foo(1, "2", "arg1", "arg2", four=4)

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

flutes/Test4DT_tests/test_flutes_exception_exception_wrapper_0_test_valid_case.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_case ________________________________

wrapper = <function exception_wrapper.<locals>.decorator at 0x7f375bb5f880>

    def test_valid_case(wrapper):
        @wrapper
        def foo(one, two, *args, three=None, **kwargs):
            raise ValueError("Test error")
    
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

flutes/Test4DT_tests/test_flutes_exception_exception_wrapper_0_test_valid_case.py:17: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_exception_exception_wrapper_0_test_valid_case.py::test_valid_case
============================== 1 failed in 0.10s ===============================
"""