
import pytest
from mimesis.providers.structure import Structure
from mimesis.exceptions import UnsupportedLocale

# Test initialization with valid locale and seed

# Test initialization with unsupported locale
def test_unsupported_locale():
    with pytest.raises(UnsupportedLocale):
        Structure(locale='unsupported-locale')

# Test method generation of HTML tag with text inside and some attributes set