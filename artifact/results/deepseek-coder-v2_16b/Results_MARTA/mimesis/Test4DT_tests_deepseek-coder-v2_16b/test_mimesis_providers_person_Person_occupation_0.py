
import pytest
from mimesis.providers.person import Person as MimesisPerson
from mimesis.exceptions import UnsupportedLocale



def test_invalid_locale():
    with pytest.raises(UnsupportedLocale):
        person = MimesisPerson(locale='unsupported_locale')