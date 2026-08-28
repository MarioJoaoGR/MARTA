
import pytest
from httpie.plugins.base import AuthPlugin
import requests.auth


def test_get_auth_with_invalid_credentials():
    class MyAuthPlugin(AuthPlugin):
        def get_auth(self, username=None, password=None):
            if username == "user" and password == "pass":
                return requests.auth.HTTPBasicAuth(username, password)
            else:
                raise ValueError("Invalid credentials")
    
    plugin = MyAuthPlugin()
    with pytest.raises(ValueError):
        auth = plugin.get_auth(username="wronguser", password="wrongpass")