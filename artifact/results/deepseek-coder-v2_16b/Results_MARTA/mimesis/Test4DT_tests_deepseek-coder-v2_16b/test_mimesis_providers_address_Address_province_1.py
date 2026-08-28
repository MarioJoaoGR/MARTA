
import pytest
from mimesis.providers.address import Address
from mimesis.exceptions import UnsupportedLocale

# Test initialization with a specific locale ('en-US')

# Test initialization with an unsupported locale
def test_invalid_province_unsupported_locale():
    with pytest.raises(UnsupportedLocale):
        Address(locale='es-ES')