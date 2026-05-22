
from httpie.manager.tasks.plugins import PluginInstaller, ExitStatus
from unittest.mock import patch, MagicMock
import pytest

@pytest.fixture
def setup_installer():
    env = MagicMock()
    env.stdout = MagicMock()
    installer = PluginInstaller(env=env, debug=False)
    return installer, env

def test_edge_case_none(setup_installer):
    installer, env = setup_installer
    
    with patch('httpie.manager.tasks.plugins.PluginInstaller._install', return_value=(None, ExitStatus.SUCCESS)):
        result = installer.install(['plugin1'])
        
        assert result == ExitStatus.SUCCESS
        env.stdout.write.assert_called_with("Installing plugin1...\n")
