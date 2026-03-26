
import pytest
from flutes.run import error_wrapper
import subprocess

@pytest.fixture
def called_process_error():
    try:
        result = subprocess.run(['ls', '-l', '/nonexistent_file'], check=True, capture_output=True)
    except subprocess.CalledProcessError as e:
        return e

@pytest.fixture
def timeout_expired():
    with pytest.raises(subprocess.TimeoutExpired):
        result = subprocess.run(['sleep', '10'], timeout=1, capture_output=True)

def test_error_wrapper_basic(called_process_error, timeout_expired):
    wrapped_e = error_wrapper(called_process_error)
    assert "No such file or directory" in str(wrapped_e)
    assert "Captured output:" in str(wrapped_e)

def test_error_wrapper_timeout(timeout_expired):
    with pytest.raises(subprocess.TimeoutExpired) as excinfo:
        wrapped_e = error_wrapper(excinfo.value)
        assert "Command timed out" in str(wrapped_e)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

flutes/Test4DT_tests/test_flutes_run_error_wrapper_0_test_error_wrapper_basic.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
___________________________ test_error_wrapper_basic ___________________________

called_process_error = CalledProcessError(2, ['ls', '-l', '/nonexistent_file'])
timeout_expired = None

    def test_error_wrapper_basic(called_process_error, timeout_expired):
        wrapped_e = error_wrapper(called_process_error)
>       assert "No such file or directory" in str(wrapped_e)
E       assert 'No such file or directory' in "Command '['ls', '-l', '/nonexistent_file']' returned non-zero exit status 2.\nNo output was generated."
E        +  where "Command '['ls', '-l', '/nonexistent_file']' returned non-zero exit status 2.\nNo output was generated." = str(CalledProcessError(2, ['ls', '-l', '/nonexistent_file']))

flutes/Test4DT_tests/test_flutes_run_error_wrapper_0_test_error_wrapper_basic.py:20: AssertionError
__________________________ test_error_wrapper_timeout __________________________

timeout_expired = None

    def test_error_wrapper_timeout(timeout_expired):
        with pytest.raises(subprocess.TimeoutExpired) as excinfo:
>           wrapped_e = error_wrapper(excinfo.value)

flutes/Test4DT_tests/test_flutes_run_error_wrapper_0_test_error_wrapper_basic.py:25: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <ExceptionInfo for raises contextmanager>

    @property
    def value(self) -> E:
        """The exception value."""
        assert (
>           self._excinfo is not None
        ), ".value can only be used after the context manager exits"
E       AssertionError: .value can only be used after the context manager exits

/usr/local/lib/python3.11/site-packages/_pytest/_code/code.py:548: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_run_error_wrapper_0_test_error_wrapper_basic.py::test_error_wrapper_basic
FAILED flutes/Test4DT_tests/test_flutes_run_error_wrapper_0_test_error_wrapper_basic.py::test_error_wrapper_timeout
============================== 2 failed in 2.19s ===============================
"""