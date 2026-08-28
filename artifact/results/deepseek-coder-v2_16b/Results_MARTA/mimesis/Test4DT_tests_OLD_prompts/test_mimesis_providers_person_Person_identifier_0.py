
import pytest
from mimesis.providers.person import Person as MimesisPerson
from mimesis.exceptions import UnsupportedLocale

def test_valid_identifier_generation():
    with pytest.raises(UnsupportedLocale):
        person = MimesisPerson(locale='en_US', seed=42)

def test_missing_lines():
    with pytest.raises(UnsupportedLocale):
        person = MimesisPerson(locale='en_US', seed=42)
