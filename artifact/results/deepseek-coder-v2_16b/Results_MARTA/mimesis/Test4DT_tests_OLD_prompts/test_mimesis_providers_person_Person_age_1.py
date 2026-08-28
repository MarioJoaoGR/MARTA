
import pytest
from mimesis.providers.person import Person
from mimesis.exceptions import UnsupportedLocale

# Test for valid inputs
def test_valid_inputs():
    with pytest.raises(UnsupportedLocale):
        person = Person(locale='en_US', seed=42)
        assert person is not None

# Test for edge cases
def test_edge_cases():
    with pytest.raises(UnsupportedLocale):
        person = Person(locale='unsupported_locale', seed=42)
        assert person is not None

# Test for invalid inputs
def test_invalid_inputs():
    with pytest.raises(UnsupportedLocale):
        person = Person(locale='unsupported_locale', seed=42)
        assert person is not None
