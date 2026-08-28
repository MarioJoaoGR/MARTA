
import pytest
from mimesis.providers.person import Person as MimesisPerson
from mimesis.exceptions import UnsupportedLocale

# Test initialization with specified locale and seed

# Test initialization with unsupported locale
def test_error_case():
    with pytest.raises(UnsupportedLocale):
        person = MimesisPerson(locale='unsupported_locale')