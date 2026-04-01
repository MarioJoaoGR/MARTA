
import pytest
from isort.settings import Config, InvalidSettingsPath
import subprocess
from pathlib import Path
import os

def test_invalid_settings_path():
    with pytest.raises(InvalidSettingsPath):
        Config(settings_path="nonexistentdirectory")
