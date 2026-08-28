
import pytest
from mimesis.providers.cryptographic import Cryptographic
import secrets

# Test the default entropy case
def test_default_entropy():
    crypto_instance = Cryptographic()
    token = crypto_instance.token_urlsafe()
    assert isinstance(token, str), "Expected a string type"
    assert len(token) == 43, "Expected length of 43 characters for default entropy"

# Test with specified entropy
def test_specified_entropy():
    crypto_instance = Cryptographic()
    token = crypto_instance.token_urlsafe(entropy=16)
    assert isinstance(token, str), "Expected a string type"