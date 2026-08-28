
import pytest
from ansible.galaxy.token import KeycloakToken

def test_keycloak_token_initialization():
    token = KeycloakToken(access_token='your_refresh_token', auth_url='https://sso.redhat.com/auth/')
    assert hasattr(token, 'access_token'), "KeycloakToken should have an access_token attribute"
    assert hasattr(token, 'auth_url'), "KeycloakToken should have an auth_url attribute"
    assert token.client_id == 'cloud-services', "Default client_id should be 'cloud-services'"

