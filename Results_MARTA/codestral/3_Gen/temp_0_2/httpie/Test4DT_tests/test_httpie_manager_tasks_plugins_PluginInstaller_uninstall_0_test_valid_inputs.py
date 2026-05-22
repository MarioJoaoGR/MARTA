
import pytest
from unittest.mock import patch
from httpie.manager.tasks.plugins import PluginInstaller, Environment

@pytest.fixture
def mock_environment():
    # Create a mock environment for testing
    env = Environment(config={}, stderr=None)
    return env

def test_valid_inputs(mock_environment):
    with patch('httpie.manager.tasks.plugins.Environment', return_value=mock_environment):
        installer = PluginInstaller(env=mock_environment, debug=False)
        assert hasattr(installer, 'env')
        assert hasattr(installer, 'dir')
        assert hasattr(installer, 'debug')
