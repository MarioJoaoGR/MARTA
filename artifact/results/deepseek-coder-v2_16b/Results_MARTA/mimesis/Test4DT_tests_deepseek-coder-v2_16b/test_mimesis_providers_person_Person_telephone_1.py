
import pytest
from mimesis.providers.person import Person
from mimesis.exceptions import UnsupportedLocale

# Test initialization with unsupported locale
def test_unsupported_locale():
    with pytest.raises(UnsupportedLocale):
        person = Person(locale="es_ES")
