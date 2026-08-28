
# Module: ansible.galaxy.token
# test_keycloak_token.py
from ansible.galaxy.token import KeycloakToken
import pytest  # Importing pytest at the beginning of the file as per pylint suggestion

def test_default_client_id():
    token = KeycloakToken(access_token='your_access_token', auth_url='https://sso.redhat.com/auth/', validate_certs=True)
    assert token.access_token == 'your_access_token'
    assert token.auth_url == 'https://sso.redhat.com/auth/'
    assert token.validate_certs is True