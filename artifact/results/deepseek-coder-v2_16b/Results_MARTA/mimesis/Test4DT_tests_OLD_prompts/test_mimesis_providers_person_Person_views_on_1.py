
import pytest
from unittest.mock import patch
from mimesis.providers.person import Person
from mimesis.exceptions import UnsupportedLocale

class MockPerson(Person):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._datafile = 'person.json'

def test_valid_locale_input():
    with patch('mimesis.providers.person.Person.__init__', return_value=None):
        person = MockPerson(locale='en_US')
        assert person._datafile == 'person.json'

def test_valid_locale_and_seed_input():
    with patch('mimesis.providers.person.Person.__init__', return_value=None):
        person = MockPerson(locale='fr_FR', seed=12345)
        assert person._datafile == 'person.json'

def test_invalid_locale_input():
    with pytest.raises(UnsupportedLocale):
        Person(locale='unsupported_locale')
