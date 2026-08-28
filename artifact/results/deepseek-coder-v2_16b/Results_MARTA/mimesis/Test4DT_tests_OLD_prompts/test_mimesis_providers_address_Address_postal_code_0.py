
import pytest
from mimesis.providers.address import Address
from mimesis.exceptions import UnsupportedLocale

def test_invalid_locale():
    with pytest.raises(UnsupportedLocale):
        address = Address(locale='INVALID')  # Invalid locale provided
