
import pytest
from unittest.mock import MagicMock
import requests

def _get_confirm_token(resp):
    for key, value in resp.cookies.items():
        if key.startswith('download_warning'):
            return value
    return None

def test_invalid_input():
    # Create a mock response object with cookies
    mock_response = MagicMock()
    mock_response.cookies = {}  # No cookies in the response
    
    # Call the function with the mock response
    result = _get_confirm_token(mock_response)
    
    # Assert that the result is None, as there are no cookies to check
    assert result == None
