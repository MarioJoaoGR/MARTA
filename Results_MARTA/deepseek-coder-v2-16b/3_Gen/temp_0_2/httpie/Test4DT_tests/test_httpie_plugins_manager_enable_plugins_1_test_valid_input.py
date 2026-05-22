
import unittest.mock as mock
from httpie.plugins.manager import enable_plugins
from contextlib import nullcontext
from pathlib import Path
from typing import Optional, ContextManager

def test_valid_input():
    with mock.patch('sys.path', []):  # Mock the sys.path to be empty initially
        result = enable_plugins(Path('/some/directory'))
        assert isinstance(result, ContextManager)
