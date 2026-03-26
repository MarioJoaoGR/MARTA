
import pytest
from typing import List
from unittest.mock import patch
from logging import Logger, NOTSET, CRITICAL, ERROR, WARNING, INFO, DEBUG  # type: ignore[attr-defined]

# Assuming LEVEL_MAP is defined somewhere in the flutes.log module
LEVEL_MAP = {
    'CRITICAL': CRITICAL,
    'ERROR': ERROR,
    'WARNING': WARNING,
    'INFO': INFO,
    'DEBUG': DEBUG,
}

def get_logging_levels() -> List[str]:
    r"""Return a list of logging levels that the logging system supports."""
    return list(LEVEL_MAP.keys())  # type: ignore[arg-type]

@pytest.mark.parametrize("expected", [
    (['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG'])
])
def test_valid_case(expected):
    with patch('flutes.log.LEVEL_MAP', LEVEL_MAP):
        levels = get_logging_levels()
        assert levels == expected
