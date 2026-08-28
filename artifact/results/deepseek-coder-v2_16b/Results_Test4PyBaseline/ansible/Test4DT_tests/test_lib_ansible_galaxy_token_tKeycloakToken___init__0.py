# Module: ansible.galaxy.token
# test_keycloak_token.py
from ansible.galaxy.token import KeycloakToken

def test_basic_initialization():
    token = KeycloakToken(access_token='your_access_token', auth_url='https://sso.redhat.com/auth/', validate_certs=True)
    assert token.access_token == 'your_access_token'
    assert token.auth_url == 'https://sso.redhat.com/auth/'
    assert token.validate_certs is True
    assert token.client_id == 'cloud-services'

def test_default_client_id():
    token = KeycloakToken(access_token='your_access_token', auth_url='https://sso.redhat.com/auth/', validate_certs=True, client_id=None)
    assert token.access_token == 'your_access_token'
    assert token.auth_url == 'https://sso.redhat.com/auth/'
    assert token.validate_certs is True
    assert token.client_id == 'cloud-services'

def test_custom_client_id():
    token = KeycloakToken(access_token='your_access_token', auth_url='https://sso.redhat.com/auth/', validate_certs=True, client_id='custom_client_id')
    assert token.access_token == 'your_access_token'
    assert token.auth_url == 'https://sso.redhat.com/auth/'
    assert token.validate_certs is True
    assert token.client_id == 'custom_client_id'
