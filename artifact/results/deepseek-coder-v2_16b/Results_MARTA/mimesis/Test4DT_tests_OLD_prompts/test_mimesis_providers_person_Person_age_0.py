
import pytest
from mimesis.providers.person import Person
from mimesis.exceptions import UnsupportedLocale

# Test valid inputs
def test_valid_inputs():
    with pytest.raises(UnsupportedLocale):
        person = Person(locale='en_us', seed=42)
