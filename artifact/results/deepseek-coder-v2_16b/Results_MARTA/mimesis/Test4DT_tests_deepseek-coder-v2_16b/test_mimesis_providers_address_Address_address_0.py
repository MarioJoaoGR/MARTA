
import pytest
from mimesis.providers.address import Address

# Test for generating a random full address in the default locale (en_US)
def test_valid_address_default_locale():
    address = Address()
    assert isinstance(address.address(), str), "Expected a string representation of an address"

# Test for generating a random full address in a specific locale (ja)
def test_valid_address_specific_locale():
    address_jp = Address(locale='ja')
    assert isinstance(address_jp.address(), str), "Expected a string representation of a Japanese address"
    # Additional assertion to check if the city is included in the address for ja locale
    assert len(address_jp._data['city']) > 0, "Expected at least one city in the Japanese address"

# Test handling of an invalid or unsupported locale (ZZ)
def test_invalid_locale():
    with pytest.raises(KeyError):
        Address(locale='ZZ')
