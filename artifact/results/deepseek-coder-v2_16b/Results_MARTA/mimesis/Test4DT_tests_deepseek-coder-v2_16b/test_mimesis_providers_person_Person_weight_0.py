
import pytest
from mimesis.providers.person import Person
from mimesis.exceptions import UnsupportedLocale

# Test initialization with specified locale and seed

# Test initialization with specified locale only
def test_invalid_locale():
    with pytest.raises(UnsupportedLocale):
        Person(locale='en_us')

# Test initialization with unsupported locale
def test_unsupported_locale():
    with pytest.raises(UnsupportedLocale):
        Person(locale='unsupported_locale')

# Test edge case for weight generation with minimum and maximum values at the boundaries