
import pytest
from pathlib import Path
from httpie.plugins.manager import _load_directories
from unittest.mock import patch, MagicMock

def test_invalid_input():
    with pytest.raises(TypeError):
        # Test that _load_directories raises a TypeError when given an invalid input type (e.g., string)
        for _ in _load_directories("invalid_input"):
            pass
