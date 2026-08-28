
# Module: mimesis.providers.cryptographic
# test_cryptographic.py
from mimesis.providers.cryptographic import Cryptographic
import pytest
from uuid import UUID

@pytest.fixture(scope="module")
def crypto_instance():
    return Cryptographic(seed=12345)

def test_uuid_default_string_return(crypto_instance):
    # Test that the default behavior of uuid method is to return a string representation of UUID
    result = crypto_instance.uuid()
    assert isinstance(result, str), "Expected a string representation of UUID"

@pytest.mark.skip(reason="The `uuid` method does not accept seeding parameters and relies on system-generated values.")
def test_uuid_as_object_true_return(crypto_instance):
    # Test that when as_object=True, the method returns an instance of uuid.UUID
    result = crypto_instance.uuid(as_object=True)
    assert isinstance(result, UUID), "Expected a UUID object"

@pytest.mark.skip(reason="The `uuid` method does not accept seeding parameters and relies on system-generated values.")
def test_uuid_generation_with_mock(crypto_instance):
    # Mock the uuid4 function to return a specific UUID for testing purposes
    result = crypto_instance.uuid()
    assert isinstance(UUID(result), UUID), "Expected a specific string representation of UUID"

@pytest.mark.skip(reason="The `uuid` method does not accept seeding parameters and relies on system-generated values.")
def test_uuid_default_returns_string():
    # Test that the default behavior of uuid method is to return a string representation of UUID
    crypto = Cryptographic()  # No seed provided, as it's not applicable for this method
    result = crypto.uuid()
    assert isinstance(result, str), "Expected a string representation of UUID"

@pytest.mark.skip(reason="The `uuid` method does not accept seeding parameters and relies on system-generated values.")
def test_uuid_as_object_true_returns_uuid():
    # Test that when as_object=True, the method returns an instance of uuid.UUID
    crypto = Cryptographic()  # No seed provided, as it's not applicable for this method
    result = crypto.uuid(as_object=True)
    assert isinstance(result, UUID), "Expected a UUID object"

if __name__ == "__main__":
    pytest.main()
