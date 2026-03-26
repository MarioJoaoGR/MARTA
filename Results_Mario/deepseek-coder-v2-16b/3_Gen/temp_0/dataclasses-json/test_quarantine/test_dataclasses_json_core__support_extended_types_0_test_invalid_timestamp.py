
from dataclasses import is_dataclass, fields
from datetime import datetime, timezone
from decimal import Decimal
from uuid import UUID
import pytest
from your_module_name import _support_extended_types  # Replace 'your_module_name' with the actual module name

# Test cases for _support_extended_types function
def test_invalid_timestamp():
    field_type = datetime
    field_value = "not a timestamp"
    
    with pytest.raises(ValueError):
        res = _support_extended_types(field_type, field_value)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__support_extended_types_0_test_invalid_timestamp
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__support_extended_types_0_test_invalid_timestamp.py:7:0: E0401: Unable to import 'your_module_name' (import-error)


"""