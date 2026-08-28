
import pytest
from mimesis.providers.person import Person
from mimesis.enums import Gender

# Test initialization with specified locale and seed

# Test initialization with specified locale only

# Test initialization with unsupported locale
def test_invalid_locale():
    with pytest.raises(Exception):
        Person(locale='unsupported_locale', seed=42)