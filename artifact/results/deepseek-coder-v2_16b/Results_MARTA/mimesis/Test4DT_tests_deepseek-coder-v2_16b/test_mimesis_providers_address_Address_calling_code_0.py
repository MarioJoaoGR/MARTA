
import pytest
from mimesis.providers.address import Address
from mimesis import locales
from mimesis.exceptions import UnsupportedLocale



def test_invalid_input():
    with pytest.raises(UnsupportedLocale):
        address_instance = Address(locale='unsupported-locale')