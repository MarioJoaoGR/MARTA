
import subprocess
from flutes.run import error_wrapper, ExcType

def test_valid_inputs():
    # Create a mock exception of type subprocess.CalledProcessError
    err = subprocess.CalledProcessError(returncode=1, cmd=['false'], output='error output'.encode('utf-8'))
    
    # Call the error_wrapper function with the mock exception
    wrapped_err = error_wrapper(err)
    
    assert isinstance(wrapped_err, subprocess.CalledProcessError), "Expected a CalledProcessError"
    assert str(wrapped_err).endswith("Captured output:\nerror output"), "Output string should include captured output"

def test_invalid_input():
    # Create a mock exception of an invalid type
    err = Exception("Test Error")
    
    # Call the error_wrapper function with the mock exception
    wrapped_err = error_wrapper(err)
    
    assert isinstance(wrapped_err, Exception), "Expected an Exception"
    assert str(wrapped_err) == "Test Error", "Original error message should remain unchanged"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

flutes/Test4DT_tests/test_flutes_run_error_wrapper_1_test_valid_inputs.py F [ 50%]
.                                                                        [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        # Create a mock exception of type subprocess.CalledProcessError
        err = subprocess.CalledProcessError(returncode=1, cmd=['false'], output='error output'.encode('utf-8'))
    
        # Call the error_wrapper function with the mock exception
        wrapped_err = error_wrapper(err)
    
        assert isinstance(wrapped_err, subprocess.CalledProcessError), "Expected a CalledProcessError"
>       assert str(wrapped_err).endswith("Captured output:\nerror output"), "Output string should include captured output"
E       AssertionError: Output string should include captured output
E       assert False
E        +  where False = <built-in method endswith of str object at 0x7f086ff65aa0>('Captured output:\nerror output')
E        +    where <built-in method endswith of str object at 0x7f086ff65aa0> = "Command '['false']' returned non-zero exit status 1.\nCaptured output:\n    error output".endswith
E        +      where "Command '['false']' returned non-zero exit status 1.\nCaptured output:\n    error output" = str(CalledProcessError())

flutes/Test4DT_tests/test_flutes_run_error_wrapper_1_test_valid_inputs.py:13: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_run_error_wrapper_1_test_valid_inputs.py::test_valid_inputs
========================= 1 failed, 1 passed in 0.12s ==========================
"""