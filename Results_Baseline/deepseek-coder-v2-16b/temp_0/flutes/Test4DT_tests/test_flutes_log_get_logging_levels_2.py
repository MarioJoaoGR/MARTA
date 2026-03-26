
# Module: flutes.log
import pytest
from typing import List
from logging import Logger, DEBUG, INFO, WARNING, ERROR, CRITICAL

# Assuming LEVEL_MAP is a predefined dictionary mapping log levels to their respective constants
LEVEL_MAP = {
    DEBUG: "DEBUG",
    INFO: "INFO",
    WARNING: "WARNING",
    ERROR: "ERROR",
    CRITICAL: "CRITICAL"
}

def get_logging_levels() -> List[Logger]:
    r"""Return a list of logging levels that the logging system supports."""
    return list(LEVEL_MAP.keys())  # type: ignore[arg-type]

# Test cases for get_logging_levels function
def test_get_logging_levels():
    expected_levels = [DEBUG, INFO, WARNING, ERROR, CRITICAL]
    assert set(get_logging_levels()) == set(expected_levels), f"Expected {expected_levels}, but got {get_logging_levels()}"

# Additional test case to cover line 136
def test_get_logging_levels_returns_correct_list():
    levels = get_logging_levels()
    assert isinstance(levels, list), "Expected a list"
    for level in levels:
        assert isinstance(level, int), f"Expected all elements to be integers, but got {type(level)}"
    assert set(levels) == {DEBUG, INFO, WARNING, ERROR, CRITICAL}, "Unexpected logging levels returned"
