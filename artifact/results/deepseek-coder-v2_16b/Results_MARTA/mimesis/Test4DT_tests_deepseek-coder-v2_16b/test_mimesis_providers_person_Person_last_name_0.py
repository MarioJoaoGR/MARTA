
import pytest
from mimesis.providers.person import Person
from mimesis import locales
from mimesis.exceptions import UnsupportedLocale


def test_invalid_locale_raises_exception():
    with pytest.raises(UnsupportedLocale):
        person = Person(locale='unsupported_locale')