
import pytest
from mimesis.providers.base import BaseDataProvider, locales
from mimesis.exceptions import UnsupportedLocale
from pathlib import Path
import json

# Test default initialization

# Test initialization with specified locale and seed

# Test initialization with specified locale only

# Test initialization with specified seed only

# Test initialization with unsupported locale
def test_invalid_locale():
    with pytest.raises(UnsupportedLocale):
        BaseDataProvider(locale='unsupported_locale')