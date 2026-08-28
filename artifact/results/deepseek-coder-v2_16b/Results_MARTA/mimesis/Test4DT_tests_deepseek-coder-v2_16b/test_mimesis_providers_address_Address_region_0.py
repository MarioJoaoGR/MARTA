
import pytest
from mimesis.providers.address import Address
from mimesis.exceptions import UnsupportedLocale


def test_invalid_locale_initialization():
    with pytest.raises(UnsupportedLocale):
        Address(locale='unsupported-locale')