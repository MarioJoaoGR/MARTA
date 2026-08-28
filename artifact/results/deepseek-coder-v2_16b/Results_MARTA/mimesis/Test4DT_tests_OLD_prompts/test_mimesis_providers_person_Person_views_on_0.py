
import pytest
from mimesis.providers.person import Person as MimesisPerson
from mimesis.exceptions import UnsupportedLocale

def test_valid_locale_seed():
    with pytest.raises(UnsupportedLocale):
        person = MimesisPerson(locale='en_US', seed=42)
