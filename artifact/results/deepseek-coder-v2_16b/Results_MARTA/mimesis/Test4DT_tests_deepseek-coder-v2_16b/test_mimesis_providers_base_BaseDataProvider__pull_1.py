
import pytest
from mimesis.providers.base import BaseDataProvider, locales
from mimesis.exceptions import UnsupportedLocale

def test_specified_locale_and_seed():
    with pytest.raises(UnsupportedLocale):
        base_data_provider = BaseDataProvider(locale="en_US", seed=42)

def test_specified_locale_only():
    with pytest.raises(UnsupportedLocale):
        base_data_provider = BaseDataProvider(locale="fr_FR")

def test_pull_default():
    base_data_provider = BaseDataProvider()
    with pytest.raises(IsADirectoryError):
        base_data_provider._pull()

def test_pull_specified():
    with pytest.raises(UnsupportedLocale):
        base_data_provider = BaseDataProvider(locale="en_US", seed=42)
        base_data_provider._pull()

def test_pull_specified_locale():
    with pytest.raises(UnsupportedLocale):
        base_data_provider = BaseDataProvider(locale="fr_FR")
        base_data_provider._pull()

def test_pull_specified_seed():
    with pytest.raises(IsADirectoryError):
        base_data_provider = BaseDataProvider(seed=12345)
        base_data_provider._pull()
