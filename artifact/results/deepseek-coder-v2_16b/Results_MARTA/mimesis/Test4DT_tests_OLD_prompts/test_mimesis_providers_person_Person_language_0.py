
import pytest
from unittest.mock import patch
from mimesis.providers.person import Person
from mimesis.exceptions import UnsupportedLocale



def test_unsupported_locale():
    with pytest.raises(UnsupportedLocale):
        Person(locale='unsupported_locale')