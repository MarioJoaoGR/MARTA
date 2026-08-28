
# Module: httpie.plugins.base
# test_auth_plugins.py
from httpie.plugins.base import AuthPlugin
import requests.auth
import pytest

@pytest.fixture(scope="module")
def basic_auth_plugin():
    return AuthPlugin()

@pytest.mark.parametrize("username, password", [
    ("user", "pass"),
    (None, None),  # Test without providing credentials
])
def test_get_auth_with_credentials(basic_auth_plugin, username, password):
    with pytest.raises(NotImplementedError):
        basic_auth_plugin.get_auth(username=username, password=password)

@pytest.mark.parametrize("username, password", [
    ("user", "pass"),
    (None, None),  # Test without providing credentials
])
def test_get_auth_with_custom_credentials(basic_auth_plugin, username, password):
    with pytest.raises(NotImplementedError):
        basic_auth_plugin.get_auth(username=username, password=password)
