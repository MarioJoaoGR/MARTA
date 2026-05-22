
import pytest
from pathlib import Path
from httpie.plugins.manager import _load_directories
from unittest.mock import patch, MagicMock

def test_invalid_input():
    with patch('httpie.plugins.manager._load_directories') as mock_load_directories:
        site_dirs = [Path('/path/to/site1'), Path('/path/to/site2')]
        mock_generator = MagicMock()
        mock_load_directories.return_value = mock_generator
        
        with pytest.raises(TypeError):
            for _ in _load_directories(site_dirs):
                pass
