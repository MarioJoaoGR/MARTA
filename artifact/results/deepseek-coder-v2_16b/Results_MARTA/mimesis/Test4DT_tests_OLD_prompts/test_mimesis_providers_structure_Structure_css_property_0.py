
import pytest
from unittest.mock import patch
from mimesis.providers.structure import Structure, CSS_PROPERTIES
from mimesis.providers.text import Text
from mimesis.exceptions import UnsupportedLocale


def test_invalid_locale():
    with pytest.raises(UnsupportedLocale):
        Structure(locale='unsupported-locale', seed=42)

