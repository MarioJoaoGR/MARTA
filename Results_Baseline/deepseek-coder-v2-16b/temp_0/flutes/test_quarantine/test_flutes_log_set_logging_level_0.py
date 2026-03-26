
# Module: flutes.log
import pytest
from flutes.log import set_logging_level, LEVEL_MAP

# Define a fixture for the logging level to be used in tests
@pytest.fixture
def reset_logging():
    original_console_level = _CONSOLE_LOGGING_LEVEL.value
    original_file_level = LOGGER.getLevel()
    set_logging_level('DEBUG', console=True, file=True)
    yield  # This is where the tests will run
    _CONSOLE_LOGGING_LEVEL.value = original_console_level
    LOGGER.setLevel(original_file_level)

# Test cases for set_logging_level function
def test_set_logging_level_valid_level():
    with pytest.raises(ValueError):
        set_logging_level('INVALID_LEVEL', console=True, file=True)

def test_set_logging_level_default_console_true(reset_logging):
    set_logging_level('DEBUG', console=True, file=True)
    assert _CONSOLE_LOGGING_LEVEL.value == LEVEL_MAP['DEBUG']
    assert LOGGER.getLevel() == LEVEL_MAP['DEBUG']

def test_set_logging_level_default_console_false(reset_logging):
    set_logging_level('DEBUG', console=False, file=True)
    assert _CONSOLE_LOGGING_LEVEL.value == LEVEL_MAP['DEBUG']
    assert LOGGER.getLevel() == LEVEL_MAP['DEBUG']

def test_set_logging_level_default_file_false(reset_logging):
    set_logging_level('DEBUG', console=True, file=False)
    assert _CONSOLE_LOGGING_LEVEL.value == LEVEL_MAP['DEBUG']
    assert LOGGER.getLevel() == LEVEL_MAP['DEBUG']

def test_set_logging_level_default_both_false(reset_logging):
    set_logging_level('DEBUG', console=False, file=False)
    assert _CONSOLE_LOGGING_LEVEL.value == LEVEL_MAP['DEBUG']
    assert LOGGER.getLevel() == LEVEL_MAP['DEBUG']

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_log_set_logging_level_0
flutes/Test4DT_tests/test_flutes_log_set_logging_level_0.py:9:29: E0602: Undefined variable '_CONSOLE_LOGGING_LEVEL' (undefined-variable)
flutes/Test4DT_tests/test_flutes_log_set_logging_level_0.py:10:26: E0602: Undefined variable 'LOGGER' (undefined-variable)
flutes/Test4DT_tests/test_flutes_log_set_logging_level_0.py:13:4: E0602: Undefined variable '_CONSOLE_LOGGING_LEVEL' (undefined-variable)
flutes/Test4DT_tests/test_flutes_log_set_logging_level_0.py:14:4: E0602: Undefined variable 'LOGGER' (undefined-variable)
flutes/Test4DT_tests/test_flutes_log_set_logging_level_0.py:23:11: E0602: Undefined variable '_CONSOLE_LOGGING_LEVEL' (undefined-variable)
flutes/Test4DT_tests/test_flutes_log_set_logging_level_0.py:24:11: E0602: Undefined variable 'LOGGER' (undefined-variable)
flutes/Test4DT_tests/test_flutes_log_set_logging_level_0.py:28:11: E0602: Undefined variable '_CONSOLE_LOGGING_LEVEL' (undefined-variable)
flutes/Test4DT_tests/test_flutes_log_set_logging_level_0.py:29:11: E0602: Undefined variable 'LOGGER' (undefined-variable)
flutes/Test4DT_tests/test_flutes_log_set_logging_level_0.py:33:11: E0602: Undefined variable '_CONSOLE_LOGGING_LEVEL' (undefined-variable)
flutes/Test4DT_tests/test_flutes_log_set_logging_level_0.py:34:11: E0602: Undefined variable 'LOGGER' (undefined-variable)
flutes/Test4DT_tests/test_flutes_log_set_logging_level_0.py:38:11: E0602: Undefined variable '_CONSOLE_LOGGING_LEVEL' (undefined-variable)
flutes/Test4DT_tests/test_flutes_log_set_logging_level_0.py:39:11: E0602: Undefined variable 'LOGGER' (undefined-variable)


"""