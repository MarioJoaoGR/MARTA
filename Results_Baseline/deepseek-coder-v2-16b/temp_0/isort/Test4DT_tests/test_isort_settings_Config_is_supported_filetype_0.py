
# Module: isort.settings
# test_isort_settings.py
import os
import stat

import pytest

from isort.settings import Config


@pytest.fixture
def config():
    return Config()

def test_config_initialization(config):
    assert isinstance(config, Config)

def test_is_supported_filetype_with_valid_extension(config):
    # Assuming .py is a valid extension for this example
    assert config.is_supported_filetype("example.py") == True

def test_is_supported_filetype_with_invalid_extension(config):
    # Assuming .lock is an invalid extension for this example
    assert config.is_supported_filetype("example.lock") == False

def test_is_supported_filetype_with_editor_backup_file(config):
    # Assuming editor backup files are not supported
    assert config.is_supported_filetype("example.py~") == False

def test_is_supported_filetype_with_shebang(config):
    # Assuming a file with a shebang line is supported
    with open("example.py", "w") as fp:
        fp.write("#!/usr/bin/env python\nprint('Hello, World!')")
    assert config.is_supported_filetype("example.py") == True
