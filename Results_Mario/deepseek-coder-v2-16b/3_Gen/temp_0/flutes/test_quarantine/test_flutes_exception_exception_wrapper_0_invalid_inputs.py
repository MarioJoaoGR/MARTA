
import pytest
from flutes.exception import exception_wrapper
import inspect

@pytest.mark.parametrize("invalid_input", [
    None,  # Invalid type: not a callable
    123,   # Invalid type: not a callable
    "",    # Invalid type: not a callable
])
def test_exception_wrapper_invalid_handler(invalid_input):
    """Test that exception_wrapper raises ValueError when the provided handler is not callable."""
    with pytest.raises(ValueError) as excinfo:
        @exception_wrapper(invalid_input)
        def dummy_function():
            pass
    
    assert str(excinfo.value) == "Exception handler must have a positional argument for the exception object"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

flutes/Test4DT_tests/test_flutes_exception_exception_wrapper_0_invalid_inputs.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_________________ test_exception_wrapper_invalid_handler[None] _________________

invalid_input = None

    @pytest.mark.parametrize("invalid_input", [
        None,  # Invalid type: not a callable
        123,   # Invalid type: not a callable
        "",    # Invalid type: not a callable
    ])
    def test_exception_wrapper_invalid_handler(invalid_input):
        """Test that exception_wrapper raises ValueError when the provided handler is not callable."""
>       with pytest.raises(ValueError) as excinfo:
E       Failed: DID NOT RAISE <class 'ValueError'>

flutes/Test4DT_tests/test_flutes_exception_exception_wrapper_0_invalid_inputs.py:13: Failed
_________________ test_exception_wrapper_invalid_handler[123] __________________

func = 123

    def getfullargspec(func):
        """Get the names and default values of a callable object's parameters.
    
        A tuple of seven things is returned:
        (args, varargs, varkw, defaults, kwonlyargs, kwonlydefaults, annotations).
        'args' is a list of the parameter names.
        'varargs' and 'varkw' are the names of the * and ** parameters or None.
        'defaults' is an n-tuple of the default values of the last n parameters.
        'kwonlyargs' is a list of keyword-only parameter names.
        'kwonlydefaults' is a dictionary mapping names from kwonlyargs to defaults.
        'annotations' is a dictionary mapping parameter names to annotations.
    
        Notable differences from inspect.signature():
          - the "self" parameter is always reported, even for bound methods
          - wrapper chains defined by __wrapped__ *not* unwrapped automatically
        """
        try:
            # Re: `skip_bound_arg=False`
            #
            # There is a notable difference in behaviour between getfullargspec
            # and Signature: the former always returns 'self' parameter for bound
            # methods, whereas the Signature always shows the actual calling
            # signature of the passed object.
            #
            # To simulate this behaviour, we "unbind" bound methods, to trick
            # inspect.signature to always return their first parameter ("self",
            # usually)
    
            # Re: `follow_wrapper_chains=False`
            #
            # getfullargspec() historically ignored __wrapped__ attributes,
            # so we ensure that remains the case in 3.3+
    
>           sig = _signature_from_callable(func,
                                           follow_wrapper_chains=False,
                                           skip_bound_arg=False,
                                           sigcls=Signature,
                                           eval_str=False)

/usr/local/lib/python3.11/inspect.py:1365: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

obj = 123

    def _signature_from_callable(obj, *,
                                 follow_wrapper_chains=True,
                                 skip_bound_arg=True,
                                 globals=None,
                                 locals=None,
                                 eval_str=False,
                                 sigcls):
    
        """Private helper function to get signature for arbitrary
        callable objects.
        """
    
        _get_signature_of = functools.partial(_signature_from_callable,
                                    follow_wrapper_chains=follow_wrapper_chains,
                                    skip_bound_arg=skip_bound_arg,
                                    globals=globals,
                                    locals=locals,
                                    sigcls=sigcls,
                                    eval_str=eval_str)
    
        if not callable(obj):
>           raise TypeError('{!r} is not a callable object'.format(obj))
E           TypeError: 123 is not a callable object

/usr/local/lib/python3.11/inspect.py:2456: TypeError

The above exception was the direct cause of the following exception:

invalid_input = 123

    @pytest.mark.parametrize("invalid_input", [
        None,  # Invalid type: not a callable
        123,   # Invalid type: not a callable
        "",    # Invalid type: not a callable
    ])
    def test_exception_wrapper_invalid_handler(invalid_input):
        """Test that exception_wrapper raises ValueError when the provided handler is not callable."""
        with pytest.raises(ValueError) as excinfo:
>           @exception_wrapper(invalid_input)

flutes/Test4DT_tests/test_flutes_exception_exception_wrapper_0_invalid_inputs.py:14: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
flutes/flutes/exception.py:107: in decorator
    handler_argspec = inspect.getfullargspec(_unwrap(handler_fn))
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

func = 123

    def getfullargspec(func):
        """Get the names and default values of a callable object's parameters.
    
        A tuple of seven things is returned:
        (args, varargs, varkw, defaults, kwonlyargs, kwonlydefaults, annotations).
        'args' is a list of the parameter names.
        'varargs' and 'varkw' are the names of the * and ** parameters or None.
        'defaults' is an n-tuple of the default values of the last n parameters.
        'kwonlyargs' is a list of keyword-only parameter names.
        'kwonlydefaults' is a dictionary mapping names from kwonlyargs to defaults.
        'annotations' is a dictionary mapping parameter names to annotations.
    
        Notable differences from inspect.signature():
          - the "self" parameter is always reported, even for bound methods
          - wrapper chains defined by __wrapped__ *not* unwrapped automatically
        """
        try:
            # Re: `skip_bound_arg=False`
            #
            # There is a notable difference in behaviour between getfullargspec
            # and Signature: the former always returns 'self' parameter for bound
            # methods, whereas the Signature always shows the actual calling
            # signature of the passed object.
            #
            # To simulate this behaviour, we "unbind" bound methods, to trick
            # inspect.signature to always return their first parameter ("self",
            # usually)
    
            # Re: `follow_wrapper_chains=False`
            #
            # getfullargspec() historically ignored __wrapped__ attributes,
            # so we ensure that remains the case in 3.3+
    
            sig = _signature_from_callable(func,
                                           follow_wrapper_chains=False,
                                           skip_bound_arg=False,
                                           sigcls=Signature,
                                           eval_str=False)
        except Exception as ex:
            # Most of the times 'signature' will raise ValueError.
            # But, it can also raise AttributeError, and, maybe something
            # else. So to be fully backwards compatible, we catch all
            # possible exceptions here, and reraise a TypeError.
>           raise TypeError('unsupported callable') from ex
E           TypeError: unsupported callable

/usr/local/lib/python3.11/inspect.py:1375: TypeError
___________________ test_exception_wrapper_invalid_handler[] ___________________

func = ''

    def getfullargspec(func):
        """Get the names and default values of a callable object's parameters.
    
        A tuple of seven things is returned:
        (args, varargs, varkw, defaults, kwonlyargs, kwonlydefaults, annotations).
        'args' is a list of the parameter names.
        'varargs' and 'varkw' are the names of the * and ** parameters or None.
        'defaults' is an n-tuple of the default values of the last n parameters.
        'kwonlyargs' is a list of keyword-only parameter names.
        'kwonlydefaults' is a dictionary mapping names from kwonlyargs to defaults.
        'annotations' is a dictionary mapping parameter names to annotations.
    
        Notable differences from inspect.signature():
          - the "self" parameter is always reported, even for bound methods
          - wrapper chains defined by __wrapped__ *not* unwrapped automatically
        """
        try:
            # Re: `skip_bound_arg=False`
            #
            # There is a notable difference in behaviour between getfullargspec
            # and Signature: the former always returns 'self' parameter for bound
            # methods, whereas the Signature always shows the actual calling
            # signature of the passed object.
            #
            # To simulate this behaviour, we "unbind" bound methods, to trick
            # inspect.signature to always return their first parameter ("self",
            # usually)
    
            # Re: `follow_wrapper_chains=False`
            #
            # getfullargspec() historically ignored __wrapped__ attributes,
            # so we ensure that remains the case in 3.3+
    
>           sig = _signature_from_callable(func,
                                           follow_wrapper_chains=False,
                                           skip_bound_arg=False,
                                           sigcls=Signature,
                                           eval_str=False)

/usr/local/lib/python3.11/inspect.py:1365: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

obj = ''

    def _signature_from_callable(obj, *,
                                 follow_wrapper_chains=True,
                                 skip_bound_arg=True,
                                 globals=None,
                                 locals=None,
                                 eval_str=False,
                                 sigcls):
    
        """Private helper function to get signature for arbitrary
        callable objects.
        """
    
        _get_signature_of = functools.partial(_signature_from_callable,
                                    follow_wrapper_chains=follow_wrapper_chains,
                                    skip_bound_arg=skip_bound_arg,
                                    globals=globals,
                                    locals=locals,
                                    sigcls=sigcls,
                                    eval_str=eval_str)
    
        if not callable(obj):
>           raise TypeError('{!r} is not a callable object'.format(obj))
E           TypeError: '' is not a callable object

/usr/local/lib/python3.11/inspect.py:2456: TypeError

The above exception was the direct cause of the following exception:

invalid_input = ''

    @pytest.mark.parametrize("invalid_input", [
        None,  # Invalid type: not a callable
        123,   # Invalid type: not a callable
        "",    # Invalid type: not a callable
    ])
    def test_exception_wrapper_invalid_handler(invalid_input):
        """Test that exception_wrapper raises ValueError when the provided handler is not callable."""
        with pytest.raises(ValueError) as excinfo:
>           @exception_wrapper(invalid_input)

flutes/Test4DT_tests/test_flutes_exception_exception_wrapper_0_invalid_inputs.py:14: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
flutes/flutes/exception.py:107: in decorator
    handler_argspec = inspect.getfullargspec(_unwrap(handler_fn))
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

func = ''

    def getfullargspec(func):
        """Get the names and default values of a callable object's parameters.
    
        A tuple of seven things is returned:
        (args, varargs, varkw, defaults, kwonlyargs, kwonlydefaults, annotations).
        'args' is a list of the parameter names.
        'varargs' and 'varkw' are the names of the * and ** parameters or None.
        'defaults' is an n-tuple of the default values of the last n parameters.
        'kwonlyargs' is a list of keyword-only parameter names.
        'kwonlydefaults' is a dictionary mapping names from kwonlyargs to defaults.
        'annotations' is a dictionary mapping parameter names to annotations.
    
        Notable differences from inspect.signature():
          - the "self" parameter is always reported, even for bound methods
          - wrapper chains defined by __wrapped__ *not* unwrapped automatically
        """
        try:
            # Re: `skip_bound_arg=False`
            #
            # There is a notable difference in behaviour between getfullargspec
            # and Signature: the former always returns 'self' parameter for bound
            # methods, whereas the Signature always shows the actual calling
            # signature of the passed object.
            #
            # To simulate this behaviour, we "unbind" bound methods, to trick
            # inspect.signature to always return their first parameter ("self",
            # usually)
    
            # Re: `follow_wrapper_chains=False`
            #
            # getfullargspec() historically ignored __wrapped__ attributes,
            # so we ensure that remains the case in 3.3+
    
            sig = _signature_from_callable(func,
                                           follow_wrapper_chains=False,
                                           skip_bound_arg=False,
                                           sigcls=Signature,
                                           eval_str=False)
        except Exception as ex:
            # Most of the times 'signature' will raise ValueError.
            # But, it can also raise AttributeError, and, maybe something
            # else. So to be fully backwards compatible, we catch all
            # possible exceptions here, and reraise a TypeError.
>           raise TypeError('unsupported callable') from ex
E           TypeError: unsupported callable

/usr/local/lib/python3.11/inspect.py:1375: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_exception_exception_wrapper_0_invalid_inputs.py::test_exception_wrapper_invalid_handler[None]
FAILED flutes/Test4DT_tests/test_flutes_exception_exception_wrapper_0_invalid_inputs.py::test_exception_wrapper_invalid_handler[123]
FAILED flutes/Test4DT_tests/test_flutes_exception_exception_wrapper_0_invalid_inputs.py::test_exception_wrapper_invalid_handler[]
============================== 3 failed in 0.22s ===============================

"""