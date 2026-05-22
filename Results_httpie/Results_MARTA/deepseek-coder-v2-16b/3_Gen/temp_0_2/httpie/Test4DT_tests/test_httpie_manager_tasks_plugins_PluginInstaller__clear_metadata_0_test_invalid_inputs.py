
import pytest
from unittest.mock import patch, MagicMock
from httpie.manager.tasks.plugins import PluginInstaller
from pathlib import Path

@pytest.fixture
def mock_environment():
    env = MagicMock()
    env.config.plugins_dir = Path("/fake/plugin/directory")
    return env

@pytest.mark.parametrize("invalid_input", [None, 123, [], {}])
def test_invalid_inputs(mock_environment, invalid_input):
    with patch('httpie.manager.tasks.plugins.PluginInstaller.__init__', side_effect=TypeError("Invalid input type")):
        with pytest.raises(TypeError) as excinfo:
            PluginInstaller(env=mock_environment, debug=invalid_input)
        assert str(excinfo.value) == "Invalid input type"
