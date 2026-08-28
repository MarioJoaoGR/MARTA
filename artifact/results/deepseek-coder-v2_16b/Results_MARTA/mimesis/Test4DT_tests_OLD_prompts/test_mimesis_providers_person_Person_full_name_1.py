
import pytest
from unittest.mock import patch
from mimesis.providers.person import Person
from mimesis.enums import Gender
from mimesis.exceptions import UnsupportedLocale, NonEnumerableError

@pytest.fixture(scope="module")
def person():
    with patch('mimesis.Person._pull', return_value={'names': {'male': ['John'], 'female': ['Jane']}, 'surnames': {'male': ['Doe'], 'female': ['Smith']}}):
        yield Person(locale='en_US')


def test_invalid_locale(monkeypatch):
    with patch('mimesis.Person._pull', return_value={'names': {'male': ['John'], 'female': ['Jane']}, 'surnames': {'male': ['Doe'], 'female': ['Smith']}}):
        with pytest.raises(UnsupportedLocale):
            person = Person(locale='unsupported_locale')
