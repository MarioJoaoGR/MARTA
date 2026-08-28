
import pytest
from mimesis.providers.base import BaseDataProvider, locales
from mimesis.exceptions import UnsupportedLocale


def test_invalid_locale():
    with pytest.raises(UnsupportedLocale):
        BaseDataProvider(locale='unsupported_locale')

def test_no_locale_and_seed():
    base_data_provider = BaseDataProvider()
    assert base_data_provider is not None
    assert base_data_provider.locale == locales.DEFAULT_LOCALE
    assert base_data_provider._datafile == ''
    assert base_data_provider._data_dir.name == 'data'