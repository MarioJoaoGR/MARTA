
import logging
import pytest
from flutes.log import _remove_handlers

def test_invalid_input():
    # Create an invalid logger type (e.g., a string)
    invalid_logger = "invalid_logger"
    
    # Mock the logging module to raise an error when trying to remove handlers from an invalid logger
    with pytest.raises(TypeError):
        _remove_handlers(invalid_logger)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_log__remove_handlers_2_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        # Create an invalid logger type (e.g., a string)
        invalid_logger = "invalid_logger"
    
        # Mock the logging module to raise an error when trying to remove handlers from an invalid logger
        with pytest.raises(TypeError):
>           _remove_handlers(invalid_logger)

flutes/Test4DT_tests/test_flutes_log__remove_handlers_2_test_invalid_input.py:12: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

logger = 'invalid_logger'

    def _remove_handlers(logger):
>       while len(logger.handlers) > 0:
E       AttributeError: 'str' object has no attribute 'handlers'

flutes/flutes/log.py:97: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_log__remove_handlers_2_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.09s ===============================

"""