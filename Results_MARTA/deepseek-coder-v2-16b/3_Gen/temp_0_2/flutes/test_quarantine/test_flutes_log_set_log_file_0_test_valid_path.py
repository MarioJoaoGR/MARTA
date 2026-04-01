
from pathlib import Path
from unittest.mock import patch
import logging
from flutes.log import MultiprocessingFileHandler, set_log_file

LOGGER = logging.getLogger()

def test_valid_path():
    with patch('flutes.log.MultiprocessingFileHandler') as mock_handler:
        path = Path('test_log_file.log')
        set_log_file(path)

        # Assert that the logger has a handler added and it's of the correct type
        assert len(LOGGER.handlers) == 1
        assert isinstance(LOGGER.handlers[0], mock_handler)

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

flutes/Test4DT_tests/test_flutes_log_set_log_file_0_test_valid_path.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_path ________________________________

    def test_valid_path():
        with patch('flutes.log.MultiprocessingFileHandler') as mock_handler:
            path = Path('test_log_file.log')
            set_log_file(path)
    
            # Assert that the logger has a handler added and it's of the correct type
>           assert len(LOGGER.handlers) == 1
E           assert 5 == 1
E            +  where 5 = len([<_LiveLoggingNullHandler (NOTSET)>, <_FileHandler /dev/null (NOTSET)>, <LogCaptureHandler (NOTSET)>, <LogCaptureHandler (NOTSET)>, <LoggingHandler (NOTSET)>])
E            +    where [<_LiveLoggingNullHandler (NOTSET)>, <_FileHandler /dev/null (NOTSET)>, <LogCaptureHandler (NOTSET)>, <LogCaptureHandler (NOTSET)>, <LoggingHandler (NOTSET)>] = <RootLogger root (WARNING)>.handlers

flutes/Test4DT_tests/test_flutes_log_set_log_file_0_test_valid_path.py:15: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_log_set_log_file_0_test_valid_path.py::test_valid_path
============================== 1 failed in 0.08s ===============================
"""