
import pytest
from mimesis.providers.text import Text
from mimesis.exceptions import UnsupportedLocale

# Test initialization with specified locale and seed

# Test initialization with unsupported locale
def test_invalid_locale():
    with pytest.raises(UnsupportedLocale):
        Text(locale='unsupported-locale')

# Test default initialization
def test_default_initialization():
    text_data = Text()
    assert isinstance(text_data, Text)

# Test initialization with specified locale only

# Test initialization with specified seed only
def test_specified_seed():
    text_data = Text(seed=12345)
    assert isinstance(text_data, Text)