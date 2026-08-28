
import pytest
from mimesis.providers.person import Person as MimesisPerson
from mimesis.exceptions import UnsupportedLocale

# Test initialization with specified locale and seed

# Test initialization with specified locale only
def test_specified_locale():
    with pytest.raises(UnsupportedLocale):
        person = MimesisPerson(locale='es_ES')