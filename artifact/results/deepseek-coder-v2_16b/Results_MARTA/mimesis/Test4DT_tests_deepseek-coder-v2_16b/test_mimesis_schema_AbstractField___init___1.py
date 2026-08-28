
import pytest
from mimesis.schema import AbstractField
from mimesis.providers import Generic

# Test Scenario 1: Test standard input with default locale and no seed
def test_valid_case_default_locale():
    field = AbstractField()
    assert isinstance(field._gen, Generic)
    assert field._gen.locale == 'en'
    assert field._gen.seed is None

# Test Scenario 2: Test standard input with specific locale but no seed
def test_valid_case_specific_locale():
    field = AbstractField(locale='es')
    assert isinstance(field._gen, Generic)
    assert field._gen.locale == 'es'
    assert field._gen.seed is None

# Test Scenario 3: Test raising TypeError when providing invalid providers
def test_error_case_invalid_providers():
    with pytest.raises(TypeError):
        AbstractField(providers=123)
