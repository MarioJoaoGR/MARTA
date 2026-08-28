
import pytest
from mimesis.providers.address import Address

# Test fixture to create an instance of the Address class with a default locale
@pytest.fixture
def address_default_locale():
    return Address()

# Test fixture to create an instance of the Address class with a specific locale
@pytest.fixture
def address_specific_locale():
    return Address(locale='es_ES')

# Test case for generating a random street suffix with default locale
def test_street_suffix_default_locale(address_default_locale):
    suffix = address_default_locale.street_suffix()
    assert isinstance(suffix, str), "The result should be a string."