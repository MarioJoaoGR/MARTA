
import pytest
from mimesis.providers.person import Person
from mimesis.exceptions import UnsupportedLocale

# Test initialization with locale and seed

# Test initialization with only locale

# Test initialization with unsupported locale
def test_init_with_unsupported_locale():
    with pytest.raises(UnsupportedLocale):
        p = Person(locale='unsupported_locale')