
import pytest
from httpie.plugins.base import AuthPlugin
import requests.auth

class TestAuthPlugin:
    def test_get_auth(self):
        plugin = AuthPlugin()
        
        with pytest.raises(NotImplementedError):
            plugin.get_auth()
