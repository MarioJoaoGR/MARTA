
import pytest
from mimesis.providers.address import Address

# Fixture to provide an instance of the Address provider
@pytest.fixture(scope="module")
def address_provider():
    return Address()

# Test for valid continent input
def test_valid_continent_input(address_provider):
    continent = address_provider.continent(code=False)
    assert isinstance(continent, str), "Expected a string representation of the continent"

# Test for invalid continent input to ensure it raises TypeError