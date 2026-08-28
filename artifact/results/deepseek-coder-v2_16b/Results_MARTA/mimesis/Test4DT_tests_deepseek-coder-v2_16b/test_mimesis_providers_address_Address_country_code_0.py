
import pytest
from mimesis.providers.address import Address
from mimesis.exceptions import UnsupportedLocale
from mimesis.enums import CountryCode

def test_unsupported_locale():
    with pytest.raises(UnsupportedLocale):
        address = Address(locale="zz")
