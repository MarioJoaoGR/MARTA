
import os
from isort.exceptions import InvalidSettingsPath
from unittest.mock import patch
import pytest

@pytest.mark.parametrize("valid_path", [('valid_file.cfg'), ('/path/to/valid_file.cfg')])
def test_valid_input(valid_path):
    with patch('os.path.exists', return_value=True):
        assert os.path.exists(valid_path) is True
        try:
            raise InvalidSettingsPath(valid_path)
        except InvalidSettingsPath as e:
            assert str(e) == f"isort was told to use the settings_path: {valid_path} as the base directory or file that represents the starting point of config file discovery, but it does not exist."
