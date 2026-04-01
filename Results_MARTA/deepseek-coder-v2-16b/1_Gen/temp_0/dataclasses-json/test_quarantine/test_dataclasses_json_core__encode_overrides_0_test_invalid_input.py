
from dataclasses_json.core import OverrideInfo
import pytest

def _encode_overrides(kvs, overrides, encode_json=False):
    override_kvs = {}
    for k, v in kvs.items():
        if k in overrides:
            exclude = overrides[k].exclude
            # If the exclude predicate returns true, the key should be
            #  excluded from encoding, so skip the rest of the loop
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

# Test case for invalid input
def test_invalid_input():
    kvs = {"fieldName": "value"}
    overrides = {"fieldName": OverrideInfo(letter_case=lambda x: x.upper())}
    
    with pytest.raises(ValueError):
        _encode_overrides(kvs, overrides)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__encode_overrides_0_test_invalid_input
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__encode_overrides_0_test_invalid_input.py:2:0: E0611: No name 'OverrideInfo' in module 'dataclasses_json.core' (no-name-in-module)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__encode_overrides_0_test_invalid_input.py:27:16: E0602: Undefined variable '_encode_json_type' (undefined-variable)

"""