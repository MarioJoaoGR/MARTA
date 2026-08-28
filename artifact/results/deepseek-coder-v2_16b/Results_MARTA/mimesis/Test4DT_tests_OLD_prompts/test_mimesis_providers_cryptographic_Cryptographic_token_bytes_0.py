
import pytest
from mimesis.providers.cryptographic import Cryptographic
from unittest.mock import patch, MagicMock

def test_token_bytes():
    with patch('mimesis.providers.cryptographic.secrets') as mock_secrets:
        cryptographic = Cryptographic()
        entropy = 32
        expected_output = b'0123456789abcdef0123456789abcdef'  # Example output for 16 bytes
        
        mock_secrets.token_bytes.return_value = expected_output
        
        result = cryptographic.token_bytes(entropy)
        
        assert result == expected_output
        mock_secrets.token_bytes.assert_called_once_with(entropy)
