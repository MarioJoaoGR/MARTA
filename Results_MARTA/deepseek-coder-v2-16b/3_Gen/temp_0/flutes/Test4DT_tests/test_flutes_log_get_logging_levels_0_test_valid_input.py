
import pytest
from logging import LogRecord, NOTSET, DEBUG, INFO, WARNING, ERROR, CRITICAL
from typing import List

# Assuming LEVEL_MAP is defined somewhere in your codebase
LEVEL_MAP = {
    NOTSET: 'NOTSET',
    DEBUG: 'DEBUG',
    INFO: 'INFO',
    WARNING: 'WARNING',
    ERROR: 'ERROR',
    CRITICAL: 'CRITICAL'
}

def get_logging_levels() -> List[str]:
    r"""Return a list of logging levels that the logging system supports."""
    return list(LEVEL_MAP.keys())  # type: ignore[arg-type]

@pytest.mark.parametrize("expected", [
    ([NOTSET, DEBUG, INFO, WARNING, ERROR, CRITICAL]),
])
def test_valid_input(expected):
    levels = get_logging_levels()
    assert sorted(levels) == expected
