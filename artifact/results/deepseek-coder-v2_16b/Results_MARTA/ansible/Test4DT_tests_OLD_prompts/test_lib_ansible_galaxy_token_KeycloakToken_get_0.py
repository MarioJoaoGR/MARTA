
import pytest
from unittest.mock import patch, MagicMock
from ansible.galaxy.token import KeycloakToken



@patch('ansible.galaxy.token.open_url')
def test_get(mock_open_url):
    mock_response = MagicMock()
    mock_response.read.return_value = '{"access_token": "test_token"}'
    mock_open_url.return_value = mock_response

    token = KeycloakToken(access_token=None, auth_url='https://example.com')
    assert token.get() == 'test_token'