
import pytest
from unittest.mock import patch
from httpie.plugins.builtin import DigestAuthPlugin
import requests

def test_valid_input():
    with patch('httpie.plugins.builtin.DigestAuthPlugin.get_auth', return_value=requests.auth.HTTPDigestAuth("username", "password")):
        auth_plugin = DigestAuthPlugin()
        result = auth_plugin.get_auth("username", "password")
        assert isinstance(result, requests.auth.HTTPDigestAuth)
