
from unittest.mock import patch

import pytest

from isort.api import DEFAULT_CONFIG, _config


def test_valid_input_with_kwargs():
    with patch('isort.settings._get_config_data', side_effect=FileNotFoundError("No such file or directory: 'custom.toml'")):
        with pytest.raises(FileNotFoundError):
            _config(settings_path='some/directory', settings_file='custom.toml')
