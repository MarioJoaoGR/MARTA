
import pytest
from dataclasses_json import SchemaF

def test_schemaf_init():
    with pytest.raises(NotImplementedError):
        SchemaF()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_mm_SchemaF___init___0_test_valid_inputs
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_SchemaF___init___0_test_valid_inputs.py:3:0: E0611: No name 'SchemaF' in module 'dataclasses_json' (no-name-in-module)


"""