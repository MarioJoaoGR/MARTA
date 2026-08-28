
import pytest
from unittest.mock import patch
from mimesis.providers.person import Person
from mimesis.exceptions import UnsupportedLocale



def test_unsupported_locale():
    with pytest.raises(UnsupportedLocale):
        with patch('mimesis.providers.person.Person._pull', return_value=None):
            person = Person(locale='xx_YY')