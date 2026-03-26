
# Module: dataclasses_json.cfg
import pytest
from dataclasses_json import override  # Corrected import statement

def test_override_with_argument():
    assert override(None, _field_name="age") == "age"

def test_override_without_argument():
    assert override(None) is None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_cfg_override_0
dataclasses-json/Test4DT_tests/test_dataclasses_json_cfg_override_0.py:4:0: E0611: No name 'override' in module 'dataclasses_json' (no-name-in-module)

"""