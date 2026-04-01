
import pytest
from typing import List
from flutes.log import LEVEL_MAP, LoggingLevel

def get_logging_levels() -> List[LoggingLevel]:
    r"""Return a list of logging levels that the logging system supports."""
    return list(LEVEL_MAP.keys())  # type: ignore[arg-type]

@pytest.mark.skipif(not hasattr(LEVEL_MAP, 'keys'), reason="LEVEL_MAP does not have keys attribute")
def test_empty_map():
    LEVEL_MAP.clear()  # Ensure LEVEL_MAP is empty
    assert get_logging_levels() == []
