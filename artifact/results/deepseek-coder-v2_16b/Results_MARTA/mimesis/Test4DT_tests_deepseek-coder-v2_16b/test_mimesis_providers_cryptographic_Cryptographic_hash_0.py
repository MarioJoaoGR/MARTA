
import pytest
from mimesis.providers.cryptographic import Cryptographic
from mimesis.enums import Algorithm
import hashlib

@pytest.fixture(scope="module")
def cryptographic_instance():
    return Cryptographic()


def test_valid_input_specified_algorithm(cryptographic_instance):
    hashed_value = cryptographic_instance.hash(algorithm=Algorithm.SHA256)
    assert isinstance(hashed_value, str), "Expected a string hash"
    assert len(hashed_value) == 64, f"Expected SHA-256 hash length to be 64, but got {len(hashed_value)}"
