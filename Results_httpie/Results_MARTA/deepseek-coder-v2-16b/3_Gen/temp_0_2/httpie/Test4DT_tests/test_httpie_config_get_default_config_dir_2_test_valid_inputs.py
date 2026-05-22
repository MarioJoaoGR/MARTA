
import os
from pathlib import Path
import pytest
from unittest.mock import patch
from httpie.config import get_default_config_dir, ENV_HTTPIE_CONFIG_DIR, DEFAULT_WINDOWS_CONFIG_DIR, DEFAULT_RELATIVE_LEGACY_CONFIG_DIR, ENV_XDG_CONFIG_HOME, DEFAULT_RELATIVE_XDG_CONFIG_HOME, DEFAULT_CONFIG_DIRNAME

@pytest.fixture(autouse=True)
def mock_env_variables():
    with patch.dict(os.environ, {ENV_HTTPIE_CONFIG_DIR: "/valid/config/dir"}):
        yield

def test_valid_inputs():
    config_dir = get_default_config_dir()
    assert str(config_dir) == "/valid/config/dir"
