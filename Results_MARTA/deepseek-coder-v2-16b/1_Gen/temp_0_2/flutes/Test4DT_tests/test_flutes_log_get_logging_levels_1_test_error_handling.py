
import pytest
from unittest.mock import patch
from flutes.log import LEVEL_MAP, LoggingLevel
from typing import List

def get_logging_levels() -> List[LoggingLevel]:
    r"""Return a list of logging levels that the logging system supports."""
    return list(LEVEL_MAP.keys())  # type: ignore[arg-type]

@pytest.mark.skip(reason="Mocking LEVEL_MAP is not necessary for this test")
def test_error_handling():
    with patch('flutes.log.LEVEL_MAP', None):
        with pytest.raises(NameError):
            get_logging_levels()
