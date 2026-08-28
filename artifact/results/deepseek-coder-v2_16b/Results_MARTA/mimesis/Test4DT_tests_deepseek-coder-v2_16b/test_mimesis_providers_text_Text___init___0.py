
import pytest
from mimesis.providers.text import Text as MimesisText
from mimesis.exceptions import UnsupportedLocale



def test_invalid_locale():
    with pytest.raises(UnsupportedLocale):
        text = MimesisText(locale='invalid-locale')