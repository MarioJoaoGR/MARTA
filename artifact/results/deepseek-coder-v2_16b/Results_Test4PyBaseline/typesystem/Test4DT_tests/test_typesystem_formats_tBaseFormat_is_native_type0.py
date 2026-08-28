
# Module: typesystem.formats
import pytest
from typesystem.formats import BaseFormat

# Test instantiating the base format class
def test_instantiate_base_format():
    base_format = BaseFormat()
    assert isinstance(base_format, BaseFormat)

# Test is_native_type method with native Python types
@pytest.mark.parametrize("value", [
    123,
    "string",
    123.45,
    [1, 2, 3],
    {"key": "value"},
    None
])
def test_is_native_type(value):
    base_format = BaseFormat()