
import pytest
from unittest.mock import patch
from httpie.plugins.builtin import BearerAuthPlugin
from httpie.plugins.builtin import HTTPBearerAuth

def test_edge_case_none():
    with patch('httpie.plugins.builtin.HTTPBearerAuth', autospec=True) as mock_auth:
        plugin = BearerAuthPlugin()
        auth = plugin.get_auth(raw_auth=None)
        
        assert isinstance(auth, HTTPBearerAuth)
        mock_auth.assert_called_once_with(None)
