
import pytest
from mimesis.providers.person import Person as MimesisPerson
from mimesis.exceptions import UnsupportedLocale

def test_valid_input_default():
    with pytest.raises(UnsupportedLocale):
        person = MimesisPerson(locale='en_us')

def test_valid_input_with_seed():
    with pytest.raises(UnsupportedLocale):
        person = MimesisPerson(locale='en_us', seed=42)
