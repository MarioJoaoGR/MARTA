
import pytest
from unittest.mock import MagicMock, patch
from pathlib import Path
from httpie.manager.tasks.plugins import PluginInstaller

@pytest.fixture(autouse=True)
def setup_plugin_installer():
    with patch('httpie.manager.tasks.plugins.Environment', return_value=MagicMock(config=MagicMock(plugins_dir=Path('test_dir')))):
        yield

def test_valid_inputs():
    env = MagicMock()
    env.config.plugins_dir = Path('test_dir')
    installer = PluginInstaller(env=env, debug=True)
    assert installer.debug is True
    assert isinstance(installer.dir, Path)
