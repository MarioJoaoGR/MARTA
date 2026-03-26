
import pytest
from dataclasses_json.core import _encode_overrides, OverrideInfo

def test_valid_inputs():
    kvs = {'name': 'John', 'age': 30}
    overrides = {
        'name': OverrideInfo(letter_case=lambda x: x.upper(), encoder=None),
        'age': OverrideInfo(letter_case=None, encoder=str)
    }
    
    result = _encode_overrides(kvs, overrides)
    assert result == {'NAME': 30, 'age': '30'}

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__encode_overrides_0_test_valid_inputs
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__encode_overrides_0_test_valid_inputs.py:3:0: E0611: No name 'OverrideInfo' in module 'dataclasses_json.core' (no-name-in-module)


"""