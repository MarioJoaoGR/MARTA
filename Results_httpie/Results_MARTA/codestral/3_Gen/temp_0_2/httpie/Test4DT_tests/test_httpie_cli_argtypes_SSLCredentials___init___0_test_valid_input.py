
import pytest
from unittest.mock import patch
from httpie.cli.argtypes import SSLCredentials

def test_valid_input():
    with patch('httpie.cli.argtypes.SSLCredentials', autospec=True) as mock_ssl:
        # Arrange
        expected_passphrase = "my_passphrase"
        mock_ssl.return_value = mock_ssl
        
        # Act
        ssl_credentials = SSLCredentials(expected_passphrase)
        
        # Assert
        assert ssl_credentials.value == expected_passphrase
