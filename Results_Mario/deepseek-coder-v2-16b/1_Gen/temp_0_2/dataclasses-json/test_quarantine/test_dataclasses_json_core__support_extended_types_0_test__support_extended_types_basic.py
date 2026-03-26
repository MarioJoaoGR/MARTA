
import pytest
from datetime import datetime, timezone
from decimal import Decimal
from uuid import UUID
from your_module_name import _support_extended_types  # Replace 'your_module_name' with the actual module name where `_support_extended_types` is defined.

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

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__support_extended_types_0_test__support_extended_types_basic
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__support_extended_types_0_test__support_extended_types_basic.py:6:0: E0401: Unable to import 'your_module_name' (import-error)


"""