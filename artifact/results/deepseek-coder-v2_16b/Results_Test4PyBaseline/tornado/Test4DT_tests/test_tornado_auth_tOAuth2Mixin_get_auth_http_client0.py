# Module: tornado.auth
# test_oauth2mixin.py
from unittest import mock
import pytest
from tornado import httpclient
from tornado.auth import OAuth2Mixin

@pytest.fixture(scope="module")
def oauth2_mixin():
    class MyOAuthService(OAuth2Mixin):
        _OAUTH_AUTHORIZE_URL = "https://example.com/oauth/authorize"
        _OAUTH_ACCESS_TOKEN_URL = "https://example.com/oauth/token"
        
        def authorize_redirect(self, redirect_uri: str, client_id: str):
            super().authorize_redirect(redirect_uri=redirect_uri, client_id=client_id)

    return MyOAuthService()

def test_get_auth_http_client(oauth2_mixin):
    assert isinstance(oauth2_mixin.get_auth_http_client(), httpclient.AsyncHTTPClient)

@mock.patch('tornado.auth.OAuth2Mixin.authorize_redirect')
def test_authorize_redirect(mock_authorize_redirect, oauth2_mixin):
    redirect_uri = "https://myapp.com/callback"
    client_id = "your_client_id"
    
    oauth2_mixin.authorize_redirect(redirect_uri=redirect_uri, client_id=client_id)
    
    mock_authorize_redirect.assert_called_once_with(redirect_uri=redirect_uri, client_id=client_id)
