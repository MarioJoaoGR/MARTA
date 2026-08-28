
import os
from pathlib import Path
from warnings import warn
import pytest
from thefuck.conf import Settings

@pytest.fixture
def settings():
    return Settings()

def test_get_user_dir_path_deprecated(settings, monkeypatch):
    # Mock environment variable to simulate old path existence
    monkeypatch.setenv('XDG_CONFIG_HOME', '~/.config')
    legacy_user_dir = Path('~', '.thefuck').expanduser()
    assert not legacy_user_dir.is_dir()
    
    # Test the method when legacy path does not exist
    result = settings._get_user_dir_path()
    expected_path = Path('~/.config/thefuck').expanduser()
    assert str(result) == str(expected_path)