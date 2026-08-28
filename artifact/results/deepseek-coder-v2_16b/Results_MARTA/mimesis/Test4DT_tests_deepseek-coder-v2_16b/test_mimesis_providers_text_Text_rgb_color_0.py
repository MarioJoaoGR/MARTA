
import pytest
from mimesis.providers.text import Text
from mimesis.exceptions import UnsupportedLocale



def test_invalid_rgb_color():
    with pytest.raises(UnsupportedLocale):
        Text(locale='unsupported-locale')