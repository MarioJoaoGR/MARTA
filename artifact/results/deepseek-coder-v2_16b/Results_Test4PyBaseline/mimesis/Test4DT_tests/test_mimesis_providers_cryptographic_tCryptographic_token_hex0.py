# Module: mimesis.providers.cryptographic
import pytest
from mimesis.providers.cryptographic import Cryptographic

# Test cases for the token_hex method in the Cryptographic class
def test_token_hex_default_entropy():
    crypto = Cryptographic()
    token = crypto.token_hex()
    assert isinstance(token, str), "Expected a string result"
    assert len(token) == 64, "Expected default entropy to be 32 bytes (64 hex characters)"

def test_token_hex_specified_entropy():
    crypto = Cryptographic()
    token = crypto.token_hex(16)
    assert isinstance(token, str), "Expected a string result"
    assert len(token) == 32, "Expected entropy of 16 bytes (32 hex characters)"

def test_token_hex_entropy_none():
    crypto = Cryptographic()
    with pytest.raises(TypeError):
        token = crypto.token_hex(None)
