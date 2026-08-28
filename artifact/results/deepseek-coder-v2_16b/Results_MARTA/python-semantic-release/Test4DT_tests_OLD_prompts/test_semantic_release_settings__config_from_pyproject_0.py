
import pytest
from unittest.mock import patch
from semantic_release.settings import _config_from_pyproject
import os
import tomlkit
from tomlkit.exceptions import TOMLKitError



def test_non_existent_file():
    with patch('os.path.isfile', return_value=False):
        config = _config_from_pyproject("nonexistent/path/to/pyproject.toml")
        assert config == {}