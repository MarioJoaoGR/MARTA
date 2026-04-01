
import pytest
from dataclasses_json.core import _encode_overrides, OverrideInfo

def test_invalid_input():
    kvs = {'name': 'John Doe', 'age': 30}
    overrides = {
        'name': OverrideInfo(letter_case=lambda x: x.upper(), encoder=None),
        'age': OverrideInfo(letter_case=None, encoder=str)
    }
    
    with pytest.raises(ValueError):
        _encode_overrides(kvs, overrides)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__encode_overrides_1_test_invalid_input
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__encode_overrides_1_test_invalid_input.py:3:0: E0611: No name 'OverrideInfo' in module 'dataclasses_json.core' (no-name-in-module)


"""