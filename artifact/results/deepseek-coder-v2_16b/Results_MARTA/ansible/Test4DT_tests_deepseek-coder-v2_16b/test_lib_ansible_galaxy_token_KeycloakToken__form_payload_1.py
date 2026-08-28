
import pytest
from ansible.galaxy.token import KeycloakToken


def test_init_with_valid_values():
    # Test initialization with valid values for access_token and auth_url
    token = KeycloakToken(access_token="valid_token", auth_url="https://example.com")
    assert token.access_token == "valid_token"
    assert token.auth_url == "https://example.com"

def test_default_client_id():
    # Test default client ID if not provided
    token = KeycloakToken(access_token="valid_token", auth_url="https://example.com")
    assert token.client_id == "cloud-services"

def test_form_payload():
    # Test the form payload method
    token = KeycloakToken(access_token="refresh_token", auth_url="https://sso.redhat.com/auth/")
    expected_payload = 'grant_type=refresh_token&client_id=cloud-services&refresh_token=refresh_token'
    assert token._form_payload() == expected_payload
