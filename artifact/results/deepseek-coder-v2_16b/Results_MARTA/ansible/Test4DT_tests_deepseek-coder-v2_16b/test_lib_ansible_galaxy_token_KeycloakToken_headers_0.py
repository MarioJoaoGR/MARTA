
import pytest
from ansible.galaxy.token import KeycloakToken

def test_valid_input():
    access_token = "your_access_token"
    auth_url = "https://sso.redhat.com/auth/"
    token = KeycloakToken(access_token=access_token, auth_url=auth_url)
    
    assert token.access_token == access_token
    assert token.auth_url == auth_url
    assert token.client_id == 'cloud-services'

