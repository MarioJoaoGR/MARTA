
import pytest
from unittest.mock import patch
from mimesis.providers.person import Person
from mimesis.exceptions import UnsupportedLocale



def test_invalid_inputs_gender():
    with patch('mimesis.providers.base.locales.SUPPORTED_LOCALES', {'en_US'}):
        with pytest.raises(UnsupportedLocale):
            person = Person(locale='unsupported_locale')