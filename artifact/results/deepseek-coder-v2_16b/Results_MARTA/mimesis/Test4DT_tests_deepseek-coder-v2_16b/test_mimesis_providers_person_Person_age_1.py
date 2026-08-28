
import pytest
from mimesis.providers.person import Person
from mimesis.exceptions import UnsupportedLocale

# Test initialization with specified locale and seed

# Test initialization with unsupported locale
def test_unsupported_locale():
    with pytest.raises(UnsupportedLocale):
        Person(locale='en_us')

# Test edge case where no locale is provided