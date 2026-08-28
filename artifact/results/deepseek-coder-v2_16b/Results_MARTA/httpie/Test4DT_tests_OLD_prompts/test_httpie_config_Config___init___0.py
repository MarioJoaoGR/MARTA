
import pytest
from httpie.config import Config, DEFAULT_CONFIG_DIR
from pathlib import Path
from unittest.mock import patch


def test_valid_input_custom_directory():
    with patch('httpie.config.DEFAULT_CONFIG_DIR', 'default_dir'):
        config = Config('custom/path')
        assert config.directory == Path('custom/path')