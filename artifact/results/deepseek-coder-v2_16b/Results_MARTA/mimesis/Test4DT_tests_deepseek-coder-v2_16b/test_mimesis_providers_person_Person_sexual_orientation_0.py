
import pytest
from mimesis.providers.person import Person as MPerson
from mimesis import locales
from mimesis.exceptions import UnsupportedLocale

def test_valid_input_default_symbol():
    with pytest.raises(UnsupportedLocale):
        person = MPerson(locale='en_US', seed=42)

def test_valid_input_with_symbol():
    with pytest.raises(UnsupportedLocale):
        person = MPerson(locale='en_US', seed=42)
