
import pytest
from mimesis.providers.address import Address
from mimesis.exceptions import UnsupportedLocale

# Test initialization with a valid locale

# Test initialization with an unsupported locale
def test_unsupported_locale():
    with pytest.raises(UnsupportedLocale):
        Address(locale='es_ES')