
import pytest
from mimesis.providers.text import Text
from mimesis import locales
from mimesis.exceptions import UnsupportedLocale

def test_valid_input_default_quantity():
    with pytest.raises(UnsupportedLocale):
        text_data = Text(locale='en-us')


def test_invalid_input_negative_quantity():
    with pytest.raises(TypeError):
        text_data = Text(locale='en-US', quantity=-1)