
import pytest
from unittest.mock import patch
from mimesis.providers.person import Person

def test_instantiate_person_with_locale():
    with pytest.raises(Exception):
        person = Person(locale='en_us')

def test_instantiate_person_with_locale_and_seed():
    with pytest.raises(Exception):
        person = Person(locale='en_us', seed=42)

