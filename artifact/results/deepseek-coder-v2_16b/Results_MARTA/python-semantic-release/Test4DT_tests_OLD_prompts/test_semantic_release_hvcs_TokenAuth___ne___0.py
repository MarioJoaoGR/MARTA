
import pytest
from unittest.mock import patch, MagicMock
from semantic_release.hvcs import TokenAuth
import requests

def test_tokenauth_in_http_request():
    with patch('requests.get') as mock_get:
        auth = TokenAuth(token='valid_token')
        headers = {'Authorization': f'Token {auth.token}'}
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        response = requests.get('http://example.com', headers=headers)
        
        assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"

def test_tokenauth_unauthorized_access():
    with patch('requests.get') as mock_get:
        auth = TokenAuth(token='invalid_token')
        headers = {'Authorization': f'Token {auth.token}'}
        mock_response = MagicMock()
        mock_response.status_code = 401
        mock_get.return_value = mock_response

        response = requests.get('http://example.com', headers=headers)
        
        assert response.status_code == 401, f"Expected status code 401 but got {response.status_code}"
