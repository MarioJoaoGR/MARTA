
import pytest
from unittest.mock import patch, MagicMock
from thefuck.logs import settings, color

# Test for default usage with colored output enabled
def test_color_default_usage():
    with patch('thefuck.logs.settings', MockSettings):
        settings.no_colors = False
        assert color('red') == 'red'

# Test for disabled output when colored output is enabled

# Mocking the settings module to avoid NameError
class MockSettings:
    no_colors = False  # or True depending on your preference

@pytest.fixture(autouse=True)
def mock_settings():
    with patch('thefuck.logs.settings', MockSettings):
        yield