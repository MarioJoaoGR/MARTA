
import pytest
from ansible.galaxy.token import KeycloakToken


def test_valid_initialization():
    # Test that initializing KeycloakToken with valid parameters does not raise an Exception
    token = KeycloakToken(access_token='your_refresh_token', auth_url='https://sso.redhat.com/auth/')
    assert token is not None, "KeycloakToken initialization failed"

def test_default_client_id():
    # Test that the default client_id is 'cloud-services' if not provided
    token = KeycloakToken(access_token='your_refresh_token', auth_url='https://sso.redhat.com/auth/')
    assert token.client_id == 'cloud-services', "Default client_id should be 'cloud-services'"

def test_form_payload():
    # Test that the _form_payload method constructs a valid payload string
    token = KeycloakToken(access_token='your_refresh_token', auth_url='https://sso.redhat.com/auth/')
    payload = token._form_payload()
    assert 'grant_type=refresh_token&client_id=cloud-services&refresh_token=your_refresh_token' in payload, "Form payload is incorrect"
