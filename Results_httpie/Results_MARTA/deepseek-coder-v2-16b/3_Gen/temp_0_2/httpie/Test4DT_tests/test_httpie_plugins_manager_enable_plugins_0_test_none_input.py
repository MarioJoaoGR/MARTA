
import pytest
from httpie.plugins.manager import enable_plugins
from contextlib import nullcontext
from pathlib import Path
from unittest.mock import patch, MagicMock

def test_none_input():
    with patch('httpie.plugins.manager.enable_plugins') as mock_enable_plugins:
        mock_enable_plugins.return_value = nullcontext()
        ctx = enable_plugins(None)
        assert isinstance(ctx, nullcontext)
