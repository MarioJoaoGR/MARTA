
import pytest
from mimesis.providers.address import Address
from mimesis.exceptions import UnsupportedLocale


def test_invalid_province_error_handling():
    with pytest.raises(UnsupportedLocale):
        address_instance = Address(locale='unsupported-locale')