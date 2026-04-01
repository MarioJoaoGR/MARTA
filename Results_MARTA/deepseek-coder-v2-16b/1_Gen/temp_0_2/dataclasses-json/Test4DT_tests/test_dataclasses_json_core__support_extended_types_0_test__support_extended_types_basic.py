
import pytest
from datetime import datetime, timezone
from decimal import Decimal
from uuid import UUID
from dataclasses_json.core import _support_extended_types

def test__support_extended_types_basic():
    # Test conversion of timestamp to datetime object
    assert isinstance(_support_extended_types(datetime, 1633072800), datetime)
    
    # Test conversion of string to Decimal
    assert _support_extended_types(Decimal, "123.45") == Decimal('123.45')
    
    # Test conversion of string to UUID
    assert isinstance(_support_extended_types(UUID, "123e4567-e89b-12d3-a456-426614174000"), UUID)
    
    # Test conversion of string to int
    assert _support_extended_types(int, "123") == 123
    
    # Test conversion of string to float
    assert _support_extended_types(float, "123.45") == 123.45
    
    # Test leaving int unchanged as str
    assert _support_extended_types(str, 123) == '123'
    
    # Test conversion of string to bool
    assert _support_extended_types(bool, "True") is True

# Helper function to check if a class is a subclass (safe version)
def _issubclass_safe(cls, base):
    return isinstance(cls, type) and issubclass(cls, base)
