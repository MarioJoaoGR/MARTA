
import pytest
from pathlib import Path
from thefuck.conf import const

class Settings:
    def __init__(self):
        self.user_dir = None

    def _init_settings_file(self):
        settings_path = self.user_dir.joinpath('settings.py')
        if not settings_path.is_file():
            with open(settings_path, 'w') as f:
                for setting in const.DEFAULT_SETTINGS.items():
                    f.write(u'# {} = {}\n'.format(*setting))
    
@pytest.fixture
def settings():
    settings = Settings()
    return settings

def test_init_settings_file_with_user_dir(tmp_path):
    # Arrange: Set up the user directory and call the method under test
    settings = Settings()
    settings.user_dir = tmp_path
    assert not (tmp_path / 'settings.py').is_file(), "File should not exist initially"
    
    # Act: Call the method to initialize the settings file
    settings._init_settings_file()
    
    # Assert: Check that the file has been created with default settings
    assert (tmp_path / 'settings.py').is_file(), "File should be created"
    with open(tmp_path / 'settings.py', 'r') as f:
        content = f.read()
        for setting in const.DEFAULT_SETTINGS.items():
            assert u'# {} = {}\n'.format(*setting) in content, "Default settings should be written to the file"

def test_init_settings_file_existing_file(tmp_path):
    # Create a mock settings file with default content
    settings_path = tmp_path / 'settings.py'
    settings_path.write_text('\n'.join([u'# {} = {}'.format(*setting) for setting in const.DEFAULT_SETTINGS.items()]))
    
    # Initialize the Settings instance with this path
    settings = Settings()
    settings.user_dir = tmp_path
    
    # Act: Call the method to initialize the settings file (should do nothing if file exists)
    settings._init_settings_file()
    
    # Assert: Check that the file still exists and no new file is created
    assert settings_path.is_file(), "File should already exist"
