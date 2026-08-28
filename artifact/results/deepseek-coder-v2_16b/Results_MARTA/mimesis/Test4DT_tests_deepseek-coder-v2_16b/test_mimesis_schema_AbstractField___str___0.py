
import pytest
from mimesis.providers.base import BaseProvider
from mimesis.schema import AbstractField, Generic
from mimesis.exceptions import UnsupportedLocale

# Test initialization without parameters
def test_abstract_field_default_initialization():
    field = AbstractField()
    assert field.locale == 'en'
    assert field._gen is not None
    assert isinstance(field._gen, Generic)
    assert field._table == {}

# Test initialization with specific locale and seed
def test_abstract_field_with_parameters():
    field = AbstractField(locale='es', seed=12345)
    assert field.locale == 'es'
    assert field.seed == 12345
    assert isinstance(field._gen, Generic)
    assert field._table == {}

# Test initialization with unsupported locale
def test_abstract_field_unsupported_locale():
    with pytest.raises(UnsupportedLocale):
        AbstractField(locale='fr_FR')

# Test adding custom providers
class MyCustomProvider(BaseProvider):
    def my_custom_method(self):
        return "Hello, World!"


# Test string representation of the class
def test_abstract_field_str():
    field = AbstractField(locale='es', seed=12345)
    expected_str = 'AbstractField <es>'
    assert str(field) == expected_str