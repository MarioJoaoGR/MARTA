
import pytest
from flutes.log import LEVEL_MAP, _CONSOLE_LOGGING_LEVEL, LOGGER

@pytest.mark.parametrize("invalid_level", ["INVALID_LEVEL", "DEBUG", "INFO"])
def test_invalid_inputs(invalid_level):
    with pytest.raises(ValueError) as excinfo:
        set_logging_level(invalid_level)
    assert str(excinfo.value) == f"Incorrect logging level '{invalid_level}'"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_log_set_logging_level_1_test_invalid_inputs
flutes/Test4DT_tests/test_flutes_log_set_logging_level_1_test_invalid_inputs.py:8:8: E0602: Undefined variable 'set_logging_level' (undefined-variable)


"""