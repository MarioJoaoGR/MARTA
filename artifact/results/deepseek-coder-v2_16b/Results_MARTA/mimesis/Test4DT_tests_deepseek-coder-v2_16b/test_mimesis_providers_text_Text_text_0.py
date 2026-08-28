
import pytest
from mimesis.providers.text import Text
from mimesis.exceptions import UnsupportedLocale

# Test initialization with specified locale and default seed

# Test initialization with unspecified locale and default seed
def test_valid_input_default_locale():
    text_data = Text()
    assert isinstance(text_data, Text)

# Test initialization with specified locale and invalid case
def test_invalid_input_case_insensitive_locale():
    with pytest.raises(UnsupportedLocale):
        Text(locale='en-us')

# Test initialization with unspecified locale and seed
def test_valid_input_default_seed():
    text_data = Text()
    assert isinstance(text_data, Text)

# Test initialization with specified locale and specified seed

# Test initialization with unsupported locale
def test_invalid_input_unsupported_locale():
    with pytest.raises(UnsupportedLocale):
        Text(locale='unsupported-locale')