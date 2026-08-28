
import pytest
from mimesis.providers.person import Person
from mimesis.exceptions import UnsupportedLocale

# Test initialization with specified locale and seed

# Test initialization with specified locale only

# Test initialization with specified seed only
def test_valid_input_seed_only():
    person = Person(seed=42)
    assert isinstance(person, Person), "Expected a Person object"
    assert person._datafile == 'person.json', "Expected data file to be 'person.json'"

# Test initialization with unsupported locale
def test_invalid_input_unsupported_locale():
    with pytest.raises(UnsupportedLocale):
        person = Person(locale='unsupported_locale')