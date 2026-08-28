
import pytest
from mimesis.providers.person import Person
from mimesis.exceptions import UnsupportedLocale


def test_invalid_locale():
    with pytest.raises(UnsupportedLocale):
        person_invalid_locale = Person(locale='unsupported_locale')