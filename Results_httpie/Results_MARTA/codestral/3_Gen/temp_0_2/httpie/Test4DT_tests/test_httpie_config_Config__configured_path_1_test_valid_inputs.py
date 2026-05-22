
import pytest
from httpie.config import Config
from pathlib import Path
from unittest.mock import patch

def test_valid_inputs():
    with patch('httpie.config.DEFAULT_CONFIG_DIR', '/test/directory'):
        config = Config()
        result = config._configured_path('test_option', 'default_file')
        assert isinstance(result, Path)
