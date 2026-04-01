
import pytest
from isort import Config
from isort.exceptions import InvalidSettingsPath

def test_invalid_inputs():
    # Test case 1: Missing settings file path and profile name
    with pytest.raises(InvalidSettingsPath):
        Config(settings_file="", settings_path="non_existent_directory")
    
    # Test case 2: Incorrect or non-existent configuration file path
    with pytest.raises(FileNotFoundError):
        Config(settings_file="nonexistent.ini")
