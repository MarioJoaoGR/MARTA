
import pytest
from unittest.mock import patch, MagicMock
from httpie.manager.tasks.plugins import PluginInstaller

@pytest.fixture
def mock_environment():
    env = MagicMock()
    env.config.plugins_dir = "/invalid/path"
    return env

def test_error_handling(mock_environment):
    with patch('httpie.manager.tasks.plugins.PluginInstaller.__init__', side_effect=OSError("Permission denied")):
        with pytest.raises(OSError):
            PluginInstaller(env=mock_environment, debug=True)
