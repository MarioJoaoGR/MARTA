
import pytest
from flutes.log import set_logging_level, LoggingLevel, LEVEL_MAP
from logging import Logger, getLogger, WARNING

# Mocking the necessary objects and constants for testing
class _CONSOLE_LOGGING_LEVEL:
    value = None

LOGGER = getLogger()

def test_set_logging_level_valid_level():
    set_logging_level('DEBUG')
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

flutes/Test4DT_tests/test_flutes_log_set_logging_level_0.py F            [100%]

=================================== FAILURES ===================================
______________________ test_set_logging_level_valid_level ______________________

    def test_set_logging_level_valid_level():
>       set_logging_level('DEBUG')

flutes/Test4DT_tests/test_flutes_log_set_logging_level_0.py:13: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

level = 'DEBUG', console = True, file = True

    def set_logging_level(level: LoggingLevel, console: bool = True, file: bool = True) -> None:
        r"""Set the global logging level to the specified level.
    
        :param level: Logging level.
        :param console: If ``True``, the specified logging level applies to console output.
        :param file: If ``True``, the specified logging level applies to file output.
        """
        if level not in LEVEL_MAP:
>           raise ValueError(f"Incorrect logging level '{level}'")
E           ValueError: Incorrect logging level 'DEBUG'

flutes/flutes/log.py:193: ValueError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_log_set_logging_level_0.py::test_set_logging_level_valid_level
============================== 1 failed in 0.09s ===============================
"""