
import pytest
from dataclasses_json.core import _ExtendedEncoder
import json
from datetime import datetime
from uuid import UUID
import enum
from decimal import Decimal

def test_invalid_inputs():
    encoder = _ExtendedEncoder()
    
    # Test invalid input types
    with pytest.raises(TypeError):
        encoder.default(None)  # None is not a valid type for this encoder
    
    with pytest.raises(TypeError):
        encoder.default([])  # List is not a valid type for this encoder
    
    with pytest.raises(TypeError):
        encoder.default({})  # Dictionary is not a valid type for this encoder
    
    with pytest.raises(TypeError):
        encoder.default("not a datetime")  # String is not a valid datetime
    
    with pytest.raises(TypeError):
        encoder.default(b"not a UUID")  # Bytes is not a valid UUID
    
    with pytest.raises(TypeError):
        encoder.default(123)  # Integer is not a valid enum value
    
    with pytest.raises(TypeError):
        encoder.default(Decimal("invalid"))  # Invalid Decimal string
    
    # Test valid input types
    assert encoder.default(42) == 42
    assert encoder.default("hello") == "hello"
    now = datetime.now()
    assert isinstance(encoder.default(now), float)  # Timestamp representation
    uid = UUID("123e4567-e89b-12d3-a456-426614174000")
    assert encoder.default(uid) == "123e4567-e89b-12d3-a456-426614174000"
    class MyEnum(enum.Enum):
        VALUE = "example"
    assert encoder.default(MyEnum.VALUE) == "example"
    assert encoder.default(Decimal("123.45")) == "123.45"
    assert encoder.default({"key": "value"}) == {"key": "value"}

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__ExtendedEncoder_default_0_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        encoder = _ExtendedEncoder()
    
        # Test invalid input types
        with pytest.raises(TypeError):
            encoder.default(None)  # None is not a valid type for this encoder
    
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__ExtendedEncoder_default_0_test_invalid_inputs.py:17: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_core__ExtendedEncoder_default_0_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.04s ===============================
"""