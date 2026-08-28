
import pytest
from mimesis.providers.person import Person as MimesisPerson
from mimesis.exceptions import UnsupportedLocale

# Test initialization with specified locale and seed

# Test initialization with unsupported locale
def test_unsupported_locale():
    with pytest.raises(UnsupportedLocale):
        person = MimesisPerson(locale='en_us')

# Test edge cases where inputs are None or empty