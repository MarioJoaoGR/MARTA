
import pytest
from unittest.mock import patch
from httpie.output.formatters.colors import ColorFormatter, Environment, DEFAULT_STYLE, AUTO_STYLE

@pytest.fixture
def env():
    return Environment()

@pytest.fixture
def invalid_color_scheme():
    return 'invalid-color'

def test_invalid_input(env, invalid_color_scheme):
    with patch('httpie.output.formatters.colors.ColorFormatter.__init__', side_effect=ValueError("Invalid color scheme")):
        with pytest.raises(ValueError) as excinfo:
            ColorFormatter(env=env, explicit_json=True, color_scheme=invalid_color_scheme)
        assert str(excinfo.value) == "Invalid color scheme"
