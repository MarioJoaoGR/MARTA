
import pytest
from mimesis.providers.address import Address
from mimesis.exceptions import UnsupportedLocale

# Test for default locale initialization
@pytest.fixture(scope="module")
def address_instance():
    return Address(locale='en-US')


# Test for retrieving prefecture with abbreviation
@pytest.fixture(scope="module")
def address_instance_abbr():
    return Address(locale='en-US')


# Additional test for unsupported locale
def test_unsupported_locale():
    with pytest.raises(UnsupportedLocale):
        Address(locale='unsupported-locale')