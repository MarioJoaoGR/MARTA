
import pytest
from mimesis.providers.address import Address
from mimesis.exceptions import UnsupportedLocale

# Test for valid country with locale

# Test for unsupported locale
def test_unsupported_locale():
    with pytest.raises(UnsupportedLocale):
        Address(locale='unsupported-locale')

# Test for random country generation