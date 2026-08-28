
import pytest
from mimesis.providers.base import BaseDataProvider, locales
from mimesis.exceptions import UnsupportedLocale


def test_invalid_locale():
    with pytest.raises(UnsupportedLocale):
        BaseDataProvider(locale='unsupported_locale')
