
import pytest
from mimesis.providers import Address
from mimesis.exceptions import UnsupportedLocale


def test_invalid_locale_raises_exception():
    with pytest.raises(UnsupportedLocale):
        address = Address(locale='unsupported-locale')