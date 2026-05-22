
import pytest
from unittest.mock import patch
from httpie.config import Config, DEFAULT_CONFIG_DIR

def test_invalid_input():
    with patch('httpie.config.DEFAULT_CONFIG_DIR', 'default_dir'):
        with pytest.raises(TypeError):
            Config(directory=None)
