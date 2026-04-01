
import pytest
from flutes.exception import exception_wrapper

@pytest.fixture
def setup():
    # Setup code here (if any)
    pass

@pytest.mark.parametrize("raise_error", [False, True])
def test_exception_wrapper(setup, raise_error):
    @exception_wrapper() if not raise_error else exception_wrapper(handler_fn=lambda e: None)
    def func_to_test():
        if raise_error:
            raise ValueError("Test error")

    with pytest.raises(ValueError) if raise_error else None:
        func_to_test()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

flutes/Test4DT_tests/test_flutes_exception_exception_wrapper_0_edge_cases.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
________________________ test_exception_wrapper[False] _________________________

setup = None, raise_error = False

    @pytest.mark.parametrize("raise_error", [False, True])
    def test_exception_wrapper(setup, raise_error):
        @exception_wrapper() if not raise_error else exception_wrapper(handler_fn=lambda e: None)
        def func_to_test():
            if raise_error:
                raise ValueError("Test error")
    
>       with pytest.raises(ValueError) if raise_error else None:
E       TypeError: 'NoneType' object does not support the context manager protocol

flutes/Test4DT_tests/test_flutes_exception_exception_wrapper_0_edge_cases.py:17: TypeError
_________________________ test_exception_wrapper[True] _________________________

setup = None, raise_error = True

    @pytest.mark.parametrize("raise_error", [False, True])
    def test_exception_wrapper(setup, raise_error):
        @exception_wrapper() if not raise_error else exception_wrapper(handler_fn=lambda e: None)
        def func_to_test():
            if raise_error:
                raise ValueError("Test error")
    
>       with pytest.raises(ValueError) if raise_error else None:
E       Failed: DID NOT RAISE <class 'ValueError'>

flutes/Test4DT_tests/test_flutes_exception_exception_wrapper_0_edge_cases.py:17: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_exception_exception_wrapper_0_edge_cases.py::test_exception_wrapper[False]
FAILED flutes/Test4DT_tests/test_flutes_exception_exception_wrapper_0_edge_cases.py::test_exception_wrapper[True]
============================== 2 failed in 0.09s ===============================

"""