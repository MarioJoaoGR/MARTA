
from pathlib import Path
from typing import Any
from unittest.mock import patch
import pytest
from isort.api import _config, DEFAULT_CONFIG

@pytest.mark.parametrize(
    "path, config_kwargs, expected",
    [
        (Path("some/path"), {}, DEFAULT_CONFIG),
        (None, {"settings_file": "custom_config.toml"}, DEFAULT_CONFIG),
        (None, {"settings_path": Path("some/path")}, DEFAULT_CONFIG),
        (Path("some/path"), {"settings_file": "custom_config.toml"}, DEFAULT_CONFIG),
    ],
)
@patch('isort.api._config')
def test_valid_inputs(mock_config, path, config_kwargs, expected):
    with patch('isort.api.Config', return_value=expected):
        result = _config(path=path, **config_kwargs)
        assert result == expected
