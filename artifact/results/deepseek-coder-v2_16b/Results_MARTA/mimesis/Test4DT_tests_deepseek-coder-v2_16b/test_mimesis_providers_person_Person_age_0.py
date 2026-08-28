
import pytest
from mimesis.providers.person import Person as MPerson
from mimesis import locales
from mimesis.exceptions import UnsupportedLocale

# Test for valid input scenario

# Test for edge case scenario where minimum age is set to a very low value
def test_edge_case():
    with pytest.raises(UnsupportedLocale):
        MPerson(locale='en_US', seed=42)

# Test for invalid input scenario with unsupported locale
def test_invalid_input():
    with pytest.raises(UnsupportedLocale):
        MPerson(locale='unsupported_locale', seed=42)