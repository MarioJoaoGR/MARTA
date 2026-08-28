
import pytest
from unittest.mock import patch
from mimesis.schema import AbstractField
from mimesis.exceptions import UnsupportedLocale
from mimesis.providers import Generic

# Test 1: test_valid_locale_and_seed
def test_valid_locale_and_seed():
    with patch('mimesis.providers.Generic.__init__', return_value=None):
        field = AbstractField(locale='es', seed=12345)
        assert field.locale == 'es'
        assert field.seed == 12345
        assert isinstance(field._gen, Generic)

# Test 2: test_none_providers
def test_none_providers():
    with patch('mimesis.providers.Generic.__init__', return_value=None):
        field = AbstractField(locale='en')
        assert field.locale == 'en'
        assert field.seed is None
        assert isinstance(field._gen, Generic)

# Test 3: test_invalid_locale
def test_invalid_locale():
    with pytest.raises(UnsupportedLocale):
        raise UnsupportedLocale("fr_FR")
