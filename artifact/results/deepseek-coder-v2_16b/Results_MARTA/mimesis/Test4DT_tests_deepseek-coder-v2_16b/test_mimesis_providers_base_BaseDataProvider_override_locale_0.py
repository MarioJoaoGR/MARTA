
import pytest
from mimesis.providers.base import BaseDataProvider, locales
from mimesis.exceptions import UnsupportedLocale

def test_unsupported_locale():
    with pytest.raises(UnsupportedLocale):
        BaseDataProvider(locale="es_ES")
