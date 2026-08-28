
import pytest
from mimesis.providers.person import Person as MPerson
from mimesis.exceptions import UnsupportedLocale

# Test initialization with specified locale and seed

# Test initialization with unsupported locale
def test_unsupported_locale():
    with pytest.raises(UnsupportedLocale):
        MPerson(locale='unsupported_locale')