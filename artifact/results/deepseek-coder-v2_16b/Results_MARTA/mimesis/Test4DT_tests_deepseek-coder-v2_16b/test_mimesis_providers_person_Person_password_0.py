
import pytest
from mimesis.providers.person import Person as MPerson
from mimesis.exceptions import UnsupportedLocale



def test_invalid_locale():
    with pytest.raises(UnsupportedLocale):
        MPerson(locale='unsupported_locale', seed=42)