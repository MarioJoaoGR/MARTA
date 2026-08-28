
import pytest
from unittest.mock import patch, MagicMock
from semantic_release.hvcs import TokenAuth
import requests

# Test for basic token authentication in a request
@patch('requests.get')
def test_tokenauth_request(mock_get):
    token = 'your_token_here'
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_get.return_value = mock_response
    
    auth = TokenAuth(token)
    response = requests.get("https://api.example.com/data", auth=auth)
    
    assert response.status_code == 200

# Test for token authentication in a request with a custom domain
@patch('requests.get')
def test_tokenauth_request_custom_domain(mock_get):
    token = 'your_token_here'
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_get.return_value = mock_response
    
    auth = TokenAuth(token)
    response = requests.get("https://api.customdomain.com/data", auth=auth)
    
    assert response.status_code == 200
