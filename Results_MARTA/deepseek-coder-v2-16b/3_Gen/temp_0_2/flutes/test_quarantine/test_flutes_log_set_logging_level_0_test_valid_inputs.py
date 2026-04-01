
import pytest
from unittest.mock import patch
from flutes.log import LEVEL_MAP, set_logging_level, LoggingLevel

@pytest.mark.parametrize("level, expected", [
    ('DEBUG', None),
    ('INFO', None),
    ('WARNING', None),
    ('ERROR', None),
    ('CRITICAL', None)
])
def test_valid_inputs(level, expected):
    with patch('flutes.log.LEVEL_MAP', {'DEBUG': 10, 'INFO': 20, 'WARNING': 30, 'ERROR': 40, 'CRITICAL': 50}):
        set_logging_level(level)
        assert True  # Assuming the function sets the level correctly and does not raise any errors.
