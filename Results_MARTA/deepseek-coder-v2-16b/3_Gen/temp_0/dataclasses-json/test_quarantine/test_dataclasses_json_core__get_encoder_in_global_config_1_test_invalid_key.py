
import pytest
from dataclasses_json.core import cfg  # Assuming 'cfg' is a module-level configuration object

@pytest.mark.parametrize("type_, expected", [
    ('some_type', expected_encoder),  # Replace with actual expected encoder and type for the test case
])
def test_invalid_key(type_, expected):
    with pytest.raises(KeyError):  # Assuming an appropriate error to raise if key is invalid
        _get_encoder_in_global_config(type_)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__get_encoder_in_global_config_1_test_invalid_key
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__get_encoder_in_global_config_1_test_invalid_key.py:6:18: E0602: Undefined variable 'expected_encoder' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__get_encoder_in_global_config_1_test_invalid_key.py:10:8: E0602: Undefined variable '_get_encoder_in_global_config' (undefined-variable)


"""