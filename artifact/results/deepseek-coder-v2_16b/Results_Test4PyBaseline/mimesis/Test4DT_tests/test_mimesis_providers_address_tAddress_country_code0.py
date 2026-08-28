
import pytest
from mimesis.providers.address import Address
from mimesis.enums import CountryCode

# Assuming COUNTRY_CODES is a predefined dictionary in the module
# This test assumes that COUNTRY_CODES is correctly populated with country codes data

@pytest.fixture
def address():
    return Address()

def test_country_code_default_format(address):
    """Test default format of country code."""
    country_code = address.country_code()
    assert isinstance(country_code, str), "Expected a string representation of the country code."