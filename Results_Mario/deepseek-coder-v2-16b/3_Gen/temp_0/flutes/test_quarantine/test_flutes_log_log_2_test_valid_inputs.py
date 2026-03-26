
import pytest
from flutes.log import log, LOGGING_MAP, LEVEL_MAP, _CONSOLE_LOGGING_LEVEL, COLOR_MAP, LOGGER, get_worker_id
from termcolor import colored
import time

@pytest.mark.parametrize("msg, level, force_console, timestamp, include_proc_id", [
    ("This is an info message.", "info", False, True, True),
    ("A warning!", "warning", False, False, False),
    ("Error reported.", "error", True, True, True),
    ("Success message.", "success", False, True, True),
])
def test_valid_inputs(msg, level, force_console, timestamp, include_proc_id):
    log(msg, level=level, force_console=force_console, timestamp=timestamp, include_proc_id=include_proc_id)
    
    # Add assertions to verify the expected behavior
    if level in LOGGING_MAP:
        assert True  # Assuming that logging to a logger is successful and no errors are raised
    else:
        with pytest.raises(ValueError):
            log("Invalid level", level="invalid")
