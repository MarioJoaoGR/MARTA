
import pytest
from mimesis.providers.person import Person as MimesisPerson
from mimesis.exceptions import UnsupportedLocale

# Test initialization with a valid locale

# Test initialization with unsupported locale
def test_unsupported_locale():
    with pytest.raises(UnsupportedLocale):
        person = MimesisPerson(locale='unsupported_locale', seed=42)