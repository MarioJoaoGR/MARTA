# Module: mimesis.providers.cryptographic
import pytest
from mimesis.providers.cryptographic import Cryptographic
import secrets

# Test cases for the token_bytes method in the Cryptographic class
def test_token_bytes_default_entropy():
    crypt = Cryptographic()
    random_bytes = crypt.token_bytes()
    assert isinstance(random_bytes, bytes), "Expected a byte string"
    assert len(random_bytes) == 32, "Expected default entropy to be 32 bytes"

def test_token_bytes_specified_entropy():
    crypt = Cryptographic()
    random_bytes = crypt.token_bytes(16)
    assert isinstance(random_bytes, bytes), "Expected a byte string"
    assert len(random_bytes) == 16, "Expected specified entropy to be 16 bytes"

def test_token_bytes_direct_call():
    crypt = Cryptographic()
    random_bytes = crypt.token_bytes(entropy=16)
    assert isinstance(random_bytes, bytes), "Expected a byte string"
    assert len(random_bytes) == 16, "Expected specified entropy to be 16 bytes"
