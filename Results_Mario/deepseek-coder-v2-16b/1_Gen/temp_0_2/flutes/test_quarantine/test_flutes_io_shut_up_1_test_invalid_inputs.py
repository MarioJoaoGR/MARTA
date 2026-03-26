
import pytest
import sys
import os
from flutes.io import shut_up

@pytest.fixture(autouse=True)
def mock_stdout_and_stderr():
    # Save original file descriptors
    original_stdout = sys.stdout.fileno()
    original_stderr = sys.stderr.fileno()

    # Redirect stdout and stderr to /dev/null
    null_fds = [os.open(os.devnull, os.O_RDWR)] * 2
    for fd in (sys.stdout.fileno(), sys.stderr.fileno()):
        os.dup2(null_fds[0], fd)

    yield

    # Restore original file descriptors
    for fd, original_fd in zip((sys.stdout.fileno(), sys.stderr.fileno()), (original_stdout, original_stderr)):
        os.dup2(original_fd, fd)
        os.close(null_fds[0])

@pytest.mark.parametrize("stderr, stdout", [(True, False), (False, True), (True, True)])
def test_shut_up(stderr, stdout):
    with shut_up(stderr=stderr, stdout=stdout) as s:
        assert isinstance(s, contextlib._GeneratorContextManager)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_io_shut_up_1_test_invalid_inputs
flutes/Test4DT_tests/test_flutes_io_shut_up_1_test_invalid_inputs.py:28:29: E0602: Undefined variable 'contextlib' (undefined-variable)


"""