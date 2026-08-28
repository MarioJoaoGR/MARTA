
import pytest
from ansible.galaxy.token import KeycloakToken

def test_valid_initialization():
    token = KeycloakToken(access_token='your_refresh_token', auth_url='https://sso.redhat.com/auth/')
    assert token.access_token == 'your_refresh_token'
    assert token.auth_url == 'https://sso.redhat.com/auth/'
    assert token.validate_certs is True
    assert token.client_id == 'cloud-services'

def test_initialization_with_default_client_id():
    token = KeycloakToken(access_token='your_refresh_token', auth_url='https://sso.redhat.com/auth/')
    assert token.client_id == 'cloud-services'

def test_initialization_with_custom_client_id():
    token = KeycloakToken(access_token='your_refresh_token', auth_url='https://sso.redhat.com/auth/', client_id='custom_client_id')
    assert token.client_id == 'custom_client_id'

def test_initialization_with_certificate_validation_disabled():
    token = KeycloakToken(access_token='your_refresh_token', auth_url='https://sso.redhat.com/auth/', validate_certs=False)
    assert token.validate_certs is False
