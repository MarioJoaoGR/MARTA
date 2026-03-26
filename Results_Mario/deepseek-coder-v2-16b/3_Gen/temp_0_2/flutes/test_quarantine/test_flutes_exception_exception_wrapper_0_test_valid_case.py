
import pytest
from unittest.mock import patch, MagicMock
import inspect
import functools

# Assuming the exception wrapper is defined in the flutes.exception module
from flutes.exception import exception_wrapper

@pytest.fixture(autouse=True)
def mock_handler_fn():
    with patch('flutes.exception.exception_wrapper') as mock_decorator:
        yield mock_decorator

def test_valid_case():
    def handler_fn(e, one, two, *args, my_arg=None, **kwargs):
        assert isinstance(e, ValueError)
        assert one == 1
        assert two == "2"
        assert args == ("arg1", "arg2")
        assert my_arg is None
        assert kwargs == {"four": 4}
    
    @exception_wrapper(handler_fn)
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

    def test_valid_case():
        def handler_fn(e, one, two, *args, my_arg=None, **kwargs):
            assert isinstance(e, ValueError)
            assert one == 1
            assert two == "2"
            assert args == ("arg1", "arg2")
            assert my_arg is None
            assert kwargs == {"four": 4}
    
>       @exception_wrapper(handler_fn)

flutes/Test4DT_tests/test_flutes_exception_exception_wrapper_0_test_valid_case.py:24: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

func = <function test_valid_case.<locals>.foo at 0x7f8269c04f40>

    def decorator(func):
        if handler_fn is not None:
            handler_argspec = inspect.getfullargspec(_unwrap(handler_fn))
            if len(handler_argspec.args) == 0:
                raise ValueError("Exception handler must have a positional argument for the exception object")
            if handler_argspec.varargs is not None:
>               raise ValueError("Exception handler cannot have a varargs argument (*args)")
E               ValueError: Exception handler cannot have a varargs argument (*args)

flutes/flutes/exception.py:111: ValueError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_exception_exception_wrapper_0_test_valid_case.py::test_valid_case
============================== 1 failed in 0.08s ===============================
"""