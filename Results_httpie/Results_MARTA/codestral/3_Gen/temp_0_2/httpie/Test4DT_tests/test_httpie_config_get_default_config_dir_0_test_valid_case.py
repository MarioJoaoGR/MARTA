
import os
from pathlib import Path
import pytest
from unittest.mock import patch, MagicMock
from httpie.config import get_default_config_dir

@pytest.fixture(autouse=True)
def mock_environment_variables():
    with patch.dict(os.environ, {
        'XDG_CONFIG_HOME': '/home/user/.config',
        'HTTPIE_CONFIG_DIR': '/custom/httpie'
    }):
        yield

@pytest.mark.skipif(os.name != 'nt', reason="This test is for Windows only")
def test_valid_case():
    with patch('httpie.config.is_windows', return_value=True):
        config_dir = get_default_config_dir()
        assert str(config_dir) == '/custom/httpie'
