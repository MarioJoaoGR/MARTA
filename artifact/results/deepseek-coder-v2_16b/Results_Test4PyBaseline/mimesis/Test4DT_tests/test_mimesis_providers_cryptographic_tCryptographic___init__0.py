
import pytest
from mimesis import Cryptographic
from uuid import UUID
from mimesis.enums import Algorithm

# Test creating an instance with a specific seed
def test_cryptographic_instance_with_seed():
    crypto_instance = Cryptographic(seed=12345)
    assert isinstance(crypto_instance, Cryptographic)

# Test generating a UUID
def test_uuid_generation():
    crypto_instance = Cryptographic(seed=12345)
    uuid_str = crypto_instance.uuid()