
import sys
import os
from unittest.mock import patch, MagicMock
import pytest
from flutes.io import shut_up

def test_shut_up_context_manager():
    with patch('sys.stdout', new=MagicMock()) as mock_stdout, \
         patch('sys.stderr', new=MagicMock()) as mock_stderr:
        # Capture the original file descriptors
        stdout_fd = sys.stdout.fileno()
        stderr_fd = sys.stderr.fileno()

        with shut_up(stderr=True):
            assert not mock_stderr.called
            assert mock_stdout.called

        # Restore the original file descriptors
        os.dup2(stdout_fd, sys.stdout.fileno())
        os.dup2(stderr_fd, sys.stderr.fileno())

def test_shut_up_decorator():
    with patch('sys.stdout', new=MagicMock()) as mock_stdout, \
         patch('sys.stderr', new=MagicMock()) as mock_stderr:
        # Original file descriptors
        stdout_fd = sys.stdout.fileno()
        stderr_fd = sys.stderr.fileno()

        @shut_up(stderr=True)
        def test_func():
            pass

        test_func()
        assert not mock_stderr.called
        assert mock_stdout.called

        # Restore the original file descriptors
        os.dup2(stdout_fd, sys.stdout.fileno())
        os.dup2(stderr_fd, sys.stderr.fileno())

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

flutes/Test4DT_tests/test_flutes_io_shut_up_0_test_valid_inputs.py FF    [100%]

=================================== FAILURES ===================================
_________________________ test_shut_up_context_manager _________________________

    def test_shut_up_context_manager():
        with patch('sys.stdout', new=MagicMock()) as mock_stdout, \
             patch('sys.stderr', new=MagicMock()) as mock_stderr:
            # Capture the original file descriptors
            stdout_fd = sys.stdout.fileno()
            stderr_fd = sys.stderr.fileno()
    
            with shut_up(stderr=True):
                assert not mock_stderr.called
>               assert mock_stdout.called
E               AssertionError: assert False
E                +  where False = <MagicMock id='140231365453136'>.called

flutes/Test4DT_tests/test_flutes_io_shut_up_0_test_valid_inputs.py:17: AssertionError
____________________________ test_shut_up_decorator ____________________________

    def test_shut_up_decorator():
        with patch('sys.stdout', new=MagicMock()) as mock_stdout, \
             patch('sys.stderr', new=MagicMock()) as mock_stderr:
            # Original file descriptors
            stdout_fd = sys.stdout.fileno()
            stderr_fd = sys.stderr.fileno()
    
            @shut_up(stderr=True)
            def test_func():
                pass
    
            test_func()
            assert not mock_stderr.called
>           assert mock_stdout.called
E           AssertionError: assert False
E            +  where False = <MagicMock id='140231365307408'>.called

flutes/Test4DT_tests/test_flutes_io_shut_up_0_test_valid_inputs.py:36: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_io_shut_up_0_test_valid_inputs.py::test_shut_up_context_manager
FAILED flutes/Test4DT_tests/test_flutes_io_shut_up_0_test_valid_inputs.py::test_shut_up_decorator
============================== 2 failed in 0.09s ===============================
"""