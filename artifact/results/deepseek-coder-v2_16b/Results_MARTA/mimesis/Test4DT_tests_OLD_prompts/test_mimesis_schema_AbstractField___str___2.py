
import pytest
from unittest.mock import patch, MagicMock
from mimesis.schema import AbstractField
from mimesis.exceptions import UnsupportedLocale
from mimesis.providers import Generic

# Test for valid locale and seed
def test_valid_locale_and_seed():
    with patch('mimesis.schema.Generic', autospec=True) as mock_generic:
        field = AbstractField(locale='es', seed=12345)
        assert field.locale == 'es'
        assert field.seed == 12345
        mock_generic.assert_called_once_with('es', 12345)

# Test for None providers
def test_none_providers():
    with patch('mimesis.schema.Generic', autospec=True) as mock_generic:
        field = AbstractField(locale='en')
        assert field.locale == 'en'
        assert field.seed is None
        mock_generic.assert_called_once_with('en', None)

# Test for invalid locale raising UnsupportedLocale exception
def test_invalid_locale():
    with pytest.raises(UnsupportedLocale):
        AbstractField(locale='fr_FR')
