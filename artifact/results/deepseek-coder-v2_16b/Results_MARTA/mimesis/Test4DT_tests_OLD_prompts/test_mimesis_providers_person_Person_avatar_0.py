
import pytest
from mimesis import Person
from mimesis.exceptions import UnsupportedLocale
from unittest.mock import patch

def test_invalid_locale_error():
    with pytest.raises(UnsupportedLocale):
        person = Person(locale='unsupported_locale')
