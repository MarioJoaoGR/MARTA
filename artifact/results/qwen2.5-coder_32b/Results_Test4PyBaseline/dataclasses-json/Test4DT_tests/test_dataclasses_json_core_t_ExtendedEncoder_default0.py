
# Test case  
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

def test_default_with_dict(encoder):
    data = {'key': 'value', 'numbers': [1, 2, 3], 'date': datetime(2023, 1, 1), 'uuid': UUID('12345678-1234-5678-1234-567812345678')}
    result = encoder.default(data)
    assert isinstance(result, dict)
    assert result['key'] == 'value'
    assert result['numbers'] == [1, 2, 3]