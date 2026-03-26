
import pytest
from dataclasses import dataclass, asdict
from typing import Any, Dict, Callable
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class OverrideInfo:
    encoder: Callable[[Any], Any] = None
    letter_case: Callable[[str], str] = None
    exclude: Callable[[Any], bool] = None

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

def test_valid_input_with_json_encoding():
    kvs = {"fieldName": [1, "string", {"nestedField": "value"}]}
    overrides = {"fieldName": OverrideInfo(encoder=lambda x: str(x))}
    encoded_kvs = _encode_overrides(kvs, overrides, encode_json=True)
    assert encoded_kvs == {'fieldName': ['1', 'string', {'nestedField': '"value"'}]}

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__encode_overrides_0_test_valid_input_happy_path
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__encode_overrides_0_test_valid_input_happy_path.py:36:16: E0602: Undefined variable '_encode_json_type' (undefined-variable)

"""