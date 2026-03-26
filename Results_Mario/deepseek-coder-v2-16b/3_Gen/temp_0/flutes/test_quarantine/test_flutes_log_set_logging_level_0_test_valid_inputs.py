
import pytest
from flutes.log import set_logging_level, LEVEL_MAP, _CONSOLE_LOGGING_LEVEL, LOGGER
from logging import DEBUG, INFO, WARNING, ERROR, CRITICAL

def test_set_logging_level_valid_inputs():
    # Test setting the logging level to DEBUG with console and file outputs
    set_logging_level('DEBUG', console=True, file=True)
    assert _CONSOLE_LOGGING_LEVEL.value == LEVEL_MAP['DEBUG']
    assert LOGGER.getEffectiveLevel() == LEVEL_MAP['DEBUG']

    # Test setting the logging level to INFO with only console output
    set_logging_level('INFO', console=True, file=False)
    assert _CONSOLE_LOGGING_LEVEL.value == LEVEL_MAP['INFO']
    assert LOGGER.getEffectiveLevel() == LEVEL_MAP['INFO']

    # Test setting the logging level to WARNING with only file output
    set_logging_level('WARNING', console=False, file=True)
    assert _CONSOLE_LOGGING_LEVEL.value == LEVEL_MAP['WARNING']
    assert LOGGER.getEffectiveLevel() == LEVEL_MAP['WARNING']

    # Test setting the logging level to ERROR with neither console nor file output
    set_logging_level('ERROR', console=False, file=False)
    assert _CONSOLE_LOGGING_LEVEL.value == LEVEL_MAP['ERROR']
    assert LOGGER.getEffectiveLevel() == LEVEL_MAP['ERROR']

    # Test setting the logging level to CRITICAL with only console output
    set_logging_level('CRITICAL', console=True, file=False)
    assert _CONSOLE_LOGGING_LEVEL.value == LEVEL_MAP['CRITICAL']
    assert LOGGER.getEffectiveLevel() == LEVEL_MAP['CRITICAL']

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_log_set_logging_level_0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________ test_set_logging_level_valid_inputs ______________________

    def test_set_logging_level_valid_inputs():
        # Test setting the logging level to DEBUG with console and file outputs
>       set_logging_level('DEBUG', console=True, file=True)

flutes/Test4DT_tests/test_flutes_log_set_logging_level_0_test_valid_inputs.py:8: 
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
FAILED flutes/Test4DT_tests/test_flutes_log_set_logging_level_0_test_valid_inputs.py::test_set_logging_level_valid_inputs
============================== 1 failed in 0.11s ===============================
"""