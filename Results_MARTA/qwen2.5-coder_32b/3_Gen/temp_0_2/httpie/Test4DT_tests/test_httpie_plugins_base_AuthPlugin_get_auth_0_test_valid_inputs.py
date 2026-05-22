
import pytest
from httpie.plugins.base import AuthPlugin

class TestAuthPlugin:
    def setup_method(self):
        self.auth_plugin = AuthPlugin()

    def test_get_auth_default_values(self):
        with pytest.raises(NotImplementedError):
            self.auth_plugin.get_auth()

    @pytest.mark.parametrize("username, password", [("user", "pass"), (None, None)])
    def test_get_auth_with_credentials(self, username, password):
        with pytest.raises(NotImplementedError):
            self.auth_plugin.get_auth(username=username, password=password)
