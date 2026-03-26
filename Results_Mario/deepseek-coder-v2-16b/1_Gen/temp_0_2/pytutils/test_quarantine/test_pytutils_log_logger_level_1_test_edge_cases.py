
import logging
import pytest
from pytutils.log import logger_level

def test_logger_level():
    log = logging.getLogger(__name__)
    
    # Test setting a valid level
    with logger_level(log, logging.DEBUG):
        assert log.getEffectiveLevel() == logging.DEBUG
    
    # Test resetting to the original level after context block
    initial_level = log.getEffectiveLevel()
    with logger_level(log, logging.INFO):
        pass  # Just ensure it doesn't change anything
    assert log.getEffectiveLevel() == initial_level
    
    # Test setting an invalid level (should raise a TypeError)
    with pytest.raises(TypeError):
        with logger_level(log, "invalid_level"):
            pass  # This should not reach here due to the raised TypeError

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

pytutils/Test4DT_tests/test_pytutils_log_logger_level_1_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
______________________________ test_logger_level _______________________________

    def test_logger_level():
        log = logging.getLogger(__name__)
    
        # Test setting a valid level
        with logger_level(log, logging.DEBUG):
            assert log.getEffectiveLevel() == logging.DEBUG
    
        # Test resetting to the original level after context block
        initial_level = log.getEffectiveLevel()
        with logger_level(log, logging.INFO):
            pass  # Just ensure it doesn't change anything
        assert log.getEffectiveLevel() == initial_level
    
        # Test setting an invalid level (should raise a TypeError)
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

pytutils/Test4DT_tests/test_pytutils_log_logger_level_1_test_edge_cases.py:20: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_log_logger_level_1_test_edge_cases.py::test_logger_level
============================== 1 failed in 0.06s ===============================
"""