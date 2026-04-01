
import logging
import pytest
from pytutils.log import get_logger

def test_valid_input():
    log = get_logger()
    assert isinstance(log, logging.Logger)
    
    # Check if the root logger is not None after getting it with no name
    log_no_name = get_logger()
    assert log_no_name is not None
    
    # Check if a named logger is not None after getting it with a specific name
    log_named = get_logger('test2')
    assert log_named is not None
    
    # Log a message and check if the root logger's level allows this message to be logged
    log.info('This is a test message from the root logger.')
    captured = capsys.readouterr()
    assert 'This is a test message from the root logger.' in captured.out
    
    # Log another message through the named logger and check if it appears
    log_named.info('This is a test message from the named logger.')
    captured_named = capsys.readouterr()
    assert 'This is a test message from the named logger.' in captured_named.out

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_log_get_logger_0_test_valid_input
pytutils/Test4DT_tests/test_pytutils_log_get_logger_0_test_valid_input.py:20:15: E0602: Undefined variable 'capsys' (undefined-variable)
pytutils/Test4DT_tests/test_pytutils_log_get_logger_0_test_valid_input.py:25:21: E0602: Undefined variable 'capsys' (undefined-variable)


"""