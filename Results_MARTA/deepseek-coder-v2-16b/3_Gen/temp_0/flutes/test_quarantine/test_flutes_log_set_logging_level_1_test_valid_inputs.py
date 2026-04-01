
import pytest
from flutes.log import LoggingLevel, LEVEL_MAP, _CONSOLE_LOGGING_LEVEL, LOGGER

def test_set_logging_level_valid_inputs():
    # Test setting logging level to DEBUG with console and file outputs
    set_logging_level('DEBUG', console=True, file=True)
    assert _CONSOLE_LOGGING_LEVEL.value == LEVEL_MAP['DEBUG']
    assert LOGGER.getEffectiveLevel() == LEVEL_MAP['DEBUG']

    # Test setting logging level to INFO with only console output
    set_logging_level('INFO', console=True, file=False)
    assert _CONSOLE_LOGGING_LEVEL.value == LEVEL_MAP['INFO']
    assert LOGGER.getEffectiveLevel() == LEVEL_MAP['INFO']

    # Test setting logging level to WARNING with only file output
    set_logging_level('WARNING', console=False, file=True)
    assert _CONSOLE_LOGGING_LEVEL.value == LEVEL_MAP['WARNING']
    assert LOGGER.getEffectiveLevel() == LEVEL_MAP['WARNING']

    # Test setting logging level to ERROR with neither console nor file output
    set_logging_level('ERROR', console=False, file=False)
    assert _CONSOLE_LOGGING_LEVEL.value == LEVEL_MAP['ERROR']
    assert LOGGER.getEffectiveLevel() == LEVEL_MAP['ERROR']

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_log_set_logging_level_1_test_valid_inputs
flutes/Test4DT_tests/test_flutes_log_set_logging_level_1_test_valid_inputs.py:7:4: E0602: Undefined variable 'set_logging_level' (undefined-variable)
flutes/Test4DT_tests/test_flutes_log_set_logging_level_1_test_valid_inputs.py:12:4: E0602: Undefined variable 'set_logging_level' (undefined-variable)
flutes/Test4DT_tests/test_flutes_log_set_logging_level_1_test_valid_inputs.py:17:4: E0602: Undefined variable 'set_logging_level' (undefined-variable)
flutes/Test4DT_tests/test_flutes_log_set_logging_level_1_test_valid_inputs.py:22:4: E0602: Undefined variable 'set_logging_level' (undefined-variable)


"""