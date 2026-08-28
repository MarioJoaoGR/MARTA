
import pytest
from unittest.mock import patch
from mimesis.providers.cryptographic import Cryptographic

def test_valid_input_custom_entropy():
    with patch('secrets.token_urlsafe', return_value='valid_token'):
        cryptographic = Cryptographic()
        result = cryptographic.token_urlsafe(entropy=64)
        assert result == 'valid_token'

def test_invalid_input_negative_entropy():
    with patch('secrets.token_urlsafe', side_effect=ValueError):
        cryptographic = Cryptographic()
        with pytest.raises(ValueError):
            cryptographic.token_urlsafe(-1)
