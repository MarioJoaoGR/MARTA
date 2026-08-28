
import pytest
from mimesis import Cryptographic
from mimesis.enums import Algorithm
import hashlib
from uuid import UUID

# Fixture to create a Cryptographic instance with a specific seed
@pytest.fixture(scope="module")
def crypto_instance():
    return Cryptographic(seed=12345)

# Test for generating a random UUID4 as an UUID object
def test_uuid_as_object(crypto_instance):
    uuid_obj = crypto_instance.uuid()
    assert isinstance(UUID(uuid_obj), UUID)  # Ensure it's a valid UUID object

# Test for generating a hash using the default algorithm (SHA256)
def test_hash_default(crypto_instance):
    hashed = crypto_instance.hash()
    assert isinstance(hashed, str)  # Ensure it's a string representation of the hash

# Test for generating a hash using a specific algorithm (e.g., SHA1)
def test_hash_specific_algorithm(crypto_instance):
    hashed = crypto_instance.hash(algorithm=Algorithm.SHA1)
    assert isinstance(hashed, str)  # Ensure it's a string representation of the hash

# Test for generating random bytes
def test_token_bytes(crypto_instance):
    random_bytes = crypto_instance.token_bytes(16)
    assert len(random_bytes) == 16  # Ensure the length is correct

# Test for generating a random hexadecimal string
def test_token_hex(crypto_instance):
    hex_str = crypto_instance.token_hex()
    assert isinstance(hex_str, str)  # Ensure it's a string

# Test for generating a secure and URL-safe token
def test_token_urlsafe(crypto_instance):
    token = crypto_instance.token_urlsafe()