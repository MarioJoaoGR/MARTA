
import pytest
from mimesis import Address
from mimesis.providers import Generic

# Test initialization with default locale
def test_default_locale():
    address = Address()
    assert address.locale == 'en'
    state = address.state()