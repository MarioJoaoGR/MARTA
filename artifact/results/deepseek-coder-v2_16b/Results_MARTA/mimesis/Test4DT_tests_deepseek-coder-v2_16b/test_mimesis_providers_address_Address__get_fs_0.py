
import pytest
from mimesis.providers.address import Address
from mimesis.exceptions import UnsupportedLocale

def test_initialization_with_locale():
    with pytest.raises(UnsupportedLocale):
        address = Address(locale='en-US')



