
# Module: dataclasses_json.cfg
import pytest
from dataclasses_json.cfg import override  # Assuming this import statement should be correct based on context

def test_override_default():
    assert override() == 'field_name'

def test_override_with_custom_field_name():
    assert override(None, _field_name='custom_field') == 'custom_field'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_cfg_override_0
dataclasses-json/Test4DT_tests/test_dataclasses_json_cfg_override_0.py:4:0: E0611: No name 'override' in module 'dataclasses_json.cfg' (no-name-in-module)

"""