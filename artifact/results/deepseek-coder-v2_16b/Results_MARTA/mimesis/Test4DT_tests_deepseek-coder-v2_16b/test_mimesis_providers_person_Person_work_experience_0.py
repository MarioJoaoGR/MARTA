
import pytest
from mimesis.providers.person import Person as MimesisPerson
from mimesis.exceptions import UnsupportedLocale


def test_invalid_locale():
    with pytest.raises(UnsupportedLocale):
        person = MimesisPerson(locale='unsupported_locale', seed=42)


def test_valid_inputs_with_default_locale():
    person = MimesisPerson(seed=42)
    assert isinstance(person, MimesisPerson), "Expected a valid instance of MimesisPerson"