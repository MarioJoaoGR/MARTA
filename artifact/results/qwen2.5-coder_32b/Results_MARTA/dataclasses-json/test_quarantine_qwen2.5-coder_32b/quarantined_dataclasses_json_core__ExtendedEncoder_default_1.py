
import pytest
import json
from datetime import datetime
from uuid import UUID
from enum import Enum
from decimal import Decimal
from collections.abc import Collection, Mapping
from dataclasses_json.core import _ExtendedEncoder

# Helper function to safely check instance types
def _isinstance_safe(obj, cls):
    try:
        return isinstance(obj, cls)
    except Exception:
        return False

class _ExtendedEncoder(json.JSONEncoder):
    def default(self, o) -> json.JsonType:
        result: json.JsonType
        if _isinstance_safe(o, Collection):
            if _isinstance_safe(o, Mapping):
                result = dict(o)
            else:
                result = list(o)
        elif _isinstance_safe(o, datetime):
            result = o.timestamp()
        elif _isinstance_safe(o, UUID):
            result = str(o)
        elif _isinstance_safe(o, Enum):
            result = o.value
        elif _isinstance_safe(o, Decimal):
            result = str(o)
        else:
            result = json.JSONEncoder.default(self, o)
        return result

# Test cases for the _ExtendedEncoder.default method

def test_extended_encoder_list():
    encoder = _ExtendedEncoder()
    example_list = [1, 2, 3]
    serialized_list = json.dumps(example_list, cls=_ExtendedEncoder)
    assert serialized_list == "[1, 2, 3]"

def test_extended_encoder_dict():
    encoder = _ExtendedEncoder()
    example_dict = {'key': 'value'}
    serialized_dict = json.dumps(example_dict, cls=_ExtendedEncoder)
    assert serialized_dict == '{"key": "value"}'

def test_extended_encoder_datetime():
    encoder = _ExtendedEncoder()
    example_datetime = datetime(2023, 1, 1)
    serialized_datetime = json.dumps(example_datetime, cls=_ExtendedEncoder)
    expected_timestamp = str(example_datetime.timestamp())
    assert serialized_datetime == f'"{expected_timestamp}"'

def test_extended_encoder_uuid():
    encoder = _ExtendedEncoder()
    example_uuid = UUID('12345678-1234-5678-1234-567812345678')
    serialized_uuid = json.dumps(example_uuid, cls=_ExtendedEncoder)
    assert serialized_uuid == '"12345678-1234-5678-1234-567812345678"'

def test_extended_encoder_enum():
    encoder = _ExtendedEncoder()
    class Color(Enum):
        RED = 1
        GREEN = 2
    example_enum = Color.RED
    serialized_enum = json.dumps(example_enum, cls=_ExtendedEncoder)
    assert serialized_enum == "1"

def test_extended_encoder_decimal():
    encoder = _ExtendedEncoder()
    example_decimal = Decimal('10.5')
    serialized_decimal = json.dumps(example_decimal, cls=_ExtendedEncoder)
    assert serialized_decimal == '"10.5"'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_qwen2.5-coder_32b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
__ ERROR collecting test_dataclasses_json_core__ExtendedEncoder_default_1.py ___
/opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_qwen2.5-coder_32b/test_dataclasses_json_core__ExtendedEncoder_default_1.py:18: in <module>
    class _ExtendedEncoder(json.JSONEncoder):
/opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_qwen2.5-coder_32b/test_dataclasses_json_core__ExtendedEncoder_default_1.py:19: in _ExtendedEncoder
    def default(self, o) -> json.JsonType:
E   AttributeError: module 'json' has no attribute 'JsonType'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_qwen2.5-coder_32b/test_dataclasses_json_core__ExtendedEncoder_default_1.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.16s ===============================
"""