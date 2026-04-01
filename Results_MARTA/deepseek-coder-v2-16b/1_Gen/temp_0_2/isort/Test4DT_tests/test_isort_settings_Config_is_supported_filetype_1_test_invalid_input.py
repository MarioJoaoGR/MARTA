
import os
from isort.settings import Config
import pytest

def test_invalid_input():
    with pytest.raises(FileNotFoundError):
        config = Config(settings_file="non_existent_file.toml")
