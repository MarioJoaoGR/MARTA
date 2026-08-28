
import pytest
from mimesis.providers.base import BaseDataProvider, locales
from mimesis.exceptions import UnsupportedLocale

# Test default initialization

# Test initialization with specified locale and seed
def test_initialization_with_locale_and_seed():
    base_data_provider = BaseDataProvider(locale="fr", seed=12345)
    assert hasattr(base_data_provider, 'locale') is True
    assert base_data_provider.locale == "fr"
    assert hasattr(base_data_provider, 'seed') is True
    assert base_data_provider.seed == 12345

# Test initialization with specified locale only

# Test initialization with specified seed only

# Test initialization with unsupported locale
def test_unsupported_locale():
    with pytest.raises(UnsupportedLocale):
        BaseDataProvider(locale="es_ES")