
import pytest
from mimesis.providers.text import Text
from mimesis.exceptions import UnsupportedLocale

# Test initialization with a valid locale and seed

# Test initialization with a valid locale without providing a seed

# Test initialization with an unsupported locale
def test_unsupported_locale():
    with pytest.raises(UnsupportedLocale):
        Text(locale='zz-ZZ')