
from mimesis.providers.cryptographic import Cryptographic
import pytest
import secrets


def test_token_hex_custom_entropy():
    crypto = Cryptographic()
    token = crypto.token_hex(entropy=16)
    assert isinstance(token, str), "Expected a string"
    assert len(token) == 32, "Expected length of the token to be 32 for entropy of 16"