
import pytest
from unittest.mock import patch
from mimesis.providers.address import Address, CONTINENT_CODES

@pytest.fixture(scope="function")
def address_provider():
    return Address()

# Test 1: Basic instantiation of the Address class
def test_basic_instantiation():
    provider = Address()
    assert isinstance(provider, Address)

# Test 2: Instantiating with a specific locale

# Test 3: Generating random city name
def test_generate_random_city_name(address_provider):
    city = address_provider.city()
    assert isinstance(city, str)

# Test 4: Generating random street name
def test_generate_random_street_name(address_provider):
    street = address_provider.street_name()
    assert isinstance(street, str)

# Test 5: Generating random postal code
def test_generate_random_postal_code(address_provider):
    postal_code = address_provider.postal_code()
    assert isinstance(postal_code, str)

# Test 6: Generating random country name
def test_generate_random_country_name(address_provider):
    country = address_provider.country()
    assert isinstance(country, str)

# Test 7: Getting random continent name or code (default is False for name)

# Test 8: Getting random continent code (True for code)
def test_get_random_continent_code(address_provider):
    with patch('mimesis.providers.address.CONTINENT_CODES', new=dict(enumerate(CONTINENT_CODES))):
        continent_code = address_provider.continent(code=True)
        assert isinstance(continent_code, str)