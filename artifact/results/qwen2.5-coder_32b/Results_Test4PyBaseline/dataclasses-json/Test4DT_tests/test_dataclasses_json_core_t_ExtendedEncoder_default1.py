
import pytest
from datetime import datetime
from uuid import UUID
from enum import Enum
from decimal import Decimal
from collections.abc import Collection, Mapping
from dataclasses_json.core import _ExtendedEncoder

# Helper function to safely check instance types (assuming this is defined elsewhere in your codebase)
def _isinstance_safe(obj, cls):
    try:
        return isinstance(obj, cls)
    except Exception:
        return False

@pytest.fixture
def encoder():
    return _ExtendedEncoder()

# Existing test case for reference
def test_default_with_dict(encoder):
    data = {'key': 'value', 'numbers': [1, 2, 3], 'date': datetime(2023, 1, 1), 'uuid': UUID('12345678-1234-5678-1234-567812345678')}
    result = encoder.default(data)
    assert isinstance(result, dict)
    assert result['key'] == 'value'
    assert result['numbers'] == [1, 2, 3]

# Additional test cases to cover uncovered lines

def test_default_with_list(encoder):
    data = [1, 2, 3]
    result = encoder.default(data)
    assert isinstance(result, list)
    assert result == [1, 2, 3]

def test_default_with_datetime(encoder):
    data = datetime(2023, 1, 1)
    result = encoder.default(data)
    assert isinstance(result, float)
    assert result == data.timestamp()

def test_default_with_uuid(encoder):
    data = UUID('12345678-1234-5678-1234-567812345678')
    result = encoder.default(data)
    assert isinstance(result, str)
    assert result == '12345678-1234-5678-1234-567812345678'

def test_default_with_enum(encoder):
    class TestEnum(Enum):
        VALUE = 1

    data = TestEnum.VALUE
    result = encoder.default(data)
    assert isinstance(result, int)
    assert result == 1

def test_default_with_decimal(encoder):
    data = Decimal('123.45')
    result = encoder.default(data)
    assert isinstance(result, str)
    assert result == '123.45'

def test_default_with_unhandled_type(encoder):
    class CustomType:
        pass

    data = CustomType()
    with pytest.raises(TypeError):  # Assuming default raises TypeError for unhandled types
        encoder.default(data)

# Edge case tests to ensure robustness

def test_default_with_empty_dict(encoder):
    data = {}
    result = encoder.default(data)
    assert isinstance(result, dict)
    assert result == {}

def test_default_with_empty_list(encoder):
    data = []
    result = encoder.default(data)
    assert isinstance(result, list)
    assert result == []

def test_default_with_set(encoder):
    data = {1, 2, 3}
    result = encoder.default(data)
    assert isinstance(result, list)
    assert sorted(result) == [1, 2, 3]  # Sets are unordered, so we sort for comparison

def test_default_with_tuple(encoder):
    data = (1, 2, 3)
    result = encoder.default(data)
    assert isinstance(result, list)
    assert result == [1, 2, 3]

def test_default_with_frozenset(encoder):
    data = frozenset({1, 2, 3})
    result = encoder.default(data)
    assert isinstance(result, list)
    assert sorted(result) == [1, 2, 3]  # Frozensets are unordered, so we sort for comparison
