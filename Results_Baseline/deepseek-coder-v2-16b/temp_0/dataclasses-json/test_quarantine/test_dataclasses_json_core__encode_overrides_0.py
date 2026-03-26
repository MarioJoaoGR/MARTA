
# Module: dataclasses_json.core
import pytest
from your_module import _encode_overrides  # Replace 'your_module' with the actual module name
from dataclasses import dataclass
from typing import Dict, Any, Callable

# Define OverrideInfo class for testing purposes
@dataclass
class OverrideInfo:
    letter_case: Callable[[str], str] = None
    exclude: Callable[[Any], bool] = None
    encoder: Callable[[Any], Any] = None

# Test cases for _encode_overrides function
def test_basic_encoding():
    kvs = {"fieldName": "value"}
    overrides = {"fieldName": OverrideInfo(letter_case=lambda x: x.upper())}
    encoded_kvs = _encode_overrides(kvs, overrides)
    assert encoded_kvs == {'FIELDNAME': 'value'}

def test_json_encoding():
    kvs = {"fieldName": [1, "string", {"nestedField": "value"}]}
    overrides = {"fieldName": OverrideInfo(encoder=lambda x: str(x))}
    encoded_kvs = _encode_overrides(kvs, overrides, encode_json=True)
    assert encoded_kvs == {'fieldName': ['1', 'string', {'nestedField': '"value"'}]}

def test_exclude():
    kvs = {"fieldName": "value"}
    overrides = {"fieldName": OverrideInfo(exclude=lambda x: isinstance(x, str))}
    encoded_kvs = _encode_overrides(kvs, overrides)
    assert 'fieldName' not in encoded_kvs

def test_multiple_fields():
    kvs = {"field1": "value1", "field2": "value2"}
    overrides = {
        "field1": OverrideInfo(),
        "field2": OverrideInfo()
    }
    with pytest.raises(ValueError):
        _encode_overrides(kvs, overrides)

def test_custom_encoder():
    kvs = {"fieldName": 123}
    overrides = {"fieldName": OverrideInfo(encoder=lambda x: str(x))}
    encoded_kvs = _encode_overrides(kvs, overrides)
    assert encoded_kvs == {'fieldName': '123'}

def test_json_encoding_recursive():
    kvs = {"fieldName": [1, "string", {"nestedField": "value"}]}
    overrides = {"fieldName": OverrideInfo()}
    encoded_kvs = _encode_overrides(kvs, overrides, encode_json=True)
    assert encoded_kvs == {'fieldName': ['1', 'string', {'nestedField': '"value"'}]}

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__encode_overrides_0
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__encode_overrides_0.py:4:0: E0401: Unable to import 'your_module' (import-error)

"""