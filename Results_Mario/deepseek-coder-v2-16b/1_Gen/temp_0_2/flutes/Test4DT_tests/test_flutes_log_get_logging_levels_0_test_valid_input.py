
import pytest
from logging import (
    DEBUG, INFO, WARNING, ERROR, CRITICAL,  # Correctly imported from the logging module
)
from typing import List

def get_logging_levels() -> List[str]:
    r"""Return a list of logging levels that the logging system supports."""
    return list(LEVEL_MAP.keys())  # type: ignore[arg-type]

# Mock LEVEL_MAP for testing purposes
LEVEL_MAP = {
    'DEBUG': DEBUG,
    'INFO': INFO,
    'WARNING': WARNING,
    'ERROR': ERROR,
    'CRITICAL': CRITICAL,
}

def test_valid_input():
    log_levels = get_logging_levels()
    assert log_levels == ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
