
import pytest
from ansible.galaxy.token import KeycloakToken

# Test case for creating a KeycloakToken instance with all parameters provided
def test_keycloak_token_all_params():
    token = KeycloakToken(access_token='your_access_token', auth_url='https://sso.redhat.com/auth/', validate_certs=True)
    assert token.access_token == 'your_access_token'
    assert token.auth_url == 'https://sso.redhat.com/auth/'
    assert token.validate_certs is True
    assert token.client_id == 'cloud-services'

# Test case for creating a KeycloakToken instance without client_id (it should default to 'cloud-services')
def test_keycloak_token_no_client_id():
    token = KeycloakToken(access_token='your_access_token', auth_url='https://sso.redhat.com/auth/', validate_certs=True)
    assert token.access_token == 'your_access_token'
    assert token.auth_url == 'https://sso.redhat.com/auth/'
    assert token.validate_certs is True