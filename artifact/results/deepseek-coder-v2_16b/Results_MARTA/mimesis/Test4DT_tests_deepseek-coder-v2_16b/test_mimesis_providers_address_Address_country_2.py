
import pytest
from mimesis.providers.address import Address
from mimesis.exceptions import UnsupportedLocale

# Test initialization with specified locale and seed

# Test initialization with unsupported locale
def test_invalid_locale():
    with pytest.raises(UnsupportedLocale):
        Address(locale='unsupported-locale')

# Test getting the country of the current locale (default behavior)

# Test getting a random country name