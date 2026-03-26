
import pytest
from flutes.log import LEVEL_MAP, _CONSOLE_LOGGING_LEVEL, LOGGER

def set_logging_level(level: LoggingLevel, console: bool = True, file: bool = True) -> None:
    r"""Set the global logging level to the specified level.

    :param level: Logging level.
    :param console: If ``True``, the specified logging level applies to console output.
    :param file: If ``True``, the specified logging level applies to file output.
    """
    if level not in LEVEL_MAP:
        raise ValueError(f"Incorrect logging level '{level}'")
    if console:
        _CONSOLE_LOGGING_LEVEL.value = LEVEL_MAP[level]
    if file:
        LOGGER.setLevel(LEVEL_MAP[level])

@pytest.mark.parametrize("invalid_level", ["INVALID_LEVEL", None, 123])
def test_invalid_inputs(invalid_level):
    with pytest.raises(ValueError) as excinfo:
        set_logging_level(invalid_level)
    assert str(excinfo.value) == f"Incorrect logging level '{invalid_level}'"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_log_set_logging_level_2_test_invalid_inputs
flutes/Test4DT_tests/test_flutes_log_set_logging_level_2_test_invalid_inputs.py:5:29: E0602: Undefined variable 'LoggingLevel' (undefined-variable)


"""