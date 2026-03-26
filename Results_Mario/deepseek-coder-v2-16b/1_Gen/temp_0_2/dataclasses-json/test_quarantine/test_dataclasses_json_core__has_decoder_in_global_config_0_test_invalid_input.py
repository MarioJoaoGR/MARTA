
import pytest
from dataclasses_json.core import MockConfig

@pytest.mark.parametrize("type_, expected", [
    ('example_decoder', True),
    ('another_decoder', False),
    (None, False),  # Test with None to ensure it handles unexpected inputs gracefully
])
def test_has_decoder_in_global_config(type_, expected):
    cfg = MockConfig(['example_decoder'])
    assert _has_decoder_in_global_config(type_) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__has_decoder_in_global_config_0_test_invalid_input
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__has_decoder_in_global_config_0_test_invalid_input.py:3:0: E0611: No name 'MockConfig' in module 'dataclasses_json.core' (no-name-in-module)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__has_decoder_in_global_config_0_test_invalid_input.py:12:11: E0602: Undefined variable '_has_decoder_in_global_config' (undefined-variable)


"""