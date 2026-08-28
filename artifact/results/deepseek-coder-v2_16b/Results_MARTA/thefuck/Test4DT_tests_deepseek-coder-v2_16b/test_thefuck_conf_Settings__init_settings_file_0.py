
import pytest
from pathlib import Path
from unittest.mock import patch
from thefuck.conf import const

class Settings:
    def __init__(self, user_dir):
        self.user_dir = Path(user_dir)

    def _init_settings_file(self):
        settings_path = self.user_dir.joinpath('settings.py')
        if not settings_path.is_file():
            with settings_path.open(mode='w') as settings_file:
                settings_file.write(const.SETTINGS_HEADER)
                for setting in const.DEFAULT_SETTINGS.items():
                    settings_file.write(u'# {} = {}\n'.format(*setting))

@pytest.fixture
def valid_settings():
    user_dir = Path('test_user_dir')
    if not user_dir.exists():
        user_dir.mkdir()
    return Settings(user_dir)

@pytest.fixture
def missing_file_settings():
    user_dir = Path('test_missing_dir')
    if not user_dir.exists():
        user_dir.mkdir()
    return Settings(user_dir)

@pytest.fixture
def existing_file_settings():
    user_dir = Path('test_existing_dir')
    if not user_dir.exists():
        user_dir.mkdir()
    settings_path = user_dir / 'settings.py'
    with settings_path.open(mode='w') as f:
        f.write('# Existing file content\n')
    return Settings(user_dir)

def test_valid_input(valid_settings):
    valid_settings._init_settings_file()
    settings_path = valid_settings.user_dir / 'settings.py'
    assert settings_path.is_file()
    with settings_path.open() as f:
        content = f.read()
        assert const.SETTINGS_HEADER in content
        for setting, value in const.DEFAULT_SETTINGS.items():
            assert u'# {} = {}'.format(setting, value) in content

def test_missing_file(missing_file_settings):
    missing_file_settings._init_settings_file()
    settings_path = missing_file_settings.user_dir / 'settings.py'
    assert settings_path.is_file()
    with settings_path.open() as f:
        content = f.read()
        assert const.SETTINGS_HEADER in content
        for setting, value in const.DEFAULT_SETTINGS.items():
            assert u'# {} = {}'.format(setting, value) in content

def test_existing_file(existing_file_settings):
    with patch('builtins.open', create=True) as mock_open:
        existing_file_settings._init_settings_file()
        mock_open.assert_not_called()
