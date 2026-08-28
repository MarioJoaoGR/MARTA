
import logging
from tqdm.contrib.logging import _get_first_found_console_logging_handler
import pytest

def _is_console_logging_handler(handler):
    return isinstance(handler, (logging.StreamHandler, logging.FileHandler))

@pytest.mark.parametrize("handlers", [
    ([logging.StreamHandler(), logging.FileHandler()]),
    ([logging.FileHandler()])
])
def test_valid_input(handlers):
    logger = logging.getLogger('test')
    logger.handlers = handlers
    console_handler = _get_first_found_console_logging_handler(logger.handlers)
    if len(handlers) == 2:
        assert isinstance(console_handler, (logging.StreamHandler, logging.FileHandler)), "Expected a console handler to be found"
    else:
        assert console_handler is None, "Expected no console handler to be found"

def test_no_console_handler():
    logger = logging.getLogger('test')
    logger.handlers = [logging.FileHandler()]
    console_handler = _get_first_found_console_logging_handler(logger.handlers)
    assert console_handler is None, "Expected no console handler to be found"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_ ERROR collecting test_tqdm_contrib_logging__get_first_found_console_logging_handler_0.py _
/opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b/test_tqdm_contrib_logging__get_first_found_console_logging_handler_0.py:10: in <module>
    ([logging.StreamHandler(), logging.FileHandler()]),
E   TypeError: FileHandler.__init__() missing 1 required positional argument: 'filename'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b/test_tqdm_contrib_logging__get_first_found_console_logging_handler_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.12s ===============================
"""