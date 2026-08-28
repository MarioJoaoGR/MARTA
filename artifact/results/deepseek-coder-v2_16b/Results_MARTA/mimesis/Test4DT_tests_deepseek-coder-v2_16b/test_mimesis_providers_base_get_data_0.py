
import pytest
from mimesis.providers.base import BaseDataProvider, locales
from mimesis.exceptions import UnsupportedLocale
from pathlib import Path
import json

# Test initialization with specified locale and seed

# Test initialization with specified locale only

# Test initialization with specified seed only
def test_specified_seed_only():
    provider = BaseDataProvider(seed=67890)
    assert hasattr(provider, 'seed'), "Expected the provider to have an attribute '_seed'"

# Test get_data function with a valid locale

# Test get_data function with an unsupported locale
def test_get_data_unsupported_locale():
    provider = BaseDataProvider()
    with pytest.raises(AttributeError):
        provider.get_data("de_DE")

# Test get_data function with a valid locale and path construction