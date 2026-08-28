
import pytest
from unittest.mock import patch
from mimesis.providers.person import Person
from mimesis.exceptions import UnsupportedLocale




def test_edge_case_no_locale():
    with patch('mimesis.Person._pull') as mock_pull:
        person = Person()
        with pytest.raises(KeyError):
            gender = person.gender(iso5218=False, symbol=False)

def test_edge_case_empty_locale():
    with patch('mimesis.Person._pull') as mock_pull:
        person = Person(locale='')
        with pytest.raises(KeyError):
            gender = person.gender(iso5218=False, symbol=False)

def test_error_handling_invalid_seed():
    with patch('mimesis.Person._pull') as mock_pull:
        with pytest.raises(UnsupportedLocale):
            person = Person(locale='en_US', seed=None)