
import pytest
from mimesis.providers.base import BaseDataProvider, locales
from mimesis.exceptions import UnsupportedLocale


def test_specified_locale_and_seed():
    with pytest.raises(UnsupportedLocale):
        BaseDataProvider(locale="en_US")

def test_specified_locale_only():
    with pytest.raises(UnsupportedLocale):
        BaseDataProvider(locale="es_ES")
