
import pytest
from unittest.mock import patch, MagicMock
from ansible.galaxy.token import KeycloakToken
import json

def test_keycloak_token_initialization():
    token = KeycloakToken(access_token='your_refresh_token', auth_url='https://sso.redhat.com/auth/')
    assert hasattr(token, 'access_token'), "KeycloakToken should have an access_token attribute"
    assert hasattr(token, 'auth_url'), "KeycloakToken should have an auth_url attribute"
    assert token.access_token == 'your_refresh_token', "Access token initialization failed"
    assert token.auth_url == 'https://sso.redhat.com/auth/', "Auth URL initialization failed"

def test_keycloak_token_default_client_id():
    token = KeycloakToken(access_token='your_refresh_token', auth_url='https://sso.redhat.com/auth/')
    assert token.client_id == 'cloud-services', "Default client ID should be cloud-services"

def test_keycloak_token_get_method():
    with patch('ansible.galaxy.token.open_url') as mock_open_url:
        mock_response = MagicMock()
        mock_response.read.return_value = '{"access_token": "retrieved_token"}'
        mock_open_url.return_value = mock_response

        token = KeycloakToken(access_token='your_refresh_token', auth_url='https://sso.redhat.com/auth/')
        assert token.get() == 'retrieved_token', "The get method should return the retrieved access token"
