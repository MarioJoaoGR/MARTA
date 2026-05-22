
import pytest
from unittest.mock import patch, MagicMock
from httpie.manager.tasks.plugins import PluginInstaller

@pytest.fixture(autouse=True)
def mock_environment():
    with patch('httpie.manager.tasks.plugins.Environment', autospec=True):
        yield

def test_invalid_input():
    env = MagicMock()
    installer = PluginInstaller(env=env, debug=False)
    
    # Test raising ValueError for invalid input
    with pytest.raises(ValueError):
        installer._uninstall('')
