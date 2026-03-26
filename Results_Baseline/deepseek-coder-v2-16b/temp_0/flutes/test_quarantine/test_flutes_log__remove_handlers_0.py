
import logging
import pytest
from flutes.log import _remove_handlers

# Test fixture to create a logger with handlers for testing
@pytest.fixture
def setup_logger():
    logger = logging.getLogger('my_logger')
    logger.setLevel(logging.DEBUG)
    
    handler1 = logging.FileHandler('file1.log')
    logger.addHandler(handler1)
    
    handler2 = logging.StreamHandler()
    logger.addHandler(handler2)
    
    yield logger
    
    # Teardown: Remove all handlers to ensure no residual state affects other tests
    _remove_handlers(logger)

def test_remove_handlers_removes_all_handlers(setup_logger):
    logger = setup_logger()
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

flutes/Test4DT_tests/test_flutes_log__remove_handlers_0.py F             [100%]

=================================== FAILURES ===================================
__________________ test_remove_handlers_removes_all_handlers ___________________

setup_logger = <Logger my_logger (DEBUG)>

    def test_remove_handlers_removes_all_handlers(setup_logger):
>       logger = setup_logger()
E       TypeError: 'Logger' object is not callable

flutes/Test4DT_tests/test_flutes_log__remove_handlers_0.py:24: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_log__remove_handlers_0.py::test_remove_handlers_removes_all_handlers
============================== 1 failed in 0.08s ===============================
"""