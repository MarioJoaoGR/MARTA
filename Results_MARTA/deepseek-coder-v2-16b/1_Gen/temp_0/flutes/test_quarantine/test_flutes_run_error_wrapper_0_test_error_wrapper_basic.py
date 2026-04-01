
import subprocess
from unittest.mock import MagicMock
import pytest
from flutes.run import error_wrapper

def test_error_wrapper_basic():
    # Mocking subprocess exceptions
    called_process_error = subprocess.CalledProcessError(returncode=1, cmd=['ls', '-l', '/nonexistent_file'], output=b"Output")
    
    with pytest.raises(subprocess.CalledProcessError):
        raise called_process_error
    
    wrapped_error = error_wrapper(called_process_error)
    assert str(wrapped_error).endswith("Captured output:\n    ls: cannot access '/nonexistent_file': No such file or directory")

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

flutes/Test4DT_tests/test_flutes_run_error_wrapper_0_test_error_wrapper_basic.py F [100%]

=================================== FAILURES ===================================
___________________________ test_error_wrapper_basic ___________________________

    def test_error_wrapper_basic():
        # Mocking subprocess exceptions
        called_process_error = subprocess.CalledProcessError(returncode=1, cmd=['ls', '-l', '/nonexistent_file'], output=b"Output")
    
        with pytest.raises(subprocess.CalledProcessError):
            raise called_process_error
    
        wrapped_error = error_wrapper(called_process_error)
>       assert str(wrapped_error).endswith("Captured output:\n    ls: cannot access '/nonexistent_file': No such file or directory")
E       assert False
E        +  where False = <built-in method endswith of str object at 0x7f3ec6f787b0>("Captured output:\n    ls: cannot access '/nonexistent_file': No such file or directory")
E        +    where <built-in method endswith of str object at 0x7f3ec6f787b0> = "Command '['ls', '-l', '/nonexistent_file']' returned non-zero exit status 1.\nCaptured output:\n    Output".endswith
E        +      where "Command '['ls', '-l', '/nonexistent_file']' returned non-zero exit status 1.\nCaptured output:\n    Output" = str(CalledProcessError())

flutes/Test4DT_tests/test_flutes_run_error_wrapper_0_test_error_wrapper_basic.py:15: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_run_error_wrapper_0_test_error_wrapper_basic.py::test_error_wrapper_basic
============================== 1 failed in 0.08s ===============================
"""