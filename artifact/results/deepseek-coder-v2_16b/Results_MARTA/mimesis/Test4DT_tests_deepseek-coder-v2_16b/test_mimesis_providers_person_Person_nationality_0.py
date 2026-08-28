
import pytest
from mimesis.providers.person import Person
from mimesis import locales
from mimesis.exceptions import UnsupportedLocale



def test_instantiate_person_with_unsupported_locale():
    with pytest.raises(UnsupportedLocale):
        person = Person(locale='unsupported_locale')