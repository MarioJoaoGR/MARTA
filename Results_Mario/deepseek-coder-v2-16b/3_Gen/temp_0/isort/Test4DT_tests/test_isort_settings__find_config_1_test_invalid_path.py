
import os
from typing import Any

from isort.settings import (CONFIG_SECTIONS, CONFIG_SOURCES,
                            MAX_CONFIG_SEARCH_DEPTH,
                            STOP_CONFIG_SEARCH_ON_DIRS, _find_config)


def test_invalid_path():
    invalid_path = "/nonexistent/directory"
    result = _find_config(invalid_path)
    
    assert result[0] == invalid_path
    assert isinstance(result[1], dict)
    assert not result[1]  # The dictionary should be empty
