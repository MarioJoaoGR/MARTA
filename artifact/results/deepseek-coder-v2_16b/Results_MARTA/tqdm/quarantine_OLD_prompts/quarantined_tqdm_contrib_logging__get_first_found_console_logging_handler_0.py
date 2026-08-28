
import logging
from tqdm.contrib.logging import _get_first_found_console_logging_handler
import pytest
from unittest.mock import patch



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b/test_tqdm_contrib_logging__get_first_found_console_logging_handler_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_________________ test_get_first_found_console_logging_handler _________________

    def test_get_first_found_console_logging_handler():
        with patch('tqdm.contrib.logging._is_console_logging_handler', return_value=True):
            logger = logging.getLogger(__name__)
>           logger.handlers = [logging.StreamHandler(), logging.FileHandler()]
E           TypeError: FileHandler.__init__() missing 1 required positional argument: 'filename'

/opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b/test_tqdm_contrib_logging__get_first_found_console_logging_handler_0.py:10: TypeError
_______________________ test_no_console_logging_handler ________________________

    def test_no_console_logging_handler():
        with patch('tqdm.contrib.logging._is_console_logging_handler', return_value=False):
            logger = logging.getLogger(__name__)
>           logger.handlers = [logging.FileHandler()]
E           TypeError: FileHandler.__init__() missing 1 required positional argument: 'filename'

/opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b/test_tqdm_contrib_logging__get_first_found_console_logging_handler_0.py:18: TypeError
____________________________ test_multiple_handlers ____________________________

    def test_multiple_handlers():
        with patch('tqdm.contrib.logging._is_console_logging_handler', side_effect=[False, True]):
            logger = logging.getLogger(__name__)
>           logger.handlers = [logging.FileHandler(), logging.StreamHandler()]
E           TypeError: FileHandler.__init__() missing 1 required positional argument: 'filename'

/opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b/test_tqdm_contrib_logging__get_first_found_console_logging_handler_0.py:26: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b/test_tqdm_contrib_logging__get_first_found_console_logging_handler_0.py::test_get_first_found_console_logging_handler
FAILED ../../../../../opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b/test_tqdm_contrib_logging__get_first_found_console_logging_handler_0.py::test_no_console_logging_handler
FAILED ../../../../../opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b/test_tqdm_contrib_logging__get_first_found_console_logging_handler_0.py::test_multiple_handlers
============================== 3 failed in 0.06s ===============================
"""