
import pytest
from datetime import datetime, timezone
from decimal import Decimal
from uuid import UUID
from your_module_name import _support_extended_types  # Replace 'your_module_name' with the actual module name where _support_extended_types is defined

def test_invalid_input_type():
    # Test handling of incorrect input type
    field_type = int
    field_value = "not an integer"
    
    with pytest.raises(ValueError):  # Assuming the function raises a ValueError for invalid types
        res = _support_extended_types(field_type, field_value)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__support_extended_types_0_test_invalid_input_type
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__support_extended_types_0_test_invalid_input_type.py:6:0: E0401: Unable to import 'your_module_name' (import-error)


"""