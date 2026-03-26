
from dataclasses_json.core import OverrideInfo
import pytest

def _encode_overrides(kvs, overrides, encode_json=False):
    override_kvs = {}
    for k, v in kvs.items():
        if k in overrides:
            exclude = overrides[k].exclude
            # If the exclude predicate returns true, the key should be
            # excluded from encoding, so skip the rest of the loop
            if exclude and exclude(v):
                continue
            letter_case = overrides[k].letter_case
            original_key = k
            k = letter_case(k) if letter_case is not None else k
            if k in override_kvs:
                raise ValueError(
                    f"Multiple fields map to the same JSON "
                    f"key after letter case encoding: {k}"
                )

            encoder = overrides[original_key].encoder
            v = encoder(v) if encoder is not None else v

        if encode_json:
            v = _encode_json_type(v)
        override_kvs[k] = v
    return override_kvs

# Test case for valid input happy path
def test_valid_input_happy_path():
    from dataclasses import dataclass
    from typing import Dict, Any, Callable
    
    @dataclass
    class OverrideInfo:
        exclude: Callable[[Any], bool] = None
        letter_case: Callable[[str], str] = None
        encoder: Callable[[Any], Any] = None
    
    kvs = {"fieldName": "value"}
    overrides = {"fieldName": OverrideInfo(letter_case=lambda x: x.upper())}
    encoded_kvs = _encode_overrides(kvs, overrides)
    assert encoded_kvs == {'FIELDNAME': 'value'}
    
    kvs = {"fieldName": [1, "string", {"nestedField": "value"}]}
    overrides = {"fieldName": OverrideInfo(encoder=lambda x: str(x))}
    encoded_kvs = _encode_overrides(kvs, overrides, encode_json=True)
    assert encoded_kvs == {'fieldName': ['1', 'string', {'nestedField': '"value"'}]}

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__encode_overrides_0_test_valid_input_happy_path
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__encode_overrides_0_test_valid_input_happy_path.py:2:0: E0611: No name 'OverrideInfo' in module 'dataclasses_json.core' (no-name-in-module)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__encode_overrides_0_test_valid_input_happy_path.py:27:16: E0602: Undefined variable '_encode_json_type' (undefined-variable)


"""