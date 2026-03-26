
import pytest
from dataclasses_json.core import _ExtendedEncoder

def test_valid_input_list():
    value = [1, 2, {"key": "value"}]
    expected_output = [1, 2, {'key': 'value'}]
    
    def default(value):
        return str(value)
    
    result = _encode_json_type(value, default=default)
    
    assert result == expected_output

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__encode_json_type_0_test_valid_input_list
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__encode_json_type_0_test_valid_input_list.py:12:13: E0602: Undefined variable '_encode_json_type' (undefined-variable)


"""