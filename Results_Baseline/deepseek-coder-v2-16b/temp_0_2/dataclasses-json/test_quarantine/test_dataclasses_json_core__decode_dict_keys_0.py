
from typing import Dict, Any, Tuple, List, Optional
import pytest
from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal

# Function under test  
def _decode_dict_keys(key_type, xs, infer_missing):
    decode_function = key_type
    if key_type is None or key_type == Any or isinstance(key_type, typevar):
        decode_function = (lambda x: x)
    elif _get_type_origin(key_type) in {tuple, Tuple}:
        decode_function = tuple
        key_type = key_type

    return list(map(decode_function, xs))

# Test case  
@pytest.mark.parametrize("data, expected", [
    ({1: "value1", 2: "value2"}, {1: "value1", 2: "value2"}),
    ({"key1": {"subkey": "value"}, "key2": {"subkey": "value2"}}, {"key1": {"subkey": "value"}, "key2": {"subkey": "value2"}}),
    ({("key1", "key2"): {"value": "example"}}, {("key1", "key2"): {"value": "example"}})
])
def test_decode_dict_keys(data, expected):
    assert _decode_dict_keys(int, data, False) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__decode_dict_keys_0
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dict_keys_0.py:11:67: E0602: Undefined variable 'typevar' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dict_keys_0.py:13:9: E0602: Undefined variable '_get_type_origin' (undefined-variable)

"""