
# Module: flutes.log
import pytest
from flutes.log import log
from logging import LoggingLevel  # Corrected import statement for LoggingLevel
import time

# Assuming the following constants and functions are defined in the module flutes.log
LOGGING_MAP = {
    "success": lambda msg: print(f"SUCCESS: {msg}"),
    "warning": lambda msg: print(f"WARNING: {msg}"),
    "error": lambda msg: print(f"ERROR: {msg}"),
    "info": lambda msg: print(f"INFO: {msg}")
}

LEVEL_MAP = {
    "success": 0,
    "warning": 1,
    "error": 2,
    "info": 3
}

_CONSOLE_LOGGING_LEVEL = type('ConsoleLoggingLevel', (), {'value': 3})()
COLOR_MAP = {
    "success": 'green',
    "warning": 'yellow',
    "error": 'red',
    "info": 'blue'
}

def _CONSOLE_LOG_FN(msg):
    print(msg)

def get_worker_id():
    # Placeholder for the actual implementation of get_worker_id()
    return 42

# Test cases
def test_log_default_usage():
    log("This is an informational message.")
    # Expected output: INFO: This is an informational message.

def test_log_specific_level():
    log("Something went wrong!", level="error")
    # Expected output: ERROR: Something went wrong!

def test_force_console_without_timestamp():
    log("Console-only message.", force_console=True, timestamp=False)
    # Expected output: Console-only message.

def test_log_custom_level():
    with pytest.raises(ValueError):
        log("A custom level message.", level="custom")
    # Expected error: Incorrect logging level 'custom'

def test_logging_without_timestamp_and_include_proc_id():
    log("Message without timestamp and including process ID.", force_console=True, timestamp=False, include_proc_id=True)
    # Expected output with worker id: (Worker 42) Message without timestamp and including process ID.

if __name__ == "__main__":
    pytest.main()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_log_log_0
flutes/Test4DT_tests/test_flutes_log_log_0.py:5:0: E0611: No name 'LoggingLevel' in module 'logging' (no-name-in-module)


"""