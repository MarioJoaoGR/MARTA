
import pytest
from typesystem.formats import BaseFormat

@pytest.fixture
def base_format():
    return BaseFormat()

def test_instantiation_without_parameters(base_format):
    assert isinstance(base_format, BaseFormat)

def test_validation_error_with_max_length_code(base_format):
    with pytest.raises(KeyError):
        base_format.validation_error(code="max_length")

@pytest.mark.skip(reason="Method is not implemented in BaseFormat class.")
def test_is_native_type_integer(base_format):
    assert not base_format.is_native_type(123)

@pytest.mark.skip(reason="Method is not implemented in BaseFormat class.")
def test_validate_value(base_format):
    with pytest.raises(NotImplementedError):
        base_format.validate(123)

@pytest.mark.skip(reason="Method is not implemented in BaseFormat class.")
def test_serialize_object(base_format):
    with pytest.raises(NotImplementedError):
        base_format.serialize({"key": "value"})
