
import pytest
from unittest.mock import patch, MagicMock
from httpie.plugins.manager import PluginManager
from typing import Type, List

class AuthPlugin:
    pass

@pytest.fixture(autouse=True)
def mock_auth_plugins():
    with patch('httpie.plugins.manager.AuthPlugin', new_callable=MagicMock):
        yield

def test_valid_inputs():
    manager = PluginManager()
    auth_plugins = manager.get_auth_plugins()
    assert isinstance(auth_plugins, List)
