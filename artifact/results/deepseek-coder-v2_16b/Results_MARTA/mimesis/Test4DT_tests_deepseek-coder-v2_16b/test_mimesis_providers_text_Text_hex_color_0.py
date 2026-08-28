
import pytest
from mimesis.providers.text import Text
from mimesis.exceptions import UnsupportedLocale

# Test initialization with specified locale and seed

# Test initialization with specified locale only

# Test initialization with unsupported locale
def test_invalid_locale():
    with pytest.raises(UnsupportedLocale):
        Text(locale='en-us')