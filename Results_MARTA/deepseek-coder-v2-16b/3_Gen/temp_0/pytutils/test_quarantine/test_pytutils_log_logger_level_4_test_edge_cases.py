
import logging
from pytutils.log import logger_level

def test_logger_level():
    log = logging.getLogger(__name__)
    
    # Test with valid logger and level
    assert log.level == logging.NOTSET
    with logger_level(log, logging.DEBUG):
        assert log.level == logging.DEBUG
    assert log.level == logging.NOTSET
    
    # Test with invalid logger (should raise TypeError)
    import pytest
    with pytest.raises(TypeError):
        with logger_level(None, logging.DEBUG):

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_log_logger_level_4_test_edge_cases
pytutils/Test4DT_tests/test_pytutils_log_logger_level_4_test_edge_cases.py:18:1: E0001: Parsing failed: 'expected an indented block after 'with' statement on line 17 (Test4DT_tests.test_pytutils_log_logger_level_4_test_edge_cases, line 18)' (syntax-error)


"""