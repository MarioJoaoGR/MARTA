
import subprocess
from unittest.mock import patch, MagicMock
import pytest
from flutes.run import error_wrapper

@pytest.mark.parametrize("err", [subprocess.CalledProcessError(1, "cmd", output=b"output"), subprocess.TimeoutExpired("cmd", timeout=1)])
def test_error_wrapper(err):
    with patch('flutes.run.subprocess') as mock_subprocess:
        # Mock the exception to be returned by subprocess calls
        mock_exception = MagicMock()
        mock_exception.__str__.return_value = "Original Exception Str"

        # Set up the mock to return the mocked exception
        if isinstance(err, subprocess.CalledProcessError):
            mock_subprocess.CalledProcessError = type('CalledProcessError', (Exception,), {'__str__': lambda self: 'Mocked CalledProcessError'})
            mock_exception.__class__ = mock_subprocess.CalledProcessError
        elif isinstance(err, subprocess.TimeoutExpired):
            mock_subprocess.TimeoutExpired = type('TimeoutExpired', (Exception,), {'__str__': lambda self: 'Mocked TimeoutExpired'})
            mock_exception.__class__ = mock_subprocess.TimeoutExpired

        # Call the function under test
        wrapped_err = error_wrapper(mock_exception)

        # Check that the output is correctly captured and formatted
        assert str(wrapped_err) == "Original Exception Str\nCaptured output:\n    output"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

flutes/Test4DT_tests/test_flutes_run_error_wrapper_1_test_invalid_inputs.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
___________________________ test_error_wrapper[err0] ___________________________

err = CalledProcessError(1, 'cmd')

    @pytest.mark.parametrize("err", [subprocess.CalledProcessError(1, "cmd", output=b"output"), subprocess.TimeoutExpired("cmd", timeout=1)])
    def test_error_wrapper(err):
        with patch('flutes.run.subprocess') as mock_subprocess:
            # Mock the exception to be returned by subprocess calls
            mock_exception = MagicMock()
            mock_exception.__str__.return_value = "Original Exception Str"
    
            # Set up the mock to return the mocked exception
            if isinstance(err, subprocess.CalledProcessError):
                mock_subprocess.CalledProcessError = type('CalledProcessError', (Exception,), {'__str__': lambda self: 'Mocked CalledProcessError'})
                mock_exception.__class__ = mock_subprocess.CalledProcessError
            elif isinstance(err, subprocess.TimeoutExpired):
                mock_subprocess.TimeoutExpired = type('TimeoutExpired', (Exception,), {'__str__': lambda self: 'Mocked TimeoutExpired'})
                mock_exception.__class__ = mock_subprocess.TimeoutExpired
    
            # Call the function under test
            wrapped_err = error_wrapper(mock_exception)
    
            # Check that the output is correctly captured and formatted
>           assert str(wrapped_err) == "Original Exception Str\nCaptured output:\n    output"
E           AssertionError: assert 'Original Exception Str' == 'Original Exc...:\n    output'
E             
E             - Original Exception Str
E             ?                       -
E             + Original Exception Str
E             - Captured output:
E             -     output

flutes/Test4DT_tests/test_flutes_run_error_wrapper_1_test_invalid_inputs.py:26: AssertionError
___________________________ test_error_wrapper[err1] ___________________________

err = TimeoutExpired('cmd')

    @pytest.mark.parametrize("err", [subprocess.CalledProcessError(1, "cmd", output=b"output"), subprocess.TimeoutExpired("cmd", timeout=1)])
    def test_error_wrapper(err):
        with patch('flutes.run.subprocess') as mock_subprocess:
            # Mock the exception to be returned by subprocess calls
            mock_exception = MagicMock()
            mock_exception.__str__.return_value = "Original Exception Str"
    
            # Set up the mock to return the mocked exception
            if isinstance(err, subprocess.CalledProcessError):
                mock_subprocess.CalledProcessError = type('CalledProcessError', (Exception,), {'__str__': lambda self: 'Mocked CalledProcessError'})
                mock_exception.__class__ = mock_subprocess.CalledProcessError
            elif isinstance(err, subprocess.TimeoutExpired):
                mock_subprocess.TimeoutExpired = type('TimeoutExpired', (Exception,), {'__str__': lambda self: 'Mocked TimeoutExpired'})
                mock_exception.__class__ = mock_subprocess.TimeoutExpired
    
            # Call the function under test
>           wrapped_err = error_wrapper(mock_exception)

flutes/Test4DT_tests/test_flutes_run_error_wrapper_1_test_invalid_inputs.py:23: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

err = <MagicMock spec='TimeoutExpired' id='139620761109840'>

    def error_wrapper(err: ExcType) -> ExcType:
        r"""Wrap exceptions raised in :py:mod:`subprocess` to output captured output by default.
        """
>       if not isinstance(err, (subprocess.CalledProcessError, subprocess.TimeoutExpired)):
E       TypeError: isinstance() arg 2 must be a type, a tuple of types, or a union

flutes/flutes/run.py:31: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_run_error_wrapper_1_test_invalid_inputs.py::test_error_wrapper[err0]
FAILED flutes/Test4DT_tests/test_flutes_run_error_wrapper_1_test_invalid_inputs.py::test_error_wrapper[err1]
============================== 2 failed in 0.10s ===============================

"""