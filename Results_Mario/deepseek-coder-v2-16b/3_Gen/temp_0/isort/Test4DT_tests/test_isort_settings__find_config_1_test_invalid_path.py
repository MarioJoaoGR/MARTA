
import os
from typing import Any
from isort.settings import _find_config, MAX_CONFIG_SEARCH_DEPTH, CONFIG_SOURCES, CONFIG_SECTIONS, STOP_CONFIG_SEARCH_ON_DIRS

def test_invalid_path():
    invalid_path = "/nonexistent/directory"
    result = _find_config(invalid_path)
    
    assert result[0] == invalid_path
    assert isinstance(result[1], dict)
    assert not result[1]  # The dictionary should be empty
