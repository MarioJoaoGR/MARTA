
import pytest
from mimesis.providers.person import Person as MimesisPerson
from mimesis.exceptions import UnsupportedLocale

# Test for valid inputs
def test_valid_inputs():
    with pytest.raises(UnsupportedLocale):
        person = MimesisPerson(locale='en_US', seed=42)

# Test for edge cases
def test_edge_cases():
    with pytest.raises(UnsupportedLocale):
        person = MimesisPerson(locale='zh_CN', seed=42)

# Test for invalid inputs
def test_invalid_inputs():
    with pytest.raises(UnsupportedLocale):
        person = MimesisPerson(locale='unsupported_locale', seed=42)
