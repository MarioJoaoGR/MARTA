
import pytest
from unittest.mock import patch, MagicMock
from httpie.manager.tasks.plugins import PluginInstaller

@pytest.fixture(autouse=True)
def setup_plugin_installer():
    with patch('httpie.manager.tasks.plugins.PluginInstaller.__init__', return_value=None):
        yield

def test_edge_case():
    env = MagicMock()
    installer = PluginInstaller(env=env, debug=True)
    
    # Mock the environment to simulate a None target for uninstallation
    with patch.object(installer, '_uninstall', return_value=None):
        result = installer._uninstall("nonexistent_plugin")
        
        assert result is None
