
# Module: ansible.galaxy.token
# test_keycloak_token.py
from ansible.galaxy.token import KeycloakToken
import pytest  # Added this import for the raised exception in the last test case

def test_initialization_with_all_parameters():
    token = KeycloakToken(access_token='your_access_token', auth_url='https://sso.redhat.com/auth/', validate_certs=True)
    assert token.access_token == 'your_access_token'
    assert token.auth_url == 'https://sso.redhat.com/auth/'
    assert token.validate_certs is True
    assert token.client_id == 'cloud-services'

def test_initialization_without_client_id():
    token = KeycloakToken(access_token='your_access_token', auth_url='https://sso.redhat.com/auth/', validate_certs=True)
    assert token.access_token == 'your_access_token'
    assert token.auth_url == 'https://sso.redhat.com/auth/'
    assert token.validate_certs is True
    assert token.client_id == 'cloud-services'

def test_initialization_with_custom_client_id():
    token = KeycloakToken(access_token='your_access_token', auth_url='https://sso.redhat.com/auth/', validate_certs=True, client_id='custom_client_id')
    assert token.access_token == 'your_access_token'
    assert token.auth_url == 'https://sso.redhat.com/auth/'
    assert token.validate_certs is True