
import pytest
from unittest.mock import patch
from mimesis.providers.cryptographic import Cryptographic

def test_valid_entropy():
    with patch('mimesis.providers.cryptographic.secrets.token_hex', return_value='d41d8cd98f00b204e9800998ecf8427e'):
        crypto = Cryptographic()
        assert crypto.token_hex(entropy=32) == 'd41d8cd98f00b204e9800998ecf8427e'
