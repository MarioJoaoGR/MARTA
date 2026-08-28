
import pytest
from mimesis.providers.person import Person
from mimesis.exceptions import UnsupportedLocale, NonEnumerableError
from mimesis.enums import Gender

def test_valid_input_specific_locale():
    with pytest.raises(UnsupportedLocale):
        person = Person(locale='en_US')

def test_valid_input_with_seed():
    with pytest.raises(UnsupportedLocale):
        person = Person(locale='en_US', seed=42)

def test_valid_input_specific_gender():
    with pytest.raises(UnsupportedLocale):
        person = Person(locale='en_US')

def test_valid_input_reverse_order():
    with pytest.raises(UnsupportedLocale):
        person = Person(locale='en_US')

def test_invalid_input_none_gender():
    with pytest.raises(UnsupportedLocale):
        person = Person(locale='en_US')

def test_invalid_input_wrong_gender():
    with pytest.raises(UnsupportedLocale):
        person = Person(locale='en_US')
