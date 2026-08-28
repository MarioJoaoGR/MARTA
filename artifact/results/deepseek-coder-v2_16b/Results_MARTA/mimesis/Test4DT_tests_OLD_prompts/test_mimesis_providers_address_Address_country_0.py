
import pytest
from unittest.mock import patch
from mimesis.providers.address import Address
from mimesis.exceptions import UnsupportedLocale


def test_invalid_locale():
    with pytest.raises(UnsupportedLocale):
        Address(locale='unsupported-locale')
