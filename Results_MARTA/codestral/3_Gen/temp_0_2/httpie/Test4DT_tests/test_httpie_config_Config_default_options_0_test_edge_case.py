
import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock
from httpie.config import Config

def test_edge_case():
    with patch('httpie.config.DEFAULT_CONFIG_DIR', new=Path('/nonexistent/directory')):
        config = Config()
        assert not (config.directory / 'config.json').exists(), "Expected non-existent directory to prevent file creation"
