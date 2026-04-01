
import pytest
from unittest.mock import patch
from isort.api import _config, DEFAULT_CONFIG

def test_valid_input_with_kwargs():
    with patch('isort.settings._get_config_data', side_effect=FileNotFoundError("No such file or directory: 'custom.toml'")):
        with pytest.raises(FileNotFoundError):
            _config(settings_path='some/directory', settings_file='custom.toml')
