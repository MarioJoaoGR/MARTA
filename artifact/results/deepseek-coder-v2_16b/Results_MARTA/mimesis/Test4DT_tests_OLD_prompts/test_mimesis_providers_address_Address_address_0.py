
import pytest
from mimesis.providers.address import Address
from mimesis.exceptions import UnsupportedLocale

def test_invalid_locale_input():
    with pytest.raises(UnsupportedLocale):
        address_invalid = Address(locale='ZZ')
