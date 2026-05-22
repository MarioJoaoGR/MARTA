
import pytest
from unittest.mock import patch
from httpie.plugins.builtin import DigestAuthPlugin

def test_none_input():
    auth_plugin = DigestAuthPlugin()
    with patch('httpie.plugins.builtin.requests.auth.HTTPDigestAuth', autospec=True) as mock_digest_auth:
        username = None
        password = None
        auth_plugin.get_auth(username, password)
        mock_digest_auth.assert_called_once_with(username, password)
