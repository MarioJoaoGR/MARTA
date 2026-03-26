
# Module: isort.settings
# test_isort_settings.py
import os

import pytest

from isort.exceptions import (InvalidSettingsPath, ProfileDoesNotExist,
                              UnsupportedSettings)
from isort.settings import Config


@pytest.fixture
def config():
    return Config()

def test_config_initialization(config):
    assert isinstance(config, Config)

def test_config_with_custom_settings_file(tmp_path):
    settings_file = tmp_path / "settings.ini"
    settings_file.write_text("[isort]\nsections=python\n")
    config = Config(settings_file=str(settings_file))