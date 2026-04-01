
import pytest
from isort.settings import Config
from isort.exceptions import UnsupportedSettings

def test_valid_case(tmpdir):
    # Create a temporary file with the expected content for testing
    config_file = tmpdir / "custom_config.ini"
    config_file.write("[isort]\n# This is a comment\ncountry = USA")
    
    # Update the valid_config to include the path to the temporary file
    valid_config = {
        'config_overrides': {'quiet': True},
        'settings_file': str(config_file)
    }
    
    # Initialize Config with the updated configuration
    with pytest.raises(UnsupportedSettings):
        config = Config(**valid_config)
