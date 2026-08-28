
import pytest
from mimesis.providers import Address
from mimesis.exceptions import UnsupportedLocale

# Test initialization with unsupported locale
def test_unsupported_locale():
    with pytest.raises(UnsupportedLocale):
        address = Address(locale='es-ES')
