
import pytest
from mimesis.providers.address import Address
from mimesis.exceptions import UnsupportedLocale

# Test initialization with a valid locale

# Test initialization with an unsupported locale
def test_invalid_prefecture():
    with pytest.raises(UnsupportedLocale):
        Address(locale='ZZ')

# Test initialization with a valid locale and requesting the abbreviation