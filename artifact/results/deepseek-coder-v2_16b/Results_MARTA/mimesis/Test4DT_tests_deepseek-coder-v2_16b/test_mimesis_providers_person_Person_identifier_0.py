
import pytest
from mimesis.providers.person import Person as MPerson
from mimesis.exceptions import UnsupportedLocale

# Test initialization with specified locale and seed

# Test initialization with specified locale only

# Test initialization with unsupported locale
def test_invalid_input_with_unsupported_locale():
    with pytest.raises(UnsupportedLocale):
        MPerson(locale='xx_XX')