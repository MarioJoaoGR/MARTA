
import pytest
from unittest.mock import patch
from httpie.plugins.builtin import DigestAuthPlugin

def test_valid_input():
    with patch('httpie.plugins.builtin.DigestAuthPlugin') as mock_plugin:
        # Set up the mock to return a specific instance of DigestAuthPlugin
        mock_instance = mock_plugin.return_value
        
        # Configure the mock instance for testing
        username = 'validUser'
        password = 'validPass'
        expected_auth = mock_instance.get_auth.return_value
        
        # Call the function under test
        result = mock_instance.get_auth(username, password)
        
        # Assert that the correct method was called with the right arguments
        mock_instance.get_auth.assert_called_once_with(username, password)
        
        # Assert that the result is the expected authentication object
        assert result == expected_auth
