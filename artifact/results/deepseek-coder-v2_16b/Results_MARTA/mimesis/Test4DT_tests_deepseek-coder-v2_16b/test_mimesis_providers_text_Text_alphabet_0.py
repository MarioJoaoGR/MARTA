
import pytest
from mimesis.providers.text import Text
from mimesis.exceptions import UnsupportedLocale



def test_invalid_locale():
    with pytest.raises(UnsupportedLocale):
        Text(locale='unsupported-locale')