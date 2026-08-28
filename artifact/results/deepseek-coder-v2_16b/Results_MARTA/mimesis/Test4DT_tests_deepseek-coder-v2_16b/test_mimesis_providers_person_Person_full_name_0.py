
import pytest
from mimesis.providers.person import Person
from mimesis.enums import Gender
from mimesis.exceptions import UnsupportedLocale, NonEnumerableError

def test_valid_input_specific_locale():
    with pytest.raises(UnsupportedLocale):
        person = Person(locale='en_US')

def test_valid_input_specific_gender():
    with pytest.raises(TypeError):
        person = Person(locale='en_US', gender=Gender.MALE)

def test_valid_input_reverse_order():
    with pytest.raises(UnsupportedLocale):
        person = Person(locale='en_US')

def test_edge_case_none_gender():
    with pytest.raises(TypeError):
        person = Person(locale='en_US', gender=None)
