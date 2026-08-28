
import pytest
from mimesis.providers.structure import Structure
from mimesis.exceptions import UnsupportedLocale

# Test initialization with valid locale and seed

# Test initialization with unsupported locale
def test_unsupported_locale():
    with pytest.raises(UnsupportedLocale):
        structure_instance = Structure(locale='invalid-locale', seed=42)

# Test initialization with no locale provided