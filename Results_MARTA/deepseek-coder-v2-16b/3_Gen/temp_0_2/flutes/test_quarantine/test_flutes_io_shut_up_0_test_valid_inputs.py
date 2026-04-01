
import sys
import os
from flutes.io import shut_up
import pytest

# Mocking os and sys modules to control their behavior in the test
class MockFD:
    def __init__(self, name):
        self.name = name
        self.write_calls = []
    
    def write(self, data):
        self.write_calls.append(data)

class MockStdout(MockFD):
    pass

class MockStderr(MockFD):
    pass

@pytest.fixture(autouse=True)
def mock_io():
    # Create mocks for stdout and stderr
    sys.stdout = MockStdout("stdout")
    sys.stderr = MockStderr("stderr")
    
    yield
    
    # Restore original stdout and stderr after the test
    sys.stdout = sys.__stdout__
    sys.stderr = sys.__stderr__

def test_shut_up_with_stderr():
    @shut_up(stderr=True)
    def verbose_func():
        print("This should not be printed")
    
    verbose_func()
    assert len(sys.stderr.write_calls) == 0, "Expected stderr to be suppressed"

def test_shut_up_with_stdout():
    @shut_up(stdout=True)
    def verbose_func():
        print("This should not be printed")
    
    verbose_func()
    assert len(sys.stdout.write_calls) == 0, "Expected stdout to be suppressed"

def test_shut_up_with_both():
    @shut_up(stderr=True, stdout=True)
    def verbose_func():
        print("This should not be printed")
    
    verbose_func()
    assert len(sys.stdout.write_calls) == 0 and len(sys.stderr.write_calls) == 0, "Expected both stdout and stderr to be suppressed"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

flutes/Test4DT_tests/test_flutes_io_shut_up_0_test_valid_inputs.py FFF   [100%]

=================================== FAILURES ===================================
___________________________ test_shut_up_with_stderr ___________________________

    def test_shut_up_with_stderr():
        @shut_up(stderr=True)
        def verbose_func():
            print("This should not be printed")
    
        verbose_func()
>       assert len(sys.stderr.write_calls) == 0, "Expected stderr to be suppressed"
E       AttributeError: 'EncodedFile' object has no attribute 'write_calls'

flutes/Test4DT_tests/test_flutes_io_shut_up_0_test_valid_inputs.py:40: AttributeError
----------------------------- Captured stdout call -----------------------------
This should not be printed
___________________________ test_shut_up_with_stdout ___________________________

    def test_shut_up_with_stdout():
        @shut_up(stdout=True)
        def verbose_func():
            print("This should not be printed")
    
        verbose_func()
>       assert len(sys.stdout.write_calls) == 0, "Expected stdout to be suppressed"
E       AttributeError: 'EncodedFile' object has no attribute 'write_calls'

flutes/Test4DT_tests/test_flutes_io_shut_up_0_test_valid_inputs.py:48: AttributeError
____________________________ test_shut_up_with_both ____________________________

    def test_shut_up_with_both():
        @shut_up(stderr=True, stdout=True)
        def verbose_func():
            print("This should not be printed")
    
        verbose_func()
>       assert len(sys.stdout.write_calls) == 0 and len(sys.stderr.write_calls) == 0, "Expected both stdout and stderr to be suppressed"
E       AttributeError: 'EncodedFile' object has no attribute 'write_calls'

flutes/Test4DT_tests/test_flutes_io_shut_up_0_test_valid_inputs.py:56: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_io_shut_up_0_test_valid_inputs.py::test_shut_up_with_stderr
FAILED flutes/Test4DT_tests/test_flutes_io_shut_up_0_test_valid_inputs.py::test_shut_up_with_stdout
FAILED flutes/Test4DT_tests/test_flutes_io_shut_up_0_test_valid_inputs.py::test_shut_up_with_both
============================== 3 failed in 0.11s ===============================
"""