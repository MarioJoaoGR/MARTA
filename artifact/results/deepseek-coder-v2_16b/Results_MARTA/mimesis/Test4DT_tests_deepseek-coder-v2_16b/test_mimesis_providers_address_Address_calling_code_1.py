
import pytest
from mimesis.providers.address import Address
from mimesis.exceptions import UnsupportedLocale

# Test initialization with specified locale and seed

# Test initialization with unsupported locale
def test_unsupported_locale():
    with pytest.raises(UnsupportedLocale):
        Address(locale='unsupported-locale')