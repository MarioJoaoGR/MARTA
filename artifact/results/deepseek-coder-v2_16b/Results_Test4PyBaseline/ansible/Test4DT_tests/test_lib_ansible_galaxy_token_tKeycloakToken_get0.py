
import pytest
from ansible.galaxy.token import KeycloakToken

# Test Case 1: Minimal Parameters
def test_keycloak_token_minimal_parameters():
    token = KeycloakToken(access_token='your_refresh_token', auth_url='https://sso.redhat.com/auth/', validate_certs=True)
    assert hasattr(token, 'access_token'), "Access token should be set"
    assert hasattr(token, 'auth_url'), "Auth URL should be set"
    assert hasattr(token, 'validate_certs'), "Validate certs should be set"
    assert token.client_id == 'cloud-services', "Client ID should default to 'cloud-services'"

# Test Case 2: Full Parameters
def test_keycloak_token_full_parameters():
    token = KeycloakToken(access_token='your_refresh_token', auth_url='https://sso.redhat.com/auth/', validate_certs=True, client_id='custom_client_id')
    assert hasattr(token, 'access_token'), "Access token should be set"
    assert hasattr(token, 'auth_url'), "Auth URL should be set"
    assert hasattr(token, 'validate_certs'), "Validate certs should be set"